from binance.client import Client
from config import *

client = Client(
    BINANCE_API_KEY,
    BINANCE_API_SECRET
)


def get_atr(symbol):

    try:

        candles = client.futures_klines(
            symbol=symbol,
            interval=Client.KLINE_INTERVAL_15MINUTE,
            limit=ATR_LOOKBACK + 1
        )

        if len(candles) < ATR_LOOKBACK:
            return None

        true_ranges = []

        for i in range(1, len(candles)):

            high = float(candles[i][2])
            low = float(candles[i][3])
            prev_close = float(candles[i-1][4])

            tr = max(

                high - low,

                abs(high - prev_close),

                abs(low - prev_close)

            )

            true_ranges.append(tr)

        atr = sum(true_ranges[-ATR_PERIOD:]) / ATR_PERIOD

        close = float(candles[-1][4])

        atr_percent = round((atr / close) * 100, 2)

        recent_high = max(float(c[2]) for c in candles[-10:])
        recent_low = min(float(c[3]) for c in candles[-10:])

        range_percent = round(
            ((recent_high - recent_low) / close) * 100,
            2
        )

        if atr_percent <= MIN_ATR_PERCENT:

            status = "COMPRESSION"

        elif atr_percent <= MIN_ATR_PERCENT * 2:

            status = "NORMAL"

        else:

            status = "HIGH VOLATILITY"

        return {

            "atr": round(atr, 6),

            "atr_percent": atr_percent,

            "range_percent": range_percent,

            "status": status

        }

    except Exception as e:

        print(f"ATR Error ({symbol}) : {e}")

        return None


if __name__ == "__main__":

    result = get_atr("BTCUSDT")

    print("\n========== ATR TEST ==========\n")

    print(result)

    print("\n==============================")