# 導入
import random
import os

emojis = ["✌", "👊", "🖐"]

info = "-" * 10 + "\n"
info += "請輸入:\n"
info += "\n".join([f"{i + 1}. {v}" for i, v in enumerate(emojis)])
info += "\n" + "-" * 10

while True:  # 重複執行
    print(info)
    try:
        msg = input("請選取想要出的: ")  # 建立/更新變數 值為我們在命令中打的值
        os.system("cls" if os.name == "nt" else "clear")  # 執行清除指令

        msgIndex = int(msg) - 1  # 由於 list 的 index 為從0開始計，所以我們進行 `-1` 的動作

        if not emojis[msgIndex] or msgIndex < 0:  # 確認是否輸入正確，若錯誤將觸發一個 ValueError
            raise ValueError  # 生成一 ValueError 錯誤

        bot_emoji = random.choice(emojis)  # 使用 random 中的 choice 函數，從 emojis 中隨機抓出一值
        emoji = emojis[msgIndex]  # 將用戶輸入的轉為 emoji( 方便觀察 )
        win = tie = False  # 創建/更新變數

        if emoji == bot_emoji:  # 如果相同 設變數 tie = True
            tie = True
        elif emoji == "✌" and bot_emoji == "👊":  # 如果相同 設變數 win = True
            win = True
        elif emoji == "👊" and bot_emoji == "🖐":  # 如果相同 設變數 win = True
            win = True
        elif emoji == "🖐" and bot_emoji == "✌":  # 如果相同 設變數 win = True
            win = True
    except Exception as error:  # 抓取剛剛生成的錯誤
        if isinstance(error, ValueError) or isinstance(error, IndexError):
            print("參數錯誤")
    else:  # 如果沒有出錯
        print(f"你出了 {emoji} 我出了 {bot_emoji}")
        print("耶我贏了" if win else "平手" if tie else "我輸了...")
