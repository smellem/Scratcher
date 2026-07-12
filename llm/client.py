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
        resp = requests.post(f"{self.base_url}/chat/completions",
                             headers=headers, json=payload, timeout=120)
        resp.raise_for_status()
        return resp.json()["choices"][0]["message"]["content"]

    def generate_project(self, prompt):
        system_prompt = """你是一个 Scratch 项目生成器。根据用户的自然语言描述，生成一个完整的 Scratch 3.0 项目。

请严格按照以下 JSON 格式输出（不要包含 markdown 代码块标记）：

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
{tools}"""


        tools_ref = _load_tools()
        system_prompt = system_prompt.format(tools=tools_ref)

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ]
        response = self.chat(messages)
        cleaned = response.strip()
        if cleaned.startswith('```'):
            cleaned = cleaned.split('\n', 1)[-1]
            cleaned = cleaned.rsplit('```', 1)[0]
        if cleaned.startswith('json'):
            cleaned = cleaned[4:]
        return json.loads(cleaned.strip())