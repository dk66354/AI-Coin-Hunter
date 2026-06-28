from binance.client import Client
from config import *

client = Client(
    BINANCE_API_KEY,
    BINANCE_API_SECRET
)


def get_open_interest(symbol):

    try:

        current = client.futures_open_interest(
            symbol=symbol
        )

        current_oi = float(current["openInterest"])

        history = client.futures_open_interest_hist(
            symbol=symbol,
            period="5m",
            limit=2
        )

        if len(history) < 2:
            return current_oi, 0.0

        previous_oi = float(history[0]["sumOpenInterest"])

        if previous_oi == 0:
            return current_oi, 0.0

        oi_change = (
            (current_oi - previous_oi)
            / previous_oi
        ) * 100

        return current_oi, round(oi_change, 2)

    except Exception as e:

        print(f"OI Error ({symbol}) : {e}")

        return None, None


if __name__ == "__main__":

    oi, change = get_open_interest("BTCUSDT")

    print(f"Current OI : {oi}")
    print(f"OI Change  : {change}%")