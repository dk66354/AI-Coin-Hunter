import time

from scanner import get_filtered_coins
from volume_spike import get_volume_spike
from oi import get_open_interest
from score import calculate_score

SCAN_INTERVAL = 300
TOP_RESULTS = 10


def print_header():
    print("\n" + "=" * 100)
    print("                 AI COIN HUNTER V2.0")
    print("=" * 100)


def run_scanner():

    coins = get_filtered_coins()

    final_results = []

    for coin in coins:

        symbol = coin["symbol"]

        spike_data = get_volume_spike(symbol)

        if spike_data is None:
            continue

        # Ignore weak volume spikes
        if spike_data["spike"] < 1.1:
            continue

        current_oi, oi_change = get_open_interest(symbol)

        if current_oi is None:
            continue

        # Ignore coins with negative OI Change
        

        score, reasons = calculate_score(
            coin["volume"],
            spike_data["spike"],
            oi_change
        )

        final_results.append({
            "symbol": symbol,
            "price": coin["price"],
            "change": coin["change"],
            "volume": coin["volume"],
            "spike": spike_data["spike"],
            "oi": current_oi,
            "oi_change": oi_change,
            "score": score,
            "reasons": reasons
        })

        final_results.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return final_results
while True:

    print_header()

    results = run_scanner()

    if len(results) == 0:

        print("\nNo Coins Found\n")

    else:

        print(f"\nTop {TOP_RESULTS} Momentum Coins\n")

        print("-" * 100)

        rank = 1

        for coin in results[:TOP_RESULTS]:

            print(f"\n#{rank}  {coin['symbol']}")

            print(f"Score      : {coin['score']}/55")
            print(f"Price      : {coin['price']}")
            print(f"24h Change : {coin['change']:.2f}%")
            print(f"Volume     : {coin['volume']:.2f} M")
            print(f"Spike      : {coin['spike']}x")
            print(f"Current OI : {coin['oi']:.0f}")
            print(f"OI Change  : {coin['oi_change']:.2f}%")

            print("\nReasons")

            for reason in coin["reasons"]:
                print(reason)

            print("-" * 100)

            rank += 1

    print("\nNext Scan in 5 Minutes...")
    print("=" * 100)

    time.sleep(SCAN_INTERVAL)