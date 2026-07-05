from binance.client import Client
from config import *

client = Client(
    BINANCE_API_KEY,
    BINANCE_API_SECRET
)


def get_volume_expansion(symbol):

    try:

        candles = client.futures_klines(
            symbol=symbol,
            interval=Client.KLINE_INTERVAL_15MINUTE,
            limit=VOLUME_LOOKBACK + 1
        )

        if len(candles) < VOLUME_LOOKBACK + 1:
            return None

        volumes = [float(candle[5]) for candle in candles]

        current_volume = volumes[-1]

        average_volume = sum(volumes[:-1]) / len(volumes[:-1])

        if average_volume <= 0:
            return None

        expansion = round(current_volume / average_volume, 2)

        # ============================================
        # Volume Expansion Strength
        # ============================================

        if expansion >= 3.0:

            strength = "EXTREME"

        elif expansion >= 2.0:

            strength = "STRONG"

        elif expansion >= 1.30:

            strength = "GOOD"

        else:

            strength = "WEAK"

        return {

            "current_volume": round(current_volume, 2),

            "average_volume": round(average_volume, 2),

            "expansion": expansion,

            "strength": strength

        }

    except Exception as e:

        print(f"Volume Expansion Error ({symbol}) : {e}")

        return None


if __name__ == "__main__":

    result = get_volume_expansion("BTCUSDT")

    print("\n========== VOLUME EXPANSION TEST ==========\n")

    print(result)

    print("\n==========================================\n")