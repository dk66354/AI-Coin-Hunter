import time

from config import *
from scanner import get_filtered_coins
from volume_expansion import get_volume_expansion
from oi import get_open_interest
from breakout import check_breakout
from atr import get_atr
from trend import get_trend
from score_v6 import calculate_score_v6
from ranking_engine import get_rank
from expected_move import get_expected_move
from confidence_engine import get_confidence
from risk_engine import get_risk
from telegram_alert import send_alert


def print_header():

    print("\n" + "=" * 100)
    print("                     AI COIN HUNTER V6.0")
    print("=" * 100)


def run_scanner():

    coins = get_filtered_coins()

    final_results = []

    for coin in coins:

        symbol = coin["symbol"]

        # -----------------------------
        # Volume Spike
        # -----------------------------

        volume_data = get_volume_expansion(symbol)

        if volume_data is None:
            continue
        # ----------------------------------------
        # V6 Volume Filter
        # ----------------------------------------

        if volume_data["expansion"] < MIN_VOLUME_EXPANSION:
            continue

        # -----------------------------
        # Open Interest
        # -----------------------------

        oi_data = get_open_interest(symbol)

        if oi_data is None:
            continue

        current_oi = oi_data["current_oi"]
        oi_change = oi_data["oi_change"]
        oi_strength = oi_data["strength"]
        # ----------------------------------------
        # V6 OI Filter
        # ----------------------------------------

        if oi_change < MIN_OI_CHANGE:
            continue

        # -----------------------------
        # Breakout
        # -----------------------------

        breakout_data = check_breakout(symbol)

        if breakout_data is None:
            continue
        # -----------------------------
        # ATR
        # -----------------------------

        atr_data = get_atr(symbol)

        if atr_data is None:
            continue

        # -----------------------------
        # Trend
        # -----------------------------

        trend_data = get_trend(symbol)

        if trend_data is None:
            continue
        # ----------------------------------------
        # V6 Breakout Filter
        # ----------------------------------------

        if breakout_data["status"] != "BREAKOUT READY":
            continue

        # -----------------------------
        # Score
        # -----------------------------

        score, probability, reasons = calculate_score_v6(

            volume=coin["volume"],

            volume_strength=volume_data["strength"],

            oi_change=oi_change,

            oi_strength=oi_strength,

            breakout=breakout_data["breakout"],

            atr=(atr_data["status"] == "COMPRESSION"),

            trend=trend_data["trend"] in ["BULLISH", "STRONG BULLISH"],

            liquidity=False

        )
        rank_data = get_rank(score)
        expected_move = get_expected_move(
        volume_data["strength"],
        oi_strength,
        atr_data["status"],
        trend_data["trend"]
)

        confidence = get_confidence(
        score,
        volume_data["strength"],
        oi_strength,
        breakout_data["breakout"],
        atr_data["status"],
        trend_data["trend"]
)

        risk_data = get_risk(
        volume_data["strength"],
        oi_strength,
        breakout_data["breakout"],
        atr_data["status"],
        trend_data["trend"]
)

        final_results.append({

            "symbol": symbol,

            "price": coin["price"],

            "change": coin["change"],

            "volume": coin["volume"],

            "spike": volume_data["expansion"],

            "spike_strength": volume_data["strength"],

            "oi": current_oi,

            "oi_change": oi_change,

            "oi_strength": oi_strength,

            "breakout": breakout_data["breakout"],

            "status": breakout_data["status"],

            "distance": breakout_data["distance"],

            "atr_status": atr_data["status"],

            "trend": trend_data["trend"],

            "rank": rank_data["rank"],
            "emoji": rank_data["emoji"],
            "confidence": confidence,
            "risk": risk_data["level"],
            "risk_score": risk_data["score"],
            "expected_move": expected_move,

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
            print(f"Spike Power  : {coin['spike_strength']}")
            print(f"Current OI   : {coin['oi']:.0f}")
            print(f"OI Change    : {coin['oi_change']:.2f}%")
            print(f"OI Strength  : {coin['oi_strength']}")
            print(f"Breakout     : {coin['breakout']}")
            print(f"Status       : {coin['status']}")
            print(f"Distance     : {coin['distance']}%")
            print(f"ATR Status   : {coin['atr_status']}")
            print(f"Trend        : {coin['trend']}")
            print(f"Rank         : {coin['rank']}")
            print(f"Confidence   : {coin['confidence']}%")
            print(f"Risk         : {coin['risk']}")
            print(f"Risk Score   : {coin['risk_score']}%")
            print(f"ExpectedMove : {coin['expected_move']}")

            print("\nReasons:")
            for reason in coin["reasons"]:
                print(" ", reason)

            print("-" * 100)
            
            

            # ----------------------------------------
            # TELEGRAM ALERT
            # ----------------------------------------

            if (
                coin["score"] >= ALERT_MIN_SCORE
                and coin["status"] == "BREAKOUT READY"
            ):

                message = f"""🚨 AI COIN HUNTER V6 🚨

{coin['emoji']} Rank : {coin['rank']}

Coin : {coin['symbol']}

⭐ Score : {coin['score']}/{MAX_SCORE}
🎯 Confidence : {coin['confidence']}%
📊 Probability : {coin['probability']}%

⚠️ Risk : {coin['risk']}
📉 Risk Score : {coin['risk_score']}%

📈 Expected Move : {coin['expected_move']}

💰 Price : {coin['price']}

📈 Volume : {coin['volume']:.2f} M
🔥 Volume Expansion : {coin['spike']:.2f}x
⚡ Volume Strength : {coin['spike_strength']}

📊 OI Change : {coin['oi_change']:.2f}%
💪 OI Strength : {coin['oi_strength']}

⚡ ATR : {coin['atr_status']}
📈 Trend : {coin['trend']}

🚀 Status : {coin['status']}
📍 Distance : {coin['distance']}%

Happy Trading 🚀

🕉️🕉️ OM NAMAH SHIVAY 🕉️🕉️
"""

                send_alert(
                    coin["symbol"],
                    message
                )

            print("-" * 100)

    print(f"\nNext Scan in {SCAN_INTERVAL//60} Minutes...")
    print("=" * 100)

    time.sleep(SCAN_INTERVAL)