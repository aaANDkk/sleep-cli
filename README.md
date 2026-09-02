# 💤 sleep-cli

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

> **专为精通 Sleep() 函数的开发者打造的终端睡眠与专注伴侣。**  
> 拒绝疲劳编码，科学小憩，保持大脑高并发运行状态。

---

## ✨ 核心特性

- ⏳ **终端动态进度条**：酷炫的终端字符进度条、倒计时与动态刷新。
- 🧠 **90 分钟 R.E.M 睡眠周期计算器**：基于人类睡眠生理周期，智能计算从当前时刻入睡的最佳苏醒时间，避免起床时的睡眠惯性与头晕。
- ⚡ **快速预设模式**：支持一键开启 20 分钟强力小憩（Power Nap）或 90 分钟完整深度睡眠。
- 💡 **极客哲学金句**：随机输出关于休息、编码与人生的哲思名言。
- 🪶 **零第三方依赖**：纯 Python 标准库编写，无需任何 pip install，开箱即用。

---

## 🚀 快速上手与使用指南

确保电脑已安装 Python 3.8 或更高版本：

### 1. 基础小憩 / 倒计时
直接传入时长（支持 s 秒、m 分钟、h 小时）：

`ash
# 倒计时 25 分钟（番茄钟 / 小憩，默认时长）
python sleep_cli.py 25m

# 倒计时 1 小时
python sleep_cli.py 1h

# 倒计时 45 秒（快速测试）
python sleep_cli.py 45s
`

### 2. 快捷模式
`ash
# ⚡ 20 分钟强力小憩（快速恢复脑力）
python sleep_cli.py --nap

# 🌙 90 分钟深度睡眠（完整 R.E.M 周期）
python sleep_cli.py --deep
`

### 3. 睡眠周期智能计算
计算从**当前时间**开始入睡，最适合在几点起床（按 1.5 小时为一个完整周期计算）：

`ash
python sleep_cli.py --cycles
# 或缩写：
python sleep_cli.py -c
`

*输出示例：*
`
🧠 Sleep Cycle Calculator (90-min R.E.M Cycles)
Current Time: 2026-09-02 21:16:37

If you go to sleep RIGHT NOW, wake up at one of these times to feel refreshed:
--------------------------------------------------
 • 11:01 PM (23:01) -> 1 cycle (1.5 hrs) ⚡ Power Nap
 • 12:31 AM (00:31) -> 2 cycles (3.0 hrs) 
 • 02:01 AM (02:01) -> 3 cycles (4.5 hrs) 
 • 03:31 AM (03:31) -> 4 cycles (6.0 hrs) 
 • 05:01 AM (05:01) -> 5 cycles (7.5 hrs) ⭐ Recommended (Optimal rest)
 • 06:31 AM (06:31) -> 6 cycles (9.0 hrs) ⭐ Recommended (Optimal rest)
--------------------------------------------------
`

### 4. 随机极客哲思
`ash
python sleep_cli.py --quote
# 或缩写：
python sleep_cli.py -q
`

---

## 🛠️ 参数速查表

| 参数 | 全称 | 说明 | 示例 |
| :--- | :--- | :--- | :--- |
| [duration] | - | 自定义倒计时时长（默认 25m） | python sleep_cli.py 30m |
| --nap | - | 开启 20 分钟强力小憩 | python sleep_cli.py --nap |
| --deep | - | 开启 90 分钟完整周期深度睡眠 | python sleep_cli.py --deep |
| -c | --cycles | 计算当前入睡的最佳起床时间 | python sleep_cli.py -c |
| -q | --quote | 随机显示一条极客哲思金句 | python sleep_cli.py -q |
| -h | --help | 查看帮助文档 | python sleep_cli.py -h |

---

## 📄 开源协议

本项目基于 [MIT License](LICENSE) 开源。
