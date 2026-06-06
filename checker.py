import os
import requests
from datetime import datetime, timedelta

BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN', '')
CHAT_ID   = os.environ.get('TELEGRAM_CHAT_ID', '')

def send(text):
    requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        json={'chat_id': CHAT_ID, 'text': text, 'parse_mode': 'HTML'})

def main():
    iran = datetime.utcnow() + timedelta(hours=3, minutes=30)
    time_str = iran.strftime('%H:%M')
    date_str = iran.strftime('%Y/%m/%d')

    send(f"""⏰ <b>زمان چک Rubika!</b>

📅 {date_str} — 🕐 {time_str}

📱 برو <b>m.rubika.ir</b> رو باز کن:
🔲 بنر Tile رو چک کن
📌 پین گفتگو رو چک کن

📸 اسکرین‌شات بگیر""")
    print("Sent!")

if __name__ == '__main__':
    main()
