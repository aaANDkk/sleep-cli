#!/usr/bin/env python3
"""
sleep-cli: 猫娘の添い寝伴侣 · 晚安与专注の小憩タイマー。
"""

import argparse
import random
import sys
import time
from datetime import datetime, timedelta

PINK = "\033[95m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
BLUE = "\033[94m"
RED = "\033[91m"
BOLD = "\033[1m"
RESET = "\033[0m"

BANNER = f"""{PINK}
       /\\_/\\  
      ( o.o )  {CYAN}~ にゃ〜？{PINK}
       > ^ <   {BOLD}[ sleep-cli · 猫娘の安眠伴侣 ]{RESET}
{PINK}   「 ご主人様、今日も一日お疲れ様でしたにゃ！ 」{RESET}
"""

QUOTES = [
    "“ご主人様、今日もお疲れ様にゃ！早くお布団に入るにゃ〜（主人大人，今天也辛苦啦，快钻进暖暖的被窝喵~）”",
    "“今夜の月はとても綺麗にゃ… ご主人様、いい夢を見てにゃ。（今晚月色真美喵… 要做个好梦哦）”",
    "“无论今天遇到了什么Bug，在猫猫眼里ご主人様都是全宇宙最厉害的ニャン！”",
    "“喵呜~ 睡不着的话，本猫娘可以把软乎乎的尾巴借你抱抱哦 (ฅ^•ﻌ•^ฅ)”",
    "“代码是敲不完的，但猫猫的呼噜声随时都有にゃ〜 晚安おやすみ！”",
    "“呼噜呼噜…（猫娘在枕边打起了呼噜）ご主人様、一緒におやすみにゃ！”",
    "“疲れたら休むのが一番にゃ！無理しちゃダメだニャン（累了就要好好休息喵！不许勉强自己喵~）”",
]


def render_progress(current, total, width=28):
    percent = float(current) / float(total) if total > 0 else 1.0
    filled = int(width * percent)
    bar = "=" * filled + ">" * (1 if filled < width else 0) + " " * (width - filled - (1 if filled < width else 0))
    cat_face = "(^･ω･^)" if current < total else "(=^-ω-^=)"
    return f"[{PINK}{bar}{RESET}] {BOLD}{percent * 100:5.1f}%{RESET} {CYAN}{cat_face}{RESET}"


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
            print(f"{RED}喵？无效的时间格式 '{duration_str}' にゃ！支持格式如: 25m, 1h, 30s。{RESET}")
            sys.exit(1)


def timer_mode(seconds: int, title: str = "小憩のじかん"):
    print(BANNER)
    mins = seconds // 60
    secs = seconds % 60
    dur_text = f"{mins} 分 {secs} 秒" if secs > 0 else f"{mins} 分钟"
    print(f"{BOLD}当前模式:{RESET} {PINK}{title}{RESET}")
    print(f"{BOLD}陪睡时长:{RESET} {CYAN}{dur_text}{RESET}")
    print(f"{BOLD}开始时刻:{RESET} {datetime.now().strftime('%H:%M:%S')}")
    print(f"{YELLOW}猫娘提示:{RESET} 闭上眼睛，猫娘会在旁边守着ご主人様にゃ〜")
    print("-" * 52)

    try:
        for elapsed in range(seconds + 1):
            remaining = seconds - elapsed
            rem_str = f"{remaining // 60:02d}:{remaining % 60:02d}"
            progress = render_progress(elapsed, seconds)
            sys.stdout.write(f"\r[ 睡眠中🐾 ] {BOLD}{rem_str}{RESET} {progress} ")
            sys.stdout.flush()
            if elapsed < seconds:
                time.sleep(1)

        print(f"\n\n{GREEN}叮咚—— ⏰ 时间到了にゃ！ご主人様、起きて起きて〜 充满能量继续加油喵！(ฅ^･ω･^ฅ){RESET}\n")
    except KeyboardInterrupt:
        print(f"\n\n{YELLOW}喵！倒计时被提前唤醒了，ご主人様醒得真早にゃ〜{RESET}\n")


def cycle_calculator():
    print(BANNER)
    now = datetime.now()
    print(f"{BOLD}睡眠周期の推算 · にゃんこ計算機（90 分钟 R.E.M 律动）{RESET}")
    print(f"当前时刻: {CYAN}{now.strftime('%Y-%m-%d %H:%M:%S')}{RESET}\n")
    print("如果现在和猫娘一起入睡（预留 15 分钟入眠），推荐在以下时刻醒来喵：")
    print("-" * 56)

    fall_asleep = now + timedelta(minutes=15)
    for cycles in range(1, 7):
        wake_time = fall_asleep + timedelta(minutes=90 * cycles)
        hours = cycles * 1.5
        cycle_desc = f"{cycles} 个周期 ({hours:.1f} 小时)"
        if cycles in [5, 6]:
            rec = f"{PINK}[ 黄金深眠 · 大推荐にゃ ✨ ]{RESET}"
        elif cycles == 1:
            rec = f"{YELLOW}[ 浅睡小憩 · 猫猫充电 🐾 ]{RESET}"
        else:
            rec = f"{CYAN}[ 自然醒 💤 ]{RESET}"
        print(f" • {BOLD}{wake_time.strftime('%H:%M')}{RESET} ({wake_time.strftime('%I:%M %p')}) -> {cycle_desc} {rec}")
    print("-" * 56)


def main():
    parser = argparse.ArgumentParser(
        description="sleep-cli: 猫娘の添い寝伴侣 · 命令行睡眠与小憩タイマー",
        add_help=False
    )
    parser.add_argument("duration", nargs="?", default="25m", help="倒计时时长（如 25m, 1h, 90m, 45s，默认 25m）")
    parser.add_argument("--nap", action="store_true", help="开启 20 分钟猫猫浅睡小憩（うたた寝にゃ）")
    parser.add_argument("--deep", action="store_true", help="开启 90 分钟猫娘深眠物语（ぐっすり夢の中）")
    parser.add_argument("-c", "--cycles", action="store_true", help="推算适合ご主人様的最佳苏醒时刻（にゃんこ計算）")
    parser.add_argument("-q", "--quote", action="store_true", help="听猫娘说一句甜甜の温柔轻语（猫娘の囁き）")
    parser.add_argument("-h", "--help", action="store_true", help="查看使用案内并退出にゃ")

    args = parser.parse_args()

    if args.help:
        print(BANNER)
        print("使用案内 (使い方):")
        print("  python sleep_cli.py [时长]         开启指定时长的陪睡倒计时（如 25m, 1h, 45s）")
        print("  python sleep_cli.py --nap          浅睡小憩 · 20 分钟猫猫充电 (うたた寝にゃ)")
        print("  python sleep_cli.py --deep         深眠物语 · 90 分钟完整周期 (ぐっすり夢の中)")
        print("  python sleep_cli.py -c, --cycles   智能推算最适合ご主人様的苏醒时刻喵")
        print("  python sleep_cli.py -q, --quote    抽取一句猫娘の温柔轻语 (猫娘の囁き)")
        print("  python sleep_cli.py -h, --help     查看本使用案内にゃ")
        print()
    elif args.cycles:
        cycle_calculator()
    elif args.quote:
        print(f"\n{PINK}{random.choice(QUOTES)}{RESET}\n")
    elif args.nap:
        timer_mode(20 * 60, title="浅睡小憩の20分 · うたた寝にゃ🐾")
    elif args.deep:
        timer_mode(90 * 60, title="深眠物语の90分 · ぐっすり夢の中にゃ🌙")
    else:
        seconds = parse_duration(args.duration)
        timer_mode(seconds, title="ご主人様と小憩のじかん🐾")


if __name__ == "__main__":
    main()
