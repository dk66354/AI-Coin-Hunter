from binance.client import Client
from config import *

client = Client(
    BINANCE_API_KEY,
    BINANCE_API_SECRET
)


def get_volume_spike(symbol):

    try:

        candles = client.futures_klines(
            symbol=symbol,
            interval=Client.KLINE_INTERVAL_15MINUTE,
            limit=20
        )

        if len(candles) < 20:
            return None

        volumes = [float(candle[5]) for candle in candles]

        last_volume = volumes[-1]

        average_volume = sum(volumes[:-1]) / (len(volumes) - 1)

        if average_volume <= 0:
            return None

        spike = round(last_volume / average_volume, 2)

        # -----------------------------
        # Spike Strength
        # -----------------------------

        if spike >= EXTREME_SPIKE:
            strength = "EXTREME"

        elif spike >= STRONG_SPIKE:
            strength = "STRONG"

        elif spike >= MIN_SPIKE:
            strength = "GOOD"

        else:
            strength = "WEAK"

        return {

            "last_volume": round(last_volume, 2),

            "average_volume": round(average_volume, 2),

            "spike": spike,

            "strength": strength

        }

    except Exception as e:

        print(f"Volume Spike Error ({symbol}) : {e}")

        return None


if __name__ == "__main__":

    result = get_volume_spike("BTCUSDT")

    print("\n========== VOLUME SPIKE TEST ==========\n")

    print(result)

    print("\n=======================================\n")