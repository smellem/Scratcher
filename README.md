# Scratcher

[中文](README.zh.md)

Generate Scratch 3.0 projects (.sb3) from natural language descriptions via LLM.

## How It Works

```
User Prompt → LLM → Structured JSON → SVG + Blocks → .sb3 (zip) + Extracted Directory
```

**Pipeline:**

1. **Prompt** — User describes the desired Scratch project in natural language (e.g. "a red cat that moves 10 steps when the flag is clicked")
2. **LLM Parsing** — The LLM receives the prompt along with the full block reference (`agent/tools.md`) and outputs a structured JSON describing sprites, costumes, backdrops, and scripts
3. **Asset Generation** — SVG costumes are generated from templates (circle, rect, star, arrow) or custom specifications
4. **Script Building** — Scratch blocks are constructed from the parsed JSON and linked into execution chains
5. **Packaging** — The project is saved as `.sb3` (a standard Scratch 3.0 zip archive) and extracted to a editable directory

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### Interactive Mode

```bash
python main.py
```

On first run, you will be prompted to configure an LLM API:

```text
=== Scratcher Initialization ===
No API configured. Please set up the following:

API Key: sk-xxx

Select API provider:
  1. OpenAI          (https://api.openai.com/v1)
  2. DeepSeek        (https://api.deepseek.com)
  3. 通义千问        (https://dashscope.aliyuncs.com/compatible-mode/v1)
  4. Custom URL
Choose (1-4): 2
Save config? (y/n): y
Config saved to config.yaml
```

After setup, describe your project:

```text
Describe the Scratch project you want to generate: a blue cat that spins when clicked
```

### Direct Prompt

```bash
python main.py "a red square that moves to x:100 y:100 when space is pressed"
```

### Test Project (No LLM)

```bash
python main.py --no-llm -o demo.sb3
```

### Language Selection

```bash
python main.py --lang en "create a bouncing ball"
python main.py --lang zh "创建一个弹跳的小球"
```

### Extension Manager

```bash
python main.py --editors
```

## Configuration

`config.yaml` stores your LLM API configuration:

```yaml
api_key: sk-xxx
base_url: https://api.deepseek.com
model: deepseek-v4-flash
```

Environment variables are also supported: `LLM_API_KEY`, `LLM_BASE_URL`, `LLM_MODEL`.

## Project Structure

```
Scratcher/
├── main.py              # Entry point, CLI, pipeline orchestration
├── svg/                 # SVG rendering engine
│   ├── generator.py     # Shapes, gradients, filters, paths, transforms
│   └── templates.py     # Sprite templates (circle, rect, star, arrow)
├── scratch/             # Scratch project builder
│   ├── project.py       # .sb3 packaging (zip + project.json + assets)
│   ├── sprite.py        # Sprite, costume, sound models
│   └── blocks.py        # Block builder (30+ block types)
├── llm/                 # LLM integration
│   └── client.py        # API client, prompt construction, response parsing
├── editor/              # Extension system
│   ├── manager.py       # Extension scanner, merger, lifecycle
│   ├── ui.py            # Terminal UI for extension management
│   └── *.editor         # Extension packages (zip with pack.json + tools.md)
├── agent/
│   └── tools.md         # Scratch block reference (fed to LLM as context)
├── i18n/                # Internationalization
│   ├── zh.json          # Chinese
│   └── en.json          # English
├── config.yaml          # LLM API configuration (gitignored)
└── requirements.txt     # Python dependencies
```

## Extension System

Extensions (`.editor` files) are zip archives containing:

- `pack.json` — metadata (name, version, author, enabled state)
- `agent/tools.md` — additional Scratch blocks to merge into the reference
- (optional) Extension scripts for TurboWarp

Run `python main.py --editors` to manage extensions: enable/disable, install, export.

### Available Extensions

| Extension | Description |
|-----------|-------------|
| `motion-plus.editor` | Additional motion and looks blocks |
| `tw-settings.editor` | TurboWarp advanced settings (framerate, interpolation, pen quality, clone limit) |

## Changelog

See [CHANGELOG.md](CHANGELOG.md).

## License

MIT
