# ============================================
# AI COIN HUNTER V6
# Ranking Engine
# ============================================

def get_rank(score):

    if score >= 90:
        return {
            "rank": "S+",
            "emoji": "🏆",
            "confidence": 95,
            "risk": "VERY LOW"
        }

    elif score >= 80:
        return {
            "rank": "S",
            "emoji": "🥇",
            "confidence": 90,
            "risk": "LOW"
        }

    elif score >= 70:
        return {
            "rank": "A",
            "emoji": "🥈",
            "confidence": 82,
            "risk": "LOW"
        }

    elif score >= 60:
        return {
            "rank": "B",
            "emoji": "🥉",
            "confidence": 72,
            "risk": "MEDIUM"
        }

    elif score >= 50:
        return {
            "rank": "C",
            "emoji": "⭐",
            "confidence": 60,
            "risk": "HIGH"
        }

    else:
        return {
            "rank": "D",
            "emoji": "⚠️",
            "confidence": 45,
            "risk": "VERY HIGH"
        }


if __name__ == "__main__":

    print("\n========== RANKING ENGINE TEST ==========\n")

    result = get_rank(86)

    print(result)

    print("\n=========================================\n")