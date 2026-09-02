# sleep-cli

> **「 晚安与专注の小憩 · 陪伴每个静谧夜晚与小憩时光 」**

一个轻量、治愈的命令行睡眠与专注倒计时工具，内置 90 分钟 R.E.M 睡眠周期计算。  
基于 Python 标准库实现，无需配置任何额外依赖。

---

## 機能紹介 / 功能介绍

- **倒计时と进度条**：支持秒 (s)、分 (m)、小时 (h) 自由设置，终端显示静谧字符进度与剩余时间。
- **预设の小憩模式**：内置 20 分钟浅睡充电（Power Nap）与 90 分钟完整深眠模式。
- **睡眠周期の计算**：根据当前入眠时刻，科学推算 90 分钟 R.E.M 生理周期的最佳苏醒时间点。
- **温柔の寄语**：内置文学名家与生活治愈系随想语录。
- **零依赖**：纯 Python 3 标准库打造，开箱即用。

---

## 使い方 / 使用方法

### 1. 基础倒计时

```bash
# 默认 25 分钟小憩 / 专注时间
python sleep_cli.py 25m

# 自定义时长（支持 s / m / h）
python sleep_cli.py 45s
python sleep_cli.py 1h
```

### 2. 快捷模式

```bash
# 浅睡小憩 · 20 分钟快速充电
python sleep_cli.py --nap

# 深眠物语 · 90 分钟完整周期
python sleep_cli.py --deep
```

### 3. 最佳苏醒时刻の推算

计算如果从当前时刻入眠，在哪些时间醒来能避开深睡眠阶段、醒后更加清爽：

```bash
python sleep_cli.py --cycles
# 或简写
python sleep_cli.py -c
```

### 4. 抽取温暖寄语

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
| `--nap` | - | 开启 20 分钟浅睡小憩 | `python sleep_cli.py --nap` |
| `--deep` | - | 开启 90 分钟深度睡眠 | `python sleep_cli.py --deep` |
| `--cycles` | `-c` | 推算当前入眠的最佳起床时间 | `python sleep_cli.py -c` |
| `--quote` | `-q` | 抽取一句温柔寄语 | `python sleep_cli.py -q` |
| `--help` | `-h` | 查看使用案内 | `python sleep_cli.py -h` |

---

## ライセンス / 许可证

本项目基于 [MIT License](LICENSE) 开源。
