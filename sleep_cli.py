#!/usr/bin/env python3
"""
sleep-cli: 轻量级命令行睡眠与专注倒计时工具。
"""

import argparse
import sys
import time
from datetime import datetime, timedelta

CYAN = "\033[96m"
BLUE = "\033[94m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
MAGENTA = "\033[95m"
BOLD = "\033[1m"
RESET = "\033[0m"

BANNER = f"""{CYAN}
   _____ __                 ________    ____
  / ___// /__  ___  ____   / ____/ /   /  _/
  \\__ \\/ / _ \\/ _ \\/ __ \\ / /   / /    / /  
 ___/ / /  __/  __/ /_/ // /___/ /____/ /   
/____/_/\\___/\\___/ .___/ \\____/_____/___/   
                /_/                         
{RESET}{BLUE}       [ 极客终端睡眠与专注伴侣 · sleep-cli ]{RESET}
"""

QUOTES = [
    "“说话有时，睡眠有时。” —— 荷马",
    "“睡眠是最好的冥想与内存回收。” —— 达赖喇嘛",
    "“充实的一天带来香甜的睡眠。” —— 达·芬奇",
    "“没有哪行代码的效率，比得上在充分休息的大脑中构建的逻辑。”",
    "“与其深夜硬磨 Bug，不如睡上一觉，在梦里触发异常捕获。”",
    "“清空大脑缓存，给 CPU 降降温，重启系统活力。”",
]


def render_progress(current, total, width=32):
    percent = float(current) / float(total) if total > 0 else 1.0
    filled = int(width * percent)
    bar = "=" * filled + ">" * (1 if filled < width else 0) + " " * (width - filled - (1 if filled < width else 0))
    return f"[{GREEN}{bar}{RESET}] {BOLD}{percent * 100:5.1f}%{RESET}"


def parse_duration(duration_str: str) -> int:
    """解析时间字符串，如 25m, 1h, 30s, 90m 为秒数。"""
    s = duration_str.strip().lower()
    if s.endswith("s"):
        return int(s[:-1])
    elif s.endswith("m"):
        return int(s[:-1]) * 60
    elif s.endswith("h"):
        return int(s[:-1]) * 3600
    else:
        try:
            return int(s) * 60
        except ValueError:
            print(f"{RED}错误: 无效的时间格式 '{duration_str}'。支持示例: 25m, 1h, 30s。{RESET}")
            sys.exit(1)


def timer_mode(seconds: int, title: str = "小憩 / 专注"):
    print(BANNER)
    mins = seconds // 60
    secs = seconds % 60
    dur_text = f"{mins} 分 {secs} 秒" if secs > 0 else f"{mins} 分钟"
    print(f"{BOLD}当前模式:{RESET} {CYAN}{title}{RESET}")
    print(f"{BOLD}计划时长:{RESET} {CYAN}{dur_text}{RESET}")
    print(f"{BOLD}开始时间:{RESET} {datetime.now().strftime('%H:%M:%S')}")
    print("-" * 48)

    try:
        for elapsed in range(seconds + 1):
            remaining = seconds - elapsed
            rem_str = f"{remaining // 60:02d}:{remaining % 60:02d}"
            progress = render_progress(elapsed, seconds)
            sys.stdout.write(f"\r[倒计时] {BOLD}{rem_str}{RESET} {progress} ")
            sys.stdout.flush()
            if elapsed < seconds:
                time.sleep(1)

        print(f"\n\n{GREEN}时间到！睡眠周期已完成，系统已满血复活。{RESET}\n")
    except KeyboardInterrupt:
        print(f"\n\n{YELLOW}倒计时被手动中断，准备回到工作中！{RESET}\n")


def cycle_calculator():
    print(BANNER)
    now = datetime.now()
    print(f"{BOLD}睡眠周期计算器（基于 90 分钟 R.E.M 生理周期）{RESET}")
    print(f"当前时间: {CYAN}{now.strftime('%Y-%m-%d %H:%M:%S')}{RESET}\n")
    print("如果现在开始入睡（假定 15 分钟入睡），建议在以下时间点起床：")
    print("-" * 52)

    fall_asleep = now + timedelta(minutes=15)
    for cycles in range(1, 7):
        wake_time = fall_asleep + timedelta(minutes=90 * cycles)
        hours = cycles * 1.5
        cycle_desc = f"{cycles} 个周期 ({hours:.1f} 小时)"
        if cycles in [5, 6]:
            rec = f"{GREEN}[推荐黄金睡眠]{RESET}"
        elif cycles == 1:
            rec = f"{YELLOW}[快速小憩]{RESET}"
        else:
            rec = ""
        print(f" • {BOLD}{wake_time.strftime('%H:%M')}{RESET} ({wake_time.strftime('%I:%M %p')}) -> {cycle_desc} {rec}")
    print("-" * 52)


def main():
    parser = argparse.ArgumentParser(
        description="sleep-cli: 命令行睡眠与专注倒计时工具",
        add_help=False
    )
    parser.add_argument("duration", nargs="?", default="25m", help="倒计时时长（如 25m, 1h, 90m, 45s，默认 25m）")
    parser.add_argument("--nap", action="store_true", help="开启 20 分钟快速小憩模式")
    parser.add_argument("--deep", action="store_true", help="开启 90 分钟深度睡眠模式")
    parser.add_argument("-c", "--cycles", action="store_true", help="计算当前入睡的最佳起床时间（90分钟周期）")
    parser.add_argument("-q", "--quote", action="store_true", help="随机显示一条极客哲思名言")
    parser.add_argument("-h", "--help", action="store_true", help="显示此帮助信息并退出")

    args = parser.parse_args()

    if args.help:
        print(BANNER)
        print("使用说明:")
        print("  python sleep_cli.py [时长]         开启指定时长的倒计时（如 25m, 1h, 45s）")
        print("  python sleep_cli.py --nap          开启 20 分钟快速小憩")
        print("  python sleep_cli.py --deep         开启 90 分钟深度睡眠")
        print("  python sleep_cli.py -c, --cycles   智能计算当前入睡的最佳苏醒时间")
        print("  python sleep_cli.py -q, --quote    随机抽取一条哲思名言")
        print("  python sleep_cli.py -h, --help     查看帮助信息")
        print()
    elif args.cycles:
        cycle_calculator()
    elif args.quote:
        import random
        print(f"\n{MAGENTA}{random.choice(QUOTES)}{RESET}\n")
    elif args.nap:
        timer_mode(20 * 60, title="快速强力小憩 (20分钟)")
    elif args.deep:
        timer_mode(90 * 60, title="完整深度周期 (90分钟)")
    else:
        seconds = parse_duration(args.duration)
        timer_mode(seconds, title="小憩 / 专注模式")


if __name__ == "__main__":
    main()
