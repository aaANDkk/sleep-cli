# 🐾 sleep-cli · 猫娘の安眠伴侣

```text
             ∧＿∧             ✦ · ° zzZ
            ( =˘ω˘= )          ~ (呼噜呼噜... 添い寝中)
          .─/  つ づ─.        [ sleep-cli · 猫娘伴侣 ]
         (   (   "   )   )     ✨ 今夜もいい夢を見てにゃ〜
          `─'~~~~~~~~~`─'
```

> **「 ご主人様、今日も一日お疲れ様でしたにゃ！ 晚安与专注の全彩动态猫娘添い寝タイマー 」**

一个轻量、超萌治愈的命令行睡眠与专注倒计时小工具。  
Q版二次元猫娘裹着小毯子在终端陪着ご主人様（主人大人）小憩或入眠，内置 90 分钟 R.E.M 睡眠周期计算器（にゃんこ計算機）、**全彩流光霓虹动画**与**动态 AI 轻语引擎**。  
纯 Python 标准库编写，无需安装任何额外依赖，开箱即用にゃ！

---

## 機能紹介 / 功能介绍

- **Q版二次元全彩猫娘（Full-Color Anime Neko）**：裹着薰衣草小毯子、粉萌猫耳、珊瑚腮红与摇晃尾巴的立体治愈猫猫！
- **6 FPS 丝滑微动引擎（Live ASCII Animation）**：头顶飘浮金色星芒与上升呼噜气泡（`zzZ`）、猫尾左右摇曳、自然眨眼打盹，全程丝滑无频闪！
- **流光霓虹渐变进度条（Rainbow Wave Progress）**：动态彩色流光呼吸波浪，终端颜值拉满。
- **桌面动态摸猫模式（`--live`）**：随时化身为桌面上默默陪伴你写代码或休息的治愈呼噜伴侣。
- **倒计时と进度条**：支持秒 (s)、分 (m)、小时 (h) 自由设定。
- **猫娘の小憩モード**：内置 20 分钟猫猫浅睡小憩（`--nap`）与 90 分钟完整深眠物语（`--deep`）。
- **にゃんこ周期計算**：基于 90 分钟 R.E.M 生理律动，为ご主人様推算最舒服的苏醒时间点。
- **动态猫娘音声（AI 轻语引擎）**：
  - **支持 AI 大模型对话**：已支持配置 DeepSeek / OpenAI / SiliconFlow 等 API Key，开启与猫娘的专属互动倾诉（`--chat`）；
  - **免配置海量句库**：自动从动漫/文学数据库实时获取金句并由猫娘萌化演播，千言万语绝不重样；
  - **离线时段自适应**：断网时根据清晨、午休、傍晚、深夜自动组合专属猫娘情话。
- **时段感知问候**：根据当前系统时间，小猫横幅会动态给出早安、午休、晚安或催睡提醒。
- **零依存（Zero Dependencies）**：纯 Python 3 标准库打造，绿色无污染にゃ。

---

## 🚀 安装与快速上手 / Quick Start

### 第一步：将项目下载到本地文件夹

打开你常用的终端（Windows Terminal / PowerShell / CMD / Git Bash），运行以下命令将项目克隆到本地并进入文件夹：

```bash
# 1. 克隆项目到本地
git clone https://github.com/aaANDkk/sleep-cli.git

# 2. 打开终端，进入项目文件夹
cd sleep-cli
```

> 💡 **免 Git 方式**：也可以直接在 GitHub 页面点击右上角绿色的 **Code** -> **Download ZIP**，下载解压后，在解压后的文件夹内空白处右键选择 **“在终端中打开 (Open in Terminal)”** 即可。

### 第二步：环境准备

本项目基于 **Python 3 标准库** 打造，**无需执行 `pip install` 安装任何第三方依赖库**，纯绿色零污染！  
只需确保电脑已安装 Python（推荐 Python 3.7+）：

```bash
python --version
```

---

## 使い方 / 常用指令与功能演示

### 1. 基础倒计时（小憩 / 专注 · 动态猫娘陪睡）

```bash
# 默认 25 分钟小憩（倒计时期间猫娘会实时呼吸眨眼打呼噜喵）
python sleep_cli.py 25m

# 自定义时长（支持 s 秒 / m 分 / h 小时）
python sleep_cli.py 45s
python sleep_cli.py 1h
```

### 2. 快捷模式

```bash
# 🐾 浅睡小憩 · 20 分钟猫猫快速充电 (うたた寝にゃ)
python sleep_cli.py --nap

# 🌙 深眠物语 · 90 分钟完整深眠周期 (ぐっすり夢の中)
python sleep_cli.py --deep
```

### 3. 桌面动态摸猫模式 (Live Companion)

```bash
# 开启桌面动态猫娘陪伴（常驻在终端角落打呼噜、眨眼陪伴，按 Ctrl+C 退出）
python sleep_cli.py --live
```

### 4. 最佳苏醒时刻の推算 (にゃんこ計算機)

计算如果现在和猫娘一起入睡，在哪些时刻醒来最神清气爽喵：

```bash
python sleep_cli.py --cycles
# 或简写
python sleep_cli.py -c
```

### 5. 抽取动态猫娘轻语与互动 (猫娘の囁き)

```bash
# 随机获取一句动态轻语（自动联网获取海量名言并猫娘化）
python sleep_cli.py -q

# 向猫娘诉苦或分享心情（自动针对性共情安抚）
python sleep_cli.py -q "今天写代码好累"
python sleep_cli.py -q "今天不想学考研内容了，想早点休息睡觉"

# 专属对话倾诉模式（调用本地配置的 DeepSeek/OpenAI 大模型）
python sleep_cli.py --chat "今天被Bug折磨了一整天"
```

---

## 🤖 AI 大模型接入案内 / API 配置教程

如果你想让猫娘拥有更强大的 AI 思考与无限畅聊能力，可以接入任何兼容 OpenAI 格式的大模型（如 **DeepSeek**、**OpenAI**、**硅基流动 SiliconFlow**、**Kimi**、**通义千问** 等）。

> 🔒 **安全承诺**：密钥会保存在本地 `config.json` 中，该文件已加入 `.gitignore`，**绝对不会**被上传到 GitHub 远程仓库！

### 快速配置指令：

```bash
# 1. 接入 DeepSeek 官方大模型（推荐，超高性价比）
python sleep_cli.py --set-key "sk-你的DeepSeek密钥" --set-base "https://api.deepseek.com/v1" --set-model "deepseek-chat"

# 2. 接入 OpenAI 官方大模型
python sleep_cli.py --set-key "sk-你的OpenAI密钥" --set-model "gpt-4o-mini"

# 3. 接入 硅基流动 SiliconFlow（支持免费白嫖 Qwen / DeepSeek-V3 等开源模型）
python sleep_cli.py --set-key "sk-你的密钥" --set-base "https://api.siliconflow.cn/v1" --set-model "deepseek-ai/DeepSeek-V3"

# 4. 查看当前本地 AI 配置状态（密钥自动打码保护）
python sleep_cli.py --show-config
```

> 💡 *若不配置 API Key，工具也会自动启用内置的「智能情境共情引擎」与「免配置动漫名言库」，完全不影响日常使用喵！*

---

## 参数一覧

| 参数 | 简写 | 说明 | 示例 |
| --- | --- | --- | --- |
| `duration` | - | 自定义倒计时时长（动态猫娘实时陪伴） | `python sleep_cli.py 30m` |
| `--nap` | - | 开启 20 分钟浅睡小憩 (うたた寝にゃ) | `python sleep_cli.py --nap` |
| `--deep` | - | 开启 90 分钟深眠物语 (ぐっすり夢の中) | `python sleep_cli.py --deep` |
| `--live` | `--pet` | 启动桌面动态猫娘陪伴模式 | `python sleep_cli.py --live` |
| `--cycles` | `-c` | 智能推算最适合ご主人様的苏醒时刻 | `python sleep_cli.py -c` |
| `-q [话题]` | `--quote` | 抽取动态猫娘轻语 / 倾诉心情 | `python sleep_cli.py -q "好累"` |
| `--chat [话语]`| - | 向猫娘倾诉心事并获取专属 AI 安抚 | `python sleep_cli.py --chat "想睡觉了"` |
| `--set-key [KEY]`| - | 配置本地 AI API Key（绝不上云） | `python sleep_cli.py --set-key "sk-..."` |
| `--set-base [URL]`| - | 配置自定义 API Base URL | `python sleep_cli.py --set-base "https://..."` |
| `--set-model [NAME]`| - | 配置使用的模型名称 | `python sleep_cli.py --set-model "deepseek-chat"` |
| `--show-config` | - | 查看当前 AI 配置状态 | `python sleep_cli.py --show-config` |
| `--help` | `-h` | 查看使用案内にゃ | `python sleep_cli.py -h` |

---

## ライセンス / 许可证

本项目基于 [MIT License](LICENSE) 开源，ご主人様请随意使用喵！
