from binance.client import Client
from config import *

client = Client(
    BINANCE_API_KEY,
    BINANCE_API_SECRET
)


def get_open_interest(symbol):

    try:

        current = client.futures_open_interest(
            symbol=symbol
        )

        current_oi = float(current["openInterest"])

        history = client.futures_open_interest_hist(
            symbol=symbol,
            period="5m",
            limit=2
        )

        if len(history) < 2:
            return None

        previous_oi = float(history[0]["sumOpenInterest"])

        if previous_oi <= 0:
            return None

        oi_change = (
            (current_oi - previous_oi)
            / previous_oi
        ) * 100

        oi_change = round(oi_change, 2)

        # ---------------------------------
        # OI Strength
        # ---------------------------------

        if oi_change >= EXTREME_OI:
            strength = "EXTREME"

        elif oi_change >= STRONG_OI:
            strength = "STRONG"

        elif oi_change >= MIN_OI_CHANGE:
            strength = "GOOD"

        else:
            strength = "WEAK"

        return {

            "current_oi": round(current_oi, 2),

            "previous_oi": round(previous_oi, 2),

            "oi_change": oi_change,

            "strength": strength

        }

    except Exception as e:

        print(f"OI Error ({symbol}) : {e}")

        return None


if __name__ == "__main__":

    result = get_open_interest("BTCUSDT")

    print("\n========== OPEN INTEREST TEST ==========\n")

    print(result)

    print("\n========================================\n")