# ============================================
# AI COIN HUNTER V6
# Expected Move Engine
# ============================================

def get_expected_move(
    volume_strength,
    oi_strength,
    atr_status,
    trend
):

    score = 0

    # Volume
    if volume_strength == "EXTREME":
        score += 3
    elif volume_strength == "STRONG":
        score += 2
    elif volume_strength == "GOOD":
        score += 1

    # OI
    if oi_strength == "EXTREME":
        score += 3
    elif oi_strength == "STRONG":
        score += 2
    elif oi_strength == "GOOD":
        score += 1

    # ATR
    if atr_status == "COMPRESSION":
        score += 2

    # Trend
    if trend == "STRONG BULLISH":
        score += 2
    elif trend == "BULLISH":
        score += 1

    # Expected Move
    if score >= 9:
        return "12–18%"
    elif score >= 7:
        return "8–12%"
    elif score >= 5:
        return "5–8%"
    elif score >= 3:
        return "3–5%"
    else:
        return "1–3%"


if __name__ == "__main__":

    print(
        get_expected_move(
            "STRONG",
            "EXTREME",
            "COMPRESSION",
            "STRONG BULLISH"
        )
    )