#!/usr/bin/env python3
"""
sleep-cli: 猫娘の添い寝伴侣 · 晚安与专注の小憩タイマー。
"""

import argparse
import json
import os
import random
import sys
import time
import urllib.parse
import urllib.request
from datetime import datetime, timedelta

PINK = "\033[95m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
BLUE = "\033[94m"
RED = "\033[91m"
BOLD = "\033[1m"
RESET = "\033[0m"


def get_time_greeting() -> str:
    """根据当前时间返回猫娘的时段问候。"""
    hour = datetime.now().hour
    if 5 <= hour < 9:
        return "「 おはようございますにゃ！新的一天也要和猫娘一起元气满满喵〜 」"
    elif 9 <= hour < 12:
        return "「 ご主人様、上午专注工作辛苦啦，适当休息一下眼睛にゃ！ 」"
    elif 12 <= hour < 14:
        return "「 お昼休みにゃ！吃饱饭来和猫娘睡个 20 分钟小憩吧 (うたた寝) 」"
    elif 14 <= hour < 18:
        return "「 午后容易犯困にゃ… 猫娘给ご主人様泡了一杯热茶🐾 」"
    elif 18 <= hour < 22:
        return "「 お疲れ様でした！今天也辛苦啦，准备好放松心情了吗喵？ 」"
    elif 22 <= hour < 24 or 0 <= hour < 2:
        return "「 夜深了にゃ… 屏幕很伤眼睛，快来和猫娘一起钻进被窝おやすみ〜 」"
    else:
        return "「 呜哇！都这个时间了还在熬夜にゃ？！夜更かしはダメ！快睡觉！(心配) 」"


def get_banner() -> str:
    greeting = get_time_greeting()
    return f"""{PINK}
       /\\_/\\  
      ( o.o )  {CYAN}~ にゃ〜？{PINK}
       > ^ <   {BOLD}[ sleep-cli · 猫娘の安眠伴侣 ]{RESET}
{PINK}   {greeting}{RESET}
"""


OFFLINE_QUOTES = [
    "“ご主人様、今日もお疲れ様にゃ！快钻进暖暖的被窝里，猫娘帮你掖好被角〜 (おやすみ)”",
    "“今夜の月はとても綺麗にゃ… ご主人様、今晚一定能做个甜甜的梦喵。”",
    "“无论今天遇到了什么Bug，在猫猫眼里ご主人様永远都是全宇宙最厉害的ニャン！”",
    "“喵呜~ 睡不着的话，本猫娘可以把软乎乎的尾巴借你抱抱哦 (ฅ^•ﻌ•^ฅ)”",
    "“代码是敲不完的，但猫猫的呼噜声随时都有にゃ〜 晚安おやすみ！”",
    "“呼噜呼噜…（猫娘在枕边打起了呼噜）ご主人様、今晚也辛苦啦，一起睡大觉にゃ！”",
    "“疲れたら休むのが一番にゃ！累了就要好好休息，不许勉强自己喵〜”",
    "“明天的事留给明天的太阳去照耀，现在的任务是闭上眼睛安心休息だニャン！”",
    "“（小猫爪轻轻搭在你的手背上）ご主人様、安心してください，猫娘会一直陪着你的喵。”",
]


def fetch_ai_whisper(user_topic: str = "") -> str:
    """
    多层混合猫娘轻语引擎：
    1. 若配置了 OpenAI / DeepSeek / Gemini / Ollama API 则调用真实大模型生成；
    2. 否则免费调用 Hitokoto 动漫/文学名言库并由猫娘萌化演绎；
    3. 离线/超时时根据时间与情境动态合成独一无二的猫娘语录。
    """
    # 1. 尝试调用用户配置的 AI API
    api_key = os.getenv("AI_API_KEY") or os.getenv("OPENAI_API_KEY") or os.getenv("DEEPSEEK_API_KEY")
    api_base = os.getenv("AI_API_BASE", "https://api.openai.com/v1")

    if api_key:
        try:
            prompt = user_topic if user_topic else "请给主人说一句简短的治愈晚安或小憩鼓励的话"
            req_data = {
                "model": os.getenv("AI_MODEL", "gpt-3.5-turbo"),
                "messages": [
                    {
                        "role": "system",
                        "content": "你是一只陪伴在主人身边的软萌二次元猫娘。称呼用户为'ご主人様'或'主人大人'，句尾偶尔带'にゃ'或'喵~'，语气极度温柔、贴心、治愈。回复保持在40字以内，中日双语皆可。"
                    },
                    {"role": "user", "content": prompt}
                ],
                "max_tokens": 100,
                "temperature": 0.8
            }
            req = urllib.request.Request(
                f"{api_base}/chat/completions",
                data=json.dumps(req_data).encode("utf-8"),
                headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
            )
            with urllib.request.urlopen(req, timeout=3) as resp:
                res_json = json.loads(resp.read().decode("utf-8"))
                reply = res_json["choices"][0]["message"]["content"].strip()
                return f"“{reply}”"
        except Exception:
            pass

    # 2. 免费免配置：从 Hitokoto 动漫/文学库实时抓取灵感并猫娘化
    try:
        url = "https://v1.hitokoto.cn/?c=a&c=b&c=d&c=i&encode=json"
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=2) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            hitokoto = data.get("hitokoto", "").strip()
            source = data.get("from", "").strip()
            author = data.get("from_who")
            from_text = f"{author} · 《{source}》" if author else f"《{source}》"
            
            wrappers = [
                f"“ご主人様、猫娘想读这句话给你听にゃ：『{hitokoto}』—— {from_text} 晚安喵🐾”",
                f"“喵呜~ 刚刚在书本里翻到了很温柔的一句话：『{hitokoto}』—— {from_text} 祝好梦だニャン🌙”",
                f"“主人大人，今晚的星空和这句话好相配にゃ：『{hitokoto}』—— {from_text} (ฅ^･ω･^ฅ)”",
                f"“呼噜呼噜… 猫娘把今天最美的一句话送给ご主人様：『{hitokoto}』—— {from_text} ✨”",
            ]
            return random.choice(wrappers)
    except Exception:
        pass

    # 3. 离线保底：时段 + 动作程序化动态组合生成
    actions = [
        "（用毛茸茸的脑袋蹭了蹭你的手心）",
        "（轻轻摇晃着猫尾巴，趴在你身边）",
        "（为你递上一杯温热的牛奶）",
        "（悄悄帮你把滑落的毯子拉好）",
        "（在枕边发出舒服的呼噜呼噜声）",
    ]
    phrases = [
        "今天也辛苦了，世界很大，但今晚只要安心睡在猫猫身边就好にゃ。",
        "疲劳是可逆的，快乐是无限的，现在请闭上双眼好好休息喵。",
        "梦里有一整片长满小鱼干和无Bug代码的温柔森林等着ご主人様哦！",
        "无论今天过得怎么样，明天醒来又是全新的一天，猫娘一直在这里陪着你だニャン。",
    ]
    return f"“{random.choice(actions)} ご主人様、{random.choice(phrases)} おやすみなさいにゃ〜”"


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


def timer_mode(seconds: int, title: str = "小憩のじかん", bell: bool = True):
    print(get_banner())
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

        if bell:
            sys.stdout.write("\a")
            sys.stdout.flush()

        print(f"\n\n{GREEN}叮咚—— ⏰ 时间到了にゃ！ご主人様、起きて起きて〜 充满能量继续加油喵！(ฅ^･ω･^ฅ){RESET}\n")
    except KeyboardInterrupt:
        print(f"\n\n{YELLOW}喵！倒计时被提前唤醒了，ご主人様醒得真早にゃ〜{RESET}\n")


def cycle_calculator():
    print(get_banner())
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
    parser.add_argument("-q", "--quote", nargs="?", const="", help="听猫娘说一句温柔轻语，可传入心情/话题（如 -q '今天好累'）")
    parser.add_argument("--chat", type=str, help="和猫娘进行专属对话（如 --chat '今天写代码被Bug折磨了'）")
    parser.add_argument("-h", "--help", action="store_true", help="查看使用案内并退出にゃ")

    args = parser.parse_args()

    if args.help:
        print(get_banner())
        print("使用案内 (使い方):")
        print("  python sleep_cli.py [时长]         开启指定时长的陪睡倒计时（如 25m, 1h, 45s）")
        print("  python sleep_cli.py --nap          浅睡小憩 · 20 分钟猫猫充电 (うたた寝にゃ)")
        print("  python sleep_cli.py --deep         深眠物语 · 90 分钟完整周期 (ぐっすり夢の中)")
        print("  python sleep_cli.py -c, --cycles   智能推算最适合ご主人様的苏醒时刻喵")
        print("  python sleep_cli.py -q, --quote    抽取一句动态猫娘の温柔轻语（支持联网与AI）")
        print("  python sleep_cli.py --chat [话语]  向猫娘倾诉心事，获取专属安抚回答喵")
        print("  python sleep_cli.py -h, --help     查看本使用案内にゃ")
        print()
    elif args.cycles:
        cycle_calculator()
    elif args.chat is not None:
        print(f"\n{PINK}{fetch_ai_whisper(args.chat)}{RESET}\n")
    elif args.quote is not None:
        topic = args.quote if args.quote else ""
        print(f"\n{PINK}{fetch_ai_whisper(topic)}{RESET}\n")
    elif args.nap:
        timer_mode(20 * 60, title="浅睡小憩の20分 · うたた寝にゃ🐾")
    elif args.deep:
        timer_mode(90 * 60, title="深眠物语の90分 · ぐっすり夢の中にゃ🌙")
    else:
        seconds = parse_duration(args.duration)
        timer_mode(seconds, title="ご主人様と小憩のじかん🐾")


if __name__ == "__main__":
    main()
