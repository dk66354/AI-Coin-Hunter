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

        volumes = [float(candle[5]) for candle in candles]

        if len(volumes) < 20:
            return None

        last_volume = volumes[-1]
        avg_volume = sum(volumes[:-1]) / 19

        if avg_volume == 0:
            return None

        spike = round(last_volume / avg_volume, 2)

        return {
            "last_volume": last_volume,
            "average_volume": avg_volume,
            "spike": spike
        }

    except Exception as e:

        print(f"Volume Spike Error ({symbol}) : {e}")

        return None


if __name__ == "__main__":

    result = get_volume_spike("BTCUSDT")

    print(result)