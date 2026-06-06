import os
import requests
from datetime import datetime

BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN', '')
CHAT_ID   = os.environ.get('TELEGRAM_CHAT_ID', '')

CHECKS = [
    {'placement': 'Tile', 'keyword': os.environ.get('KW_TILE', '')},
    {'placement': 'پین گفتگو', 'keyword': os.environ.get('KW_PIN', '')},
]

def send_telegram(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, json={
        'chat_id': CHAT_ID,
        'text': text,
        'parse_mode': 'HTML'
    })

def main():
    now = datetime.now().strftime('%Y/%m/%d %H:%M')
    
    msg = f"⏰ <b>زمان چک Rubika رسید!</b>\n\n"
    msg += f"🕐 ساعت: <b>{now}</b>\n\n"
    
    for c in CHECKS:
        if c['keyword']:
            msg += f"📍 <b>{c['placement']}</b>\n"
            msg += f"🔍 کلیدواژه: <code>{c['keyword']}</code>\n\n"
    
    msg += "━━━━━━━━━━━━━━\n"
    msg += "📱 الان برو <b>m.rubika.ir</b> رو باز کن\n"
    msg += "📸 اسکرین‌شات بگیر و اینجا بفرست\n"
    msg += "━━━━━━━━━━━━━━\n"
    msg += "✅ یافت شد → /found\n"
    msg += "❌ یافت نشد → /notfound"
    
    send_telegram(msg)
    print(f"[{now}] Telegram message sent successfully")

if __name__ == '__main__':
    main()
