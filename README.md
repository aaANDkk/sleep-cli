# 🐾 sleep-cli · 猫娘の安眠伴侣

> **「 ご主人様、今日も一日お疲れ様でしたにゃ！ 晚安与专注の猫娘添い寝タイマー 」**

一个轻量、超萌治愈的命令行睡眠与专注倒计时小工具。  
猫娘会在终端守着ご主人様（主人大人）小憩或入眠，内置 90 分钟 R.E.M 睡眠周期计算器（にゃんこ計算機）。  
纯 Python 标准库编写，无需安装任何额外依赖，开箱即用にゃ！

---

## 機能紹介 / 功能介绍

- **倒计时と进度条**：支持秒 (s)、分 (m)、小时 (h) 自由设定，终端显示猫猫字符进度与小猫表情（`(^･ω･^)`）。
- **猫娘の小憩モード**：内置 20 分钟猫猫浅睡小憩（`--nap`）与 90 分钟完整深眠物语（`--deep`）。
- **にゃんこ周期計算**：基于 90 分钟 R.E.M 生理律动，为ご主人様推算最舒服的苏醒时间点。
- **猫娘の囁き（温柔轻语）**：随时听猫娘给你说一句暖暖的治愈鼓励与晚安情话。
- **零依存（Zero Dependencies）**：纯 Python 3 标准库打造，绿色无污染にゃ。

---

## 使い方 / 使用方法

### 1. 基础倒计时（小憩 / 专注）

```bash
# 默认 25 分钟小憩
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

### 3. 最佳苏醒时刻の推算 (にゃんこ計算機)

计算如果现在和猫娘一起入睡，在哪些时刻醒来最神清气爽喵：

```bash
python sleep_cli.py --cycles
# 或简写
python sleep_cli.py -c
```

### 4. 听猫娘说句温柔轻语 (猫娘の囁き)

```bash
python sleep_cli.py --quote
# 或简写
python sleep_cli.py -q
```

---

## 参数一覧

| 参数 | 简写 | 说明 | 示例 |
| --- | --- | --- | --- |
| `duration` | - | 自定义倒计时时长（默认 25m） | `python sleep_cli.py 30m` |
| `--nap` | - | 开启 20 分钟浅睡小憩 (うたた寝にゃ) | `python sleep_cli.py --nap` |
| `--deep` | - | 开启 90 分钟深眠物语 (ぐっすり夢の中) | `python sleep_cli.py --deep` |
| `--cycles` | `-c` | 智能推算最适合ご主人様的苏醒时刻 | `python sleep_cli.py -c` |
| `--quote` | `-q` | 抽取一句猫娘の温柔轻语 | `python sleep_cli.py -q` |
| `--help` | `-h` | 查看使用案内にゃ | `python sleep_cli.py -h` |

---

## ライセンス / 许可证

本项目基于 [MIT License](LICENSE) 开源，ご主人様请随意使用喵！
