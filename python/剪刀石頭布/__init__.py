import random
import os

emojis = ["✌", "👊", "🖐"]

info = "-" * 10 + "\n"
info += "請輸入:\n"
info += "\n".join([f"{i + 1}. {v}" for i, v in enumerate(emojis)])
info += "\n" + "-" * 10

while True:
    print(info)
    try:
        msg = input("請選取想要出的: ")
        os.system("cls" if os.name == "nt" else "clear")

        msg = int(msg) - 1

        if not emojis[msg] or msg < 0:
            raise ValueError

        bot_emoji = random.choice(emojis)
        emoji = emojis[msg]
        win = tie = False

        if emoji == bot_emoji:
            tie = True
        elif emoji == "✌" and bot_emoji == "👊":
            win = True
        elif emoji == "👊" and bot_emoji == "🖐":
            win = True
        elif emoji == "🖐" and bot_emoji == "✌":
            win = True
    except Exception as error:
        if isinstance(error, ValueError) or isinstance(error, IndexError):
            print("參數錯誤")
    else:
        print(f"你出了 {emoji} 我出了 {bot_emoji}")
        print("耶我贏了" if win else "平手" if tie else "我輸了...")
