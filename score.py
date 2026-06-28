from config import *


def calculate_score(volume, spike, oi_change, breakout=False):

    score = 0
    reasons = []

    # -------------------------
    # Volume
    # -------------------------
    if MIN_VOLUME <= volume <= MAX_VOLUME:
        score += VOLUME_SCORE
        reasons.append("✅ Good Trading Volume")

    # -------------------------
    # Volume Spike
    # -------------------------
    if spike >= 3:
        score += SPIKE_SCORE
        reasons.append("🔥 Strong Volume Spike")

    elif spike >= 2:
        score += 10
        reasons.append("✅ Moderate Volume Spike")

    elif spike >= MIN_SPIKE:
        score += 5
        reasons.append("⚠ Small Volume Spike")

    # -------------------------
    # Open Interest
    # -------------------------
    if oi_change >= 10:
        score += OI_SCORE
        reasons.append("🚀 Strong OI Increase")

    elif oi_change >= 5:
        score += 15
        reasons.append("✅ Healthy OI Increase")

    elif oi_change > 0:
        score += 5
        reasons.append("⚠ Slight OI Increase")

    # -------------------------
    # Breakout
    # -------------------------
    if breakout:
        score += 25
        reasons.append("🔥 Breakout Ready")

    probability = round((score / MAX_SCORE) * 100)

    return score, probability, reasons


if __name__ == "__main__":

    score, probability, reasons = calculate_score(
        volume=85,
        spike=2.8,
        oi_change=8.6,
        breakout=True
    )

    print("Score :", score)
    print("Probability :", probability, "%")

    print()

    for reason in reasons:
        print(reason)