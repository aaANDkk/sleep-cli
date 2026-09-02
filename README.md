# sleep-cli

一个轻量的命令行睡眠与专注倒计时工具，内置 90 分钟 R.E.M 睡眠周期计算器。

基于 Python 标准库实现，无需安装任何额外依赖。

---

## 功能介绍

- **倒计时与进度条**：支持秒 (s)、分 (m)、小时 (h) 灵活设置，终端显示字符进度与剩余时间。
- **预设模式**：内置 20 分钟快速小憩（Power Nap）与 90 分钟深度睡眠模式。
- **睡眠周期计算**：根据当前入睡时间，计算符合 90 分钟生理周期的苏醒时间点。
- **哲思语录**：内置休息与编程哲思语录。
- **零依赖**：仅依赖 Python 3 标准库，开箱即用。

---

## 使用方法

### 1. 基础倒计时

```bash
# 默认倒计时 25 分钟
python sleep_cli.py 25m

# 自定义时长（支持 s / m / h）
python sleep_cli.py 45s
python sleep_cli.py 1h
```

### 2. 快捷预设

```bash
# 20 分钟快速小憩
python sleep_cli.py --nap

# 90 分钟深度睡眠
python sleep_cli.py --deep
```

### 3. 计算最佳苏醒时间

计算从当前时间开始入睡，哪些时间点醒来能避开深睡眠期：

```bash
python sleep_cli.py --cycles
# 或简写
python sleep_cli.py -c
```

### 4. 随机语录

```bash
python sleep_cli.py --quote
# 或简写
python sleep_cli.py -q
```

---

## 参数列表

| 参数 | 简写 | 说明 | 示例 |
| --- | --- | --- | --- |
| `duration` | - | 自定义倒计时时长（默认 25m） | `python sleep_cli.py 30m` |
| `--nap` | - | 20 分钟小憩模式 | `python sleep_cli.py --nap` |
| `--deep` | - | 90 分钟深度睡眠模式 | `python sleep_cli.py --deep` |
| `--cycles` | `-c` | 计算当前入睡的最佳起床时间 | `python sleep_cli.py -c` |
| `--quote` | `-q` | 随机显示一条语录 | `python sleep_cli.py -q` |
| `--help` | `-h` | 查看帮助文档 | `python sleep_cli.py -h` |

---

## 许可证

本项目基于 [MIT License](LICENSE) 开源。
