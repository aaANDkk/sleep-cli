#!/usr/bin/env python3
"""
sleep-cli: 晚安与专注の小憩 · 命令行睡眠伴侣。
"""

import argparse
import sys
import time
from datetime import datetime, timedelta

CYAN = "\033[96m"
PINK = "\033[95m"
BLUE = "\033[94m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
BOLD = "\033[1m"
RESET = "\033[0m"

BANNER = f"""{CYAN}
   _____ __                 ________    ____
  / ___// /__  ___  ____   / ____/ /   /  _/
  \\__ \\/ / _ \\/ _ \\/ __ \\ / /   / /    / /  
 ___/ / /  __/  __/ /_/ // /___/ /____/ /   
/____/_/\\___/\\___/ .___/ \\____/_____/___/   
                /_/                         
{RESET}{PINK}       「 晚安与专注の小憩 · 睡眠倒计时 」{RESET}
"""

QUOTES = [
    "“无论身处何处，只要睡个好觉，世界就会重新变得温柔。” —— 村上春树",
    "“今夜月色真美，请安心入眠。” —— 夏目漱石",
    "“把烦恼留在今天，向努力了一整天的自己说一声：お疲れ様（辛苦了）。”",
    "“在微风与被窝的缝隙里，藏着今天最后的安宁。”",
    "“没有哪段代码值得你透支夜晚，今夜的好眠才是明天的灵感。”",
    "“闭上眼睛，让疲惫的思绪在梦境里慢慢沉淀。”",
]


def render_progress(current, total, width=30):
    percent = float(current) / float(total) if total > 0 else 1.0
    filled = int(width * percent)
    bar = "=" * filled + ">" * (1 if filled < width else 0) + " " * (width - filled - (1 if filled < width else 0))
    return f"[{CYAN}{bar}{RESET}] {BOLD}{percent * 100:5.1f}%{RESET}"


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
            print(f"{RED}提示: 无效的时间格式 '{duration_str}'。可使用示例: 25m, 1h, 30s。{RESET}")
            sys.exit(1)


def timer_mode(seconds: int, title: str = "小憩の时间"):
    print(BANNER)
    mins = seconds // 60
    secs = seconds % 60
    dur_text = f"{mins} 分 {secs} 秒" if secs > 0 else f"{mins} 分钟"
    print(f"{BOLD}当前模式:{RESET} {PINK}{title}{RESET}")
    print(f"{BOLD}计划时长:{RESET} {CYAN}{dur_text}{RESET}")
    print(f"{BOLD}开始时刻:{RESET} {datetime.now().strftime('%H:%M:%S')}")
    print("-" * 48)

    try:
        for elapsed in range(seconds + 1):
            remaining = seconds - elapsed
            rem_str = f"{remaining // 60:02d}:{remaining % 60:02d}"
            progress = render_progress(elapsed, seconds)
            sys.stdout.write(f"\r[ 计时中 ] {BOLD}{rem_str}{RESET} {progress} ")
            sys.stdout.flush()
            if elapsed < seconds:
                time.sleep(1)

        print(f"\n\n{GREEN}叮—— 时钟归零。小憩结束，愿你带着轻盈的心情继续出发。{RESET}\n")
    except KeyboardInterrupt:
        print(f"\n\n{YELLOW}倒计时已暂停，提前苏醒，辛苦了！{RESET}\n")


def cycle_calculator():
    print(BANNER)
    now = datetime.now()
    print(f"{BOLD}睡眠周期の推算（基于 90 分钟 R.E.M 生理律动）{RESET}")
    print(f"当前时刻: {CYAN}{now.strftime('%Y-%m-%d %H:%M:%S')}{RESET}\n")
    print("若在此时入眠（预留 15 分钟自然入睡），推荐在以下时刻醒来：")
    print("-" * 52)

    fall_asleep = now + timedelta(minutes=15)
    for cycles in range(1, 7):
        wake_time = fall_asleep + timedelta(minutes=90 * cycles)
        hours = cycles * 1.5
        cycle_desc = f"{cycles} 个周期 ({hours:.1f} 小时)"
        if cycles in [5, 6]:
            rec = f"{PINK}[ 黄金深眠 · 推荐 ]{RESET}"
        elif cycles == 1:
            rec = f"{YELLOW}[ 浅睡小憩 · 快速恢复 ]{RESET}"
        else:
            rec = ""
        print(f" • {BOLD}{wake_time.strftime('%H:%M')}{RESET} ({wake_time.strftime('%I:%M %p')}) -> {cycle_desc} {rec}")
    print("-" * 52)


def main():
    parser = argparse.ArgumentParser(
        description="sleep-cli: 晚安与专注の小憩 · 命令行睡眠伴侣",
        add_help=False
    )
    parser.add_argument("duration", nargs="?", default="25m", help="倒计时时长（如 25m, 1h, 90m, 45s，默认 25m）")
    parser.add_argument("--nap", action="store_true", help="开启 20 分钟浅睡小憩模式")
    parser.add_argument("--deep", action="store_true", help="开启 90 分钟深眠物语模式")
    parser.add_argument("-c", "--cycles", action="store_true", help="推算当前入眠的最佳苏醒时间（90分钟周期）")
    parser.add_argument("-q", "--quote", action="store_true", help="抽取一句温暖の随想寄语")
    parser.add_argument("-h", "--help", action="store_true", help="查看使用案内并退出")

    args = parser.parse_args()

    if args.help:
        print(BANNER)
        print("使用案内:")
        print("  python sleep_cli.py [时长]         开启指定时长的倒计时（如 25m, 1h, 45s）")
        print("  python sleep_cli.py --nap          浅睡小憩 · 开启 20 分钟快速充电")
        print("  python sleep_cli.py --deep         深眠物语 · 开启 90 分钟完整周期")
        print("  python sleep_cli.py -c, --cycles   智能推算当前入眠的最佳苏醒时刻")
        print("  python sleep_cli.py -q, --quote    抽取一句温暖の随想寄语")
        print("  python sleep_cli.py -h, --help     查看使用案内")
        print()
    elif args.cycles:
        cycle_calculator()
    elif args.quote:
        import random
        print(f"\n{PINK}{random.choice(QUOTES)}{RESET}\n")
    elif args.nap:
        timer_mode(20 * 60, title="浅睡小憩の20分")
    elif args.deep:
        timer_mode(90 * 60, title="深眠物语の90分")
    else:
        seconds = parse_duration(args.duration)
        timer_mode(seconds, title="专注与小憩の时间")


if __name__ == "__main__":
    main()
