# Scratcher

通过自然语言描述生成 Scratch 3.0 项目（.sb3）的命令行工具，支持 LLM 驱动和扩展系统。

## 安装

```bash
pip install -r requirements.txt
```

## 快速开始

```bash
# 交互模式（首次运行会引导设置 API）
python main.py

# 直接指定描述
python main.py "创建一个红色的小猫，点击绿旗后向右移动 50 步"

# 生成测试项目（不调用 LLM）
python main.py --no-llm -o demo.sb3

# 指定语言
python main.py --lang en "create a cat that moves 10 steps"
```

## 功能

- **LLM 驱动**：接入大模型，用自然语言描述生成完整项目
- **SVG 生成**：支持圆形、矩形、星形、箭头等精灵模板
- **积木系统**：30+ 种 Scratch 积木块（运动/外观/事件/控制/侦测/运算/变量）
- **扩展系统**：`.editor` 插件包，支持 TurboWarp 扩展
- **打包/解包**：同时输出 `.sb3` 文件和可编辑的解包目录
- **i18n**：支持中英文界面

## 编辑器扩展管理

```bash
python main.py --editors
```

在管理界面中可以：
- 启用/禁用扩展
- 安装 `.editor` 插件包
- 导出 TurboWarp 扩展（`.js`）
- 合并扩展积木到 `tools.md`

## 配置文件

`config.yaml` 保存 LLM API 配置，支持自定义供应商：

```yaml
api_key: sk-xxx
base_url: https://api.deepseek.com
model: deepseek-v4-flash
```

支持的环境变量：`LLM_API_KEY`、`LLM_BASE_URL`、`LLM_MODEL`

## 项目结构

```
Scratcher/
├── main.py              # 入口
├── svg/                 # SVG 生成引擎
├── scratch/             # Scratch 项目构建
│   ├── project.py       # .sb3 打包
│   ├── sprite.py        # 精灵/造型
│   └── blocks.py        # 积木块构建
├── llm/                 # LLM 集成
├── editor/              # 扩展系统
│   ├── manager.py       # 扩展管理器
│   ├── ui.py            # 终端界面
│   └── *.editor         # 扩展包
├── agent/
│   └── tools.md         # 积木参考表
└── i18n/                # 国际化
    ├── zh.json
    └── en.json
```

## 许可

MIT
