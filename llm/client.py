import json
import os
import requests

TOOLS_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'agent', 'tools.md')


def _load_tools():
    try:
        with open(TOOLS_PATH, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        return ''

    result = []
    for line in lines[2:]:
        line = line.strip()
        if not line or not line.startswith('|'):
            continue
        parts = [p.strip() for p in line.split('|')]
        if len(parts) >= 5:
            block_type = parts[1]
            category = parts[2]
            func = parts[3]
            result.append(f'- [{block_type}] {category}: {func}')

    return '\n'.join(result)


class LLMClient:
    def __init__(self, api_key=None, base_url=None, model=None):
        self.api_key = api_key or os.getenv('LLM_API_KEY', '')
        self.base_url = (base_url or os.getenv('LLM_BASE_URL', 'https://api.openai.com/v1')).rstrip('/')
        self.model = model or os.getenv('LLM_MODEL', 'gpt-4o')
        self._messages = []

    def chat(self, messages, temperature=0.7, max_tokens=4096):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": self.model,
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens
        }
        try:
            resp = requests.post(f"{self.base_url}/chat/completions",
                                 headers=headers, json=payload, timeout=120)
            resp.raise_for_status()
            result = resp.json()
            return result["choices"][0]["message"]["content"]
        except requests.exceptions.HTTPError as e:
            detail = resp.text[:500] if 'resp' in dir() else ''
            raise RuntimeError(f'API {resp.status_code}: {detail}') from e
        except (KeyError, IndexError) as e:
            raise RuntimeError(f'Unexpected API response: {resp.text[:300]}') from e

    def chat_stream(self, messages, temperature=0.7, max_tokens=4096):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": self.model,
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens,
            "stream": True
        }
        try:
            resp = requests.post(f"{self.base_url}/chat/completions",
                                 headers=headers, json=payload, timeout=120, stream=True)
            resp.raise_for_status()
            for line in resp.iter_lines():
                if line:
                    line = line.decode('utf-8')
                    if line.startswith('data: '):
                        data = line[6:]
                        if data == '[DONE]':
                            break
                        try:
                            chunk = json.loads(data)
                            delta = chunk['choices'][0].get('delta', {})
                            content = delta.get('content', '')
                            if content:
                                yield content
                        except json.JSONDecodeError:
                            pass
        except requests.exceptions.HTTPError as e:
            detail = resp.text[:500] if 'resp' in dir() else ''
            raise RuntimeError(f'API {resp.status_code}: {detail}') from e
        except (KeyError, IndexError) as e:
            raise RuntimeError(f'Unexpected API response: {resp.text[:300]}') from e

    def chat_or_generate_stream(self, prompt):
        tools_ref = _load_tools()
        system_prompt = """你是 Scratcher，一个 Scratch 项目助手。你可以：
1. 正常对话 — 回答用户的问题、闲聊等
2. 生成 Scratch 项目 — 当用户要求创建项目时

如果用户要求创建 Scratch 项目，请输出一个 JSON 项目结构，并用 ```json ... ``` 代码块包裹。
如果只是普通对话，直接回复文本即可。

项目 JSON 格式示例：
```json
{{
  "sprites": [
    {{
      "name": "Sprite1",
      "x": 0, "y": 0, "size": 100, "direction": 90,
      "costume": {{
        "type": "circle",
        "color": "#4A90D9",
        "radius": 50,
        "label": "A"
      }},
      "scripts": [
        {{"opcode": "event_whenflagclicked"}},
        {{"opcode": "motion_movesteps", "steps": 10}},
        {{"opcode": "control_wait", "secs": 1}},
        {{"opcode": "motion_turnright", "degrees": 15}}
      ]
    }}
  ],
  "backdrop": {{
    "type": "color",
    "color": "#87CEEB"
  }}
}}

支持的 costume 类型:
- circle: {{ "type": "circle", "color": "#hex", "radius": 50, "label": "A" }}
- rect: {{ "type": "rect", "color": "#hex", "width": 80, "height": 80, "rx": 8 }}
- star: {{ "type": "star", "color": "#hex", "size": 60 }}
- arrow: {{ "type": "arrow", "color": "#hex", "size": 50, "direction": "right" }}

支持的 backdrop 类型:
- color: {{ "type": "color", "color": "#hex" }}
- grid: {{ "type": "grid", "color1": "#hex", "color2": "#hex", "rows": 3, "cols": 4 }}

以下是所有可用的 Scratch 积木块参考（来自 tools.md）：
{tools}""".format(tools=tools_ref)

        if not self._messages:
            self._messages = [{"role": "system", "content": system_prompt}]
        self._messages.append({"role": "user", "content": prompt})

        full = ''
        for chunk in self.chat_stream(self._messages):
            full += chunk
            yield ('chunk', chunk)

        self._messages.append({"role": "assistant", "content": full})

        cleaned = full.strip()
        if '```' in cleaned:
            parts = cleaned.split('```')
            for i, part in enumerate(parts):
                p = part.strip()
                if p.startswith('json'):
                    p = p[4:].strip()
                try:
                    data = json.loads(p)
                    yield ('project', data)
                    return
                except json.JSONDecodeError:
                    continue
        try:
            data = json.loads(cleaned)
            yield ('project', data)
        except json.JSONDecodeError:
            yield ('chat', full)
