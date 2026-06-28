import time

from config import *
from scanner import get_filtered_coins
from volume_spike import get_volume_spike
from oi import get_open_interest
from breakout import check_breakout
from score import calculate_score
from telegram_alert import send_alert


def print_header():

    print("\n" + "=" * 100)
    print("                     AI COIN HUNTER V4.0")
    print("=" * 100)


def run_scanner():

    coins = get_filtered_coins()

    final_results = []

    for coin in coins:

        symbol = coin["symbol"]

        # -----------------------------
        # Volume Spike
        # -----------------------------

        spike_data = get_volume_spike(symbol)

        if spike_data is None:
            continue

        # -----------------------------
        # Open Interest
        # -----------------------------

        current_oi, oi_change = get_open_interest(symbol)

        if current_oi is None:
            continue
        # Reject weak Open Interest

        if oi_change < 3:
            continue

        # -----------------------------
        # Breakout
        # -----------------------------

        breakout_data = check_breakout(symbol)

        if breakout_data is None:
            continue

        # -----------------------------
        # Score
        # -----------------------------

        score, probability, reasons = calculate_score(

            volume=coin["volume"],
            spike=spike_data["spike"],
            oi_change=oi_change,
            breakout=breakout_data["breakout"]

        )

        final_results.append({

            "symbol": symbol,

            "price": coin["price"],

            "change": coin["change"],

            "volume": coin["volume"],

            "spike": spike_data["spike"],

            "oi": current_oi,

            "oi_change": oi_change,

            "breakout": breakout_data["breakout"],

            "status": breakout_data["status"],

            "distance": breakout_data["distance"],

            "score": score,

            "probability": probability,

            "reasons": reasons

        })

    final_results.sort(

        key=lambda x: x["score"],

        reverse=True

    )

    return final_results

# =====================================================
# MAIN LOOP
# =====================================================

while True:

    print_header()

    results = run_scanner()

    if not results:

        print("\nNo Coins Found")
        print("=" * 100)

    else:

        print(f"\nTop {TOP_RESULTS} Momentum Coins")
        print("=" * 100)

        for i, coin in enumerate(results[:TOP_RESULTS], start=1):

            print(f"\n#{i} {coin['symbol']}")
            print(f"Score        : {coin['score']}/{MAX_SCORE}")
            print(f"Probability  : {coin['probability']}%")
            print(f"Price        : {coin['price']}")
            print(f"24h Change   : {coin['change']:.2f}%")
            print(f"Volume       : {coin['volume']:.2f} M")
            print(f"Spike        : {coin['spike']:.2f}x")
            print(f"Current OI   : {coin['oi']:.0f}")
            print(f"OI Change    : {coin['oi_change']:.2f}%")
            print(f"Breakout     : {coin['breakout']}")
            print(f"Status       : {coin['status']}")
            print(f"Distance     : {coin['distance']}%")

            print("\nReasons:")
            for reason in coin["reasons"]:
                print(" ", reason)

            # ----------------------------------------
            # TELEGRAM ALERT
            # ----------------------------------------

            if (
                coin["score"] >= ALERT_MIN_SCORE
                and coin["status"] == "BREAKOUT READY"
            ):

                message = f"""🚨 AI COIN HUNTER V4 🚨

Coin : {coin['symbol']}

⭐ Score : {coin['score']}/{MAX_SCORE}
📊 Probability : {coin['probability']}%

💰 Price : {coin['price']}
📈 Volume : {coin['volume']:.2f} M
🔥 Spike : {coin['spike']:.2f}x
📊 OI Change : {coin['oi_change']:.2f}%
🚀 Status : {coin['status']}
📍 Distance : {coin['distance']}%

Happy Trading 🚀
"""

                send_alert(
                    coin["symbol"],
                    message
                )

            print("-" * 100)

    print(f"\nNext Scan in {SCAN_INTERVAL//60} Minutes...")
    print("=" * 100)

    time.sleep(SCAN_INTERVAL)