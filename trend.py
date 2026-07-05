from binance.client import Client
from config import *

client = Client(
    BINANCE_API_KEY,
    BINANCE_API_SECRET
)


def ema(values, period):

    multiplier = 2 / (period + 1)

    ema_value = sum(values[:period]) / period

    for price in values[period:]:

        ema_value = (price - ema_value) * multiplier + ema_value

    return ema_value


def get_trend(symbol):

    try:

        candles = client.futures_klines(

            symbol=symbol,

            interval=Client.KLINE_INTERVAL_15MINUTE,

            limit=EMA_SLOW + 20

        )

        closes = [float(c[4]) for c in candles]

        ema20 = ema(closes, EMA_FAST)
        ema50 = ema(closes, EMA_MID)
        ema200 = ema(closes, EMA_SLOW)

        current = closes[-1]

        if current > ema20 > ema50 > ema200:

            trend = "STRONG BULLISH"

        elif current > ema20 > ema50:

            trend = "BULLISH"

        elif current < ema20 < ema50 < ema200:

            trend = "STRONG BEARISH"

        elif current < ema20 < ema50:

            trend = "BEARISH"

        else:

            trend = "SIDEWAYS"

        return {

            "price": round(current, 6),

            "ema20": round(ema20, 6),

            "ema50": round(ema50, 6),

            "ema200": round(ema200, 6),

            "trend": trend

        }

    except Exception as e:

        print(f"Trend Error ({symbol}) : {e}")

        return None


if __name__ == "__main__":

    result = get_trend("BTCUSDT")

    print()

    print(result)