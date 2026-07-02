from config import *


def calculate_score(volume, spike, oi_change, breakout=False):

    score = 0
    reasons = []

    # ==========================================
    # Volume
    # ==========================================

    if MIN_VOLUME <= volume <= MAX_VOLUME:
        score += VOLUME_SCORE
        reasons.append("✅ Good Trading Volume")

    elif volume > MAX_VOLUME:
        score += 5
        reasons.append("⚠ High Trading Volume")

    # ==========================================
    # Volume Spike
    # ==========================================

    if spike >= EXTREME_SPIKE:
        score += SPIKE_SCORE
        reasons.append("🚀 EXTREME Volume Spike")

    elif spike >= STRONG_SPIKE:
        score += 12
        reasons.append("🔥 STRONG Volume Spike")

    elif spike >= MIN_SPIKE:
        score += 8
        reasons.append("✅ GOOD Volume Spike")

    else:
        reasons.append("❌ Weak Volume Spike")

    # ==========================================
    # Open Interest
    # ==========================================

    if oi_change >= EXTREME_OI:
        score += OI_SCORE
        reasons.append("🚀 EXTREME OI Build-up")

    elif oi_change >= STRONG_OI:
        score += 16
        reasons.append("🔥 STRONG OI Build-up")

    elif oi_change >= MIN_OI_CHANGE:
        score += 10
        reasons.append("✅ GOOD OI Build-up")

    else:
        reasons.append("❌ Weak OI")

    # ==========================================
    # Breakout
    # ==========================================

    if breakout:
        score += BREAKOUT_SCORE
        reasons.append("🔥 Breakout Ready")

    # ==========================================
    # Probability
    # ==========================================

    probability = min(
        round((score / MAX_SCORE) * 100),
        100
    )

    return score, probability, reasons


if __name__ == "__main__":

    score, probability, reasons = calculate_score(
        volume=85,
        spike=2.8,
        oi_change=8.6,
        breakout=True
    )

    print("\n========== SCORE TEST ==========\n")

    print("Score :", score)
    print("Probability :", probability, "%")

    print()

    for reason in reasons:
        print(reason)

    print("\n===============================\n")