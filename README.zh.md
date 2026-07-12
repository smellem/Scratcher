# Scratcher

[English](README.md)

通过自然语言描述生成 Scratch 3.0 项目（.sb3）的命令行工具，由 LLM 驱动并支持扩展系统。

## 工作原理

```
用户描述 → LLM → 结构化 JSON → SVG + 积木块 → .sb3 (zip) + 解包目录
```

**流程：**

1. **提示** — 用户用自然语言描述所需的 Scratch 项目（例如"一只红色小猫，点击绿旗后移动 10 步"）
2. **LLM 解析** — LLM 接收用户描述和完整的积木块参考表 (`agent/tools.md`)，输出结构化 JSON，包含精灵、造型、背景和脚本的定义
3. **资源生成** — 从模板（圆形、矩形、星形、箭头）或自定义规格生成 SVG 造型
4. **积木构建** — 根据解析后的 JSON 构建 Scratch 积木块，并链接为执行链
5. **打包** — 项目保存为 `.sb3`（标准 Scratch 3.0 zip 归档），同时解包到可编辑的目录

## 安装

```bash
pip install -r requirements.txt
```

## 使用方法

### 交互模式

```bash
python main.py
```

首次运行会引导配置 LLM API：

```text
=== Scratcher 初始化 ===
检测到未配置 LLM API，请设置以下信息：

API Key: sk-xxx

选择 API 供应商：
  1. OpenAI          (https://api.openai.com/v1)
  2. DeepSeek        (https://api.deepseek.com)
  3. 通义千问        (https://dashscope.aliyuncs.com/compatible-mode/v1)
  4. 自定义地址
请选择 (1-4): 2
是否保存配置？(y/n): y
配置已保存到 config.yaml
```

配置完成后，输入项目描述：

```text
请输入你想要生成的 Scratch 项目描述: 创建一个蓝色的猫，点击后旋转
```

### 直接指定描述

```bash
python main.py "一个红色正方形，按下空格键移动到 x:100 y:100"
```

### 测试项目（不调用 LLM）

```bash
python main.py --no-llm -o demo.sb3
```

### 语言选择

```bash
python main.py --lang en "create a bouncing ball"
python main.py --lang zh "创建一个弹跳的小球"
```

### 扩展管理

```bash
python main.py --editors
```

## 配置文件

`config.yaml` 保存 LLM API 配置：

```yaml
api_key: sk-xxx
base_url: https://api.deepseek.com
model: deepseek-v4-flash
```

也支持环境变量：`LLM_API_KEY`、`LLM_BASE_URL`、`LLM_MODEL`。

## 项目结构

```
Scratcher/
├── main.py              # 入口，CLI，流程编排
├── svg/                 # SVG 渲染引擎
│   ├── generator.py     # 形状、渐变、滤镜、路径、变换
│   └── templates.py     # 精灵模板（圆形、矩形、星形、箭头）
├── scratch/             # Scratch 项目构建
│   ├── project.py       # .sb3 打包（zip + project.json + 资源）
│   ├── sprite.py        # 精灵、造型、声音模型
│   └── blocks.py        # 积木块构建器（30+ 种积木类型）
├── llm/                 # LLM 集成
│   └── client.py        # API 客户端、提示构建、响应解析
├── editor/              # 扩展系统
│   ├── manager.py       # 扩展扫描、合并、生命周期管理
│   ├── ui.py            # 终端管理界面
│   └── *.editor         # 扩展包（zip，含 pack.json + tools.md）
├── agent/
│   └── tools.md         # Scratch 积木参考表（作为上下文提供给 LLM）
├── i18n/                # 国际化
│   ├── zh.json          # 中文
│   └── en.json          # 英文
├── config.yaml          # LLM API 配置（已被 gitignore）
└── requirements.txt     # Python 依赖
```

## 扩展系统

扩展（`.editor` 文件）是 zip 归档包，包含：

- `pack.json` — 元数据（名称、版本、作者、启用状态）
- `agent/tools.md` — 需要合并到参考表的额外积木块
- （可选）TurboWarp 扩展脚本

运行 `python main.py --editors` 管理扩展：启用/禁用、安装、导出。

### 可用扩展

| 扩展 | 说明 |
|------|------|
| `motion-plus.editor` | 额外的运动和外观积木 |
| `tw-settings.editor` | TurboWarp 高级设置（帧率、插值、画笔质量、克隆体上限） |

## 更新日志

参见 [CHANGELOG.md](CHANGELOG.md)。

## 许可

MIT
