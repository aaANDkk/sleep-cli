#!/usr/bin/env python3
"""
sleep-cli - The Geek's Ultimate Sleep & Focus Companion.
Designed for developers who master the Sleep() function.
"""

import argparse
import sys
import time
from datetime import datetime, timedelta

CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
MAGENTA = "\033[95m"
BOLD = "\033[1m"
RESET = "\033[0m"

BANNER = f"""{CYAN}
  ____  _                      ____ _     ___ 
 / ___|| | ___  ___ _ __      / ___| |   |_ _|
 \\___ \\| |/ _ \\/ _ \\ '_ \\ ___| |   | |    | | 
  ___) | |  __/  __/ |_) |___| |___| |___ | | 
 |____/|_|\\___|\\___| .__/     \\____|_____|___|
                   |_|                        
{RESET}{YELLOW}       Mastering the Sleep() API since Day 1{RESET}
"""

QUOTES = [
    "“There is a time for many words, and there is also a time for sleep.” — Homer",
    "“Sleep is the best meditation.” — Dalai Lama",
    "“A well-spent day brings happy sleep.” — Leonardo da Vinci",
    "“No code runs better than code running in a dream state.”",
    "“Why fix bugs today when you can sleep and dream the solution tonight?”",
]


def render_progress(current, total, width=40):
    percent = float(current) / float(total) if total > 0 else 1.0
    filled = int(width * percent)
    bar = "█" * filled + "░" * (width - filled)
    return f"[{GREEN}{bar}{RESET}] {BOLD}{percent * 100:5.1f}%{RESET}"


def parse_duration(duration_str: str) -> int:
    """Parse time string like 25m, 1h, 30s, 90m into seconds."""
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
            print(f"{RED}Error: Invalid duration format '{duration_str}'. Use e.g. 25m, 1h, 30s.{RESET}")
            sys.exit(1)


def timer_mode(seconds: int, title: str = "Sleeping"):
    print(BANNER)
    print(f"{BOLD}⏳ Target Duration:{RESET} {CYAN}{seconds // 60}m {seconds % 60}s{RESET} ({title})")
    print(f"{BOLD}🎯 Started At:{RESET} {datetime.now().strftime('%H:%M:%S')}")
    print("-" * 50)

    try:
        for elapsed in range(seconds + 1):
            remaining = seconds - elapsed
            rem_str = f"{remaining // 60:02d}:{remaining % 60:02d}"
            progress = render_progress(elapsed, seconds)
            sys.stdout.write(f"\r💤 {BOLD}{rem_str}{RESET} {progress} ")
            sys.stdout.flush()
            if elapsed < seconds:
                time.sleep(1)

        print(f"\n\n{GREEN}✨ Wake up! Sleep cycle complete. System fully refreshed! 🚀{RESET}\n")
    except KeyboardInterrupt:
        print(f"\n\n{YELLOW}⚠️ Sleep interrupted by user signal. Time to get back to work!{RESET}\n")


def cycle_calculator():
    print(BANNER)
    now = datetime.now()
    print(f"{BOLD}🧠 Sleep Cycle Calculator (90-min R.E.M Cycles){RESET}")
    print(f"Current Time: {CYAN}{now.strftime('%Y-%m-%d %H:%M:%S')}{RESET}\n")
    print("If you go to sleep RIGHT NOW, wake up at one of these times to feel refreshed:")
    print("-" * 50)

    fall_asleep = now + timedelta(minutes=15)
    for cycles in range(1, 7):
        wake_time = fall_asleep + timedelta(minutes=90 * cycles)
        hours = cycles * 1.5
        cycle_desc = f"{cycles} cycle{'s' if cycles > 1 else ''} ({hours:.1f} hrs)"
        if cycles in [5, 6]:
            rec = f"{GREEN}⭐ Recommended (Optimal rest){RESET}"
        elif cycles == 1:
            rec = f"{YELLOW}⚡ Power Nap{RESET}"
        else:
            rec = ""
        print(f" • {BOLD}{wake_time.strftime('%I:%M %p')}{RESET} ({wake_time.strftime('%H:%M')}) -> {cycle_desc} {rec}")
    print("-" * 50)


def main():
    parser = argparse.ArgumentParser(description="sleep-cli: Terminal timer and sleep cycle calculator.")
    parser.add_argument("duration", nargs="?", default="25m", help="Duration to sleep/focus (e.g. 25m, 1h, 90m, 45s).")
    parser.add_argument("-c", "--cycles", action="store_true", help="Calculate optimal sleep cycle wake-up times.")
    parser.add_argument("-q", "--quote", action="store_true", help="Display a random sleep/philosophical quote.")

    args = parser.parse_args()

    if args.cycles:
        cycle_calculator()
    elif args.quote:
        import random
        print(f"\n{MAGENTA}💡 {random.choice(QUOTES)}{RESET}\n")
    else:
        seconds = parse_duration(args.duration)
        timer_mode(seconds, title="Power Sleep Mode")


if __name__ == "__main__":
    main()
