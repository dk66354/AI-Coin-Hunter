# ============================================
# AI COIN HUNTER V6
# Risk Engine
# ============================================

def get_risk(

    volume_strength,
    oi_strength,
    breakout,
    atr_status,
    trend

):

    risk = 50

    # Volume
    if volume_strength == "EXTREME":
        risk -= 10
    elif volume_strength == "STRONG":
        risk -= 6
    elif volume_strength == "GOOD":
        risk -= 3

    # Open Interest
    if oi_strength == "EXTREME":
        risk -= 10
    elif oi_strength == "STRONG":
        risk -= 6
    elif oi_strength == "GOOD":
        risk -= 3

    # Breakout
    if breakout:
        risk -= 8

    # ATR
    if atr_status == "COMPRESSION":
        risk -= 5
    elif atr_status == "HIGH VOLATILITY":
        risk += 10

    # Trend
    if trend == "STRONG BULLISH":
        risk -= 8
    elif trend == "BULLISH":
        risk -= 4
    elif trend == "SIDEWAYS":
        risk += 5
    elif trend == "BEARISH":
        risk += 12
    elif trend == "STRONG BEARISH":
        risk += 20

    risk = max(0, min(100, risk))

    if risk <= 20:
        level = "VERY LOW"
    elif risk <= 40:
        level = "LOW"
    elif risk <= 60:
        level = "MEDIUM"
    elif risk <= 80:
        level = "HIGH"
    else:
        level = "VERY HIGH"

    return {
        "score": risk,
        "level": level
    }


if __name__ == "__main__":

    result = get_risk(
        "STRONG",
        "EXTREME",
        True,
        "COMPRESSION",
        "STRONG BULLISH"
    )

    print(result)