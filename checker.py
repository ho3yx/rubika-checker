import os
import requests
from datetime import datetime
from playwright.sync_api import sync_playwright

BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN', '')
CHAT_ID   = os.environ.get('TELEGRAM_CHAT_ID', '')

def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, json={'chat_id': CHAT_ID, 'text': text, 'parse_mode': 'HTML'})

def send_photo(photo_path, caption):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
    with open(photo_path, 'rb') as f:
        requests.post(url, data={'chat_id': CHAT_ID, 'caption': caption, 'parse_mode': 'HTML'}, files={'photo': f})

def take_screenshot(url, output_path, scroll_y=0):
    with sync_playwright() as p:
        browser = p.chromium.launch(args=['--no-sandbox', '--disable-setuid-sandbox'])
        context = browser.new_context(
            viewport={'width': 390, 'height': 844},
            user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1'
        )
        page = context.new_page()
        page.goto(url, wait_until='networkidle', timeout=30000)
        page.wait_for_timeout(5000)
        if scroll_y > 0:
            page.evaluate(f'window.scrollTo(0, {scroll_y})')
            page.wait_for_timeout(2000)
        page.screenshot(path=output_path)
        browser.close()

def main():
    now = datetime.now()
    time_str = now.strftime('%Y/%m/%d %H:%M')

    send_message(f"⏰ <b>چک Rubika شروع شد</b>\n🕐 ساعت: <b>{time_str}</b>\n📸 در حال گرفتن اسکرین‌شات...")

    try:
        take_screenshot('https://m.rubika.ir', '/tmp/tile.jpg', scroll_y=400)
        send_photo('/tmp/tile.jpg', f"🔲 <b>جایگاه Tile</b>\n🕐 {time_str}\n\nآگهیت هست؟")

        take_screenshot('https://m.rubika.ir', '/tmp/pin.jpg', scroll_y=0)
        send_photo('/tmp/pin.jpg', f"📌 <b>جایگاه پین گفتگو</b>\n🕐 {time_str}\n\nآگهیت هست؟")

    except Exception as e:
        send_message(f"❌ خطا:\n<code>{str(e)}</code>")

if __name__ == '__main__':
    main()
