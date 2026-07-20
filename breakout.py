from binance.client import Client
from config import *

client = Client(
    BINANCE_API_KEY,
    BINANCE_API_SECRET
)


def check_breakout(symbol):

    try:

        candles = client.futures_klines(
            symbol=symbol,
            interval=Client.KLINE_INTERVAL_15MINUTE,
            limit=30
        )

        highs = [float(candle[2]) for candle in candles]
        lows = [float(candle[3]) for candle in candles]

        current_price = float(candles[-1][4])

        highest = max(highs[:-1])
        lowest = min(lows[:-1])

        distance = ((highest - current_price) / highest) * 100

        if distance < 0:
            status = "ALREADY BREAKOUT"

        elif distance <= BREAKOUT_DISTANCE:
            status = "BREAKOUT READY"

        else:
            status = "RANGE"

        return {
            "breakout": distance <= BREAKOUT_DISTANCE,
            "status": status,
            "highest": highest,
            "lowest": lowest,
            "current": current_price,
            "distance": round(distance, 2)
        }

    except Exception as e:

        print(f"Breakout Error ({symbol}) : {e}")

        return None


if __name__ == "__main__":

    result = check_breakout("BTCUSDT")

    print(result)