from config import *


def calculate_score_v6(

    volume,
    volume_strength,
    oi_change,
    oi_strength,
    breakout=False,
    atr=False,
    trend=False,
    liquidity=False

):

    score = 0

    reasons = []

    # ============================================
    # Volume
    # ============================================

    if MIN_VOLUME <= volume <= MAX_VOLUME:

        score += 10

        reasons.append("✅ Good Trading Volume")

    # ============================================
    # Volume Expansion
    # ============================================

    if volume_strength == "EXTREME":

        score += 25

        reasons.append("🔥 Extreme Volume Expansion")

    elif volume_strength == "STRONG":

        score += 20

        reasons.append("🚀 Strong Volume Expansion")

    elif volume_strength == "GOOD":

        score += 10

        reasons.append("✅ Healthy Volume Expansion")

    else:

        reasons.append("❌ Weak Volume Expansion")

    # ============================================
    # Open Interest
    # ============================================

    if oi_strength == "EXTREME":

        score += 30

        reasons.append("🔥 Extreme OI Expansion")

    elif oi_strength == "STRONG":

        score += 25

        reasons.append("🚀 Strong OI Expansion")

    elif oi_strength == "GOOD":

        score += 15

        reasons.append("✅ Healthy OI Expansion")

    else:

        reasons.append("❌ Weak OI")

    # ============================================
    # Breakout
    # ============================================

    if breakout:

        score += 10

        reasons.append("🔥 Breakout Ready")

    # ============================================
    # ATR
    # ============================================

    if atr:

        score += 15

        reasons.append("⚡ ATR Compression")

    # ============================================
    # Trend
    # ============================================

    if trend:

        score += 10

        reasons.append("📈 Bullish Trend")

    # ============================================
    # Liquidity
    # ============================================

    if liquidity:

        score += 10

        reasons.append("💧 Liquidity Confirmed")

    # ============================================
    # Probability
    # ============================================

    probability = min(score, 100)

    return score, probability, reasons


if __name__ == "__main__":

    score, probability, reasons = calculate_score_v6(

        volume=80,

        volume_strength="STRONG",

        oi_change=8,

        oi_strength="STRONG",

        breakout=True,

        atr=True,

        trend=True,

        liquidity=True

    )

    print("\n========== SCORE V6 TEST ==========\n")

    print("Score :", score)

    print("Probability :", probability)

    print()

    for reason in reasons:

        print(reason)