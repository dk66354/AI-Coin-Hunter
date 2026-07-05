import requests
from config import BOT_TOKEN, CHAT_ID

# ============================================
# AI COIN HUNTER V6
# Telegram Alert
# ============================================

_sent_alerts = set()


def send_alert(symbol, message):

    # Duplicate alert mat bhejo
    if symbol in _sent_alerts:

        print(f"⚠ Alert already sent : {symbol}")

        return False

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    payload = {

        "chat_id": CHAT_ID,

        "text": message,

        "parse_mode": "HTML",

        "disable_web_page_preview": True

    }

    try:

        response = requests.post(

            url,

            data=payload,

            timeout=15

        )

        if response.status_code == 200:

            _sent_alerts.add(symbol)

            print(f"✅ Telegram Alert Sent : {symbol}")

            return True

        print(f"❌ Telegram Failed ({response.status_code})")

        print(response.text)

        return False

    except Exception as e:

        print(f"❌ Telegram Error : {e}")

        return False


def reset_alert(symbol):

    _sent_alerts.discard(symbol)


def reset_all_alerts():

    _sent_alerts.clear()


if __name__ == "__main__":

    message = """🚨 AI COIN HUNTER V6 🚨

🥇 Rank : S

Coin : BTCUSDT

⭐ Score : 88/100
🎯 Confidence : 91%

⚠ Risk : LOW
📉 Risk Score : 28%

📈 Expected Move : 8-12%

💰 Price : 108500

📈 Volume : 125.45 M
🔥 Volume Expansion : 3.45x

📊 OI Change : 8.65%

⚡ ATR : COMPRESSION

📈 Trend : STRONG BULLISH

🚀 Status : BREAKOUT READY

Happy Trading 🚀

🕉️🕉️ OM NAMAH SHIVAY 🕉️🕉️
"""

    send_alert(

        "BTCUSDT",

        message

    )