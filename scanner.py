from binance.client import Client
from config import *

client = Client(
    BINANCE_API_KEY,
    BINANCE_API_SECRET
)


def get_filtered_coins():

    coins = []

    try:

        tickers = client.futures_ticker()

        for coin in tickers:

            try:

                symbol = coin["symbol"]

                # Only USDT Futures
                if not symbol.endswith("USDT"):
                    continue

                volume = float(coin["quoteVolume"]) / 1_000_000

                if volume < MIN_VOLUME:
                    continue

                if volume > MAX_VOLUME:
                    continue

                coins.append({
                    "symbol": symbol,
                    "price": float(coin["lastPrice"]),
                    "change": float(coin["priceChangePercent"]),
                    "volume": volume
                })

            except Exception:
                continue

        return coins

    except Exception as e:

        print("Scanner Error :", e)
        return []


if __name__ == "__main__":

    coins = get_filtered_coins()

    print("=" * 60)
    print(f"Coins Found : {len(coins)}")
    print("=" * 60)

    for coin in coins[:10]:
        print(
            f"{coin['symbol']} | "
            f"Price: {coin['price']} | "
            f"Change: {coin['change']}% | "
            f"Volume: {round(coin['volume'], 2)}M"
        )