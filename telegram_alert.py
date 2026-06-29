import requests
from config import BOT_TOKEN, CHAT_ID

# Duplicate alerts ko rokne ke liye
import time

_sent_alerts = set()

def send_alert(symbol, message):

    # Same coin ka alert dobara mat bhejo
    if symbol in _sent_alerts:
        print(f"Alert already sent for {symbol}")
        return False
    
    #print(BOT_TOKEN)
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    #print(url)

    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }

    try:

        response = requests.post(
            url,
            data=payload,
            timeout=10
        )

        

        if response.status_code == 200:

            _sent_alerts.add(symbol)

            print("Telegram Alert Sent Successfully")

            return True

        print("Telegram Alert Failed")

        return False

    except Exception as e:

        print("Telegram Error :", e)

        return False


def reset_alert(symbol):

    if symbol in _sent_alerts:
        _sent_alerts.remove(symbol)


if __name__ == "__main__":

    send_alert(

        "BTCUSDT",

        """🚨 AI COIN HUNTER V4 🚨

Coin : BTCUSDT

This is a TEST ALERT.

If you received this message,
Telegram integration is working correctly.

Happy Trading 🚀
"""
    )