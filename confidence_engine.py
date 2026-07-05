# ============================================
# AI COIN HUNTER V6
# Confidence Engine
# ============================================

def get_confidence(

    score,
    volume_strength,
    oi_strength,
    breakout,
    atr,
    trend

):

    confidence = score

    # ============================================
    # Volume
    # ============================================

    if volume_strength == "EXTREME":
        confidence += 8

    elif volume_strength == "STRONG":
        confidence += 5

    elif volume_strength == "GOOD":
        confidence += 2

    # ============================================
    # Open Interest
    # ============================================

    if oi_strength == "EXTREME":
        confidence += 8

    elif oi_strength == "STRONG":
        confidence += 5

    elif oi_strength == "GOOD":
        confidence += 2

    # ============================================
    # Breakout
    # ============================================

    if breakout:
        confidence += 8

    # ============================================
    # ATR
    # ============================================

    if atr == "COMPRESSION":
        confidence += 5

    # ============================================
    # Trend
    # ============================================

    if trend == "STRONG BULLISH":
        confidence += 8

    elif trend == "BULLISH":
        confidence += 5

    elif trend == "SIDEWAYS":
        confidence -= 5

    elif trend == "BEARISH":
        confidence -= 10

    elif trend == "STRONG BEARISH":
        confidence -= 15

    # ============================================
    # Limit
    # ============================================

    confidence = max(0, min(100, confidence))

    return round(confidence)


if __name__ == "__main__":

    confidence = get_confidence(

        score=78,

        volume_strength="STRONG",

        oi_strength="EXTREME",

        breakout=True,

        atr="COMPRESSION",

        trend="STRONG BULLISH"

    )

    print()

    print(f"Confidence : {confidence}%")