from config import *


def get_liquidity_score(

    above_liquidity,
    below_liquidity

):

    try:

        total = above_liquidity + below_liquidity

        if total == 0:

            return {

                "ratio": 0,

                "strength": "UNKNOWN",

                "bullish": False

            }

        ratio = round(

            above_liquidity / total,

            2

        )

        if ratio >= 0.75:

            strength = "EXTREME"

            bullish = True

        elif ratio >= 0.60:

            strength = "STRONG"

            bullish = True

        elif ratio >= 0.50:

            strength = "GOOD"

            bullish = True

        else:

            strength = "WEAK"

            bullish = False

        return {

            "ratio": ratio,

            "strength": strength,

            "bullish": bullish

        }

    except Exception as e:

        print(f"Liquidity Error : {e}")

        return None


if __name__ == "__main__":

    result = get_liquidity_score(

        above_liquidity=850000,

        below_liquidity=250000

    )

    print()

    print(result)