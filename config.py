# ============================================
# AI COIN HUNTER V6
# Configuration File
# ============================================

# ============================================
# Binance
# ============================================

BINANCE_API_KEY = ""
BINANCE_API_SECRET = ""

# ============================================
# Telegram
# ============================================

BOT_TOKEN = "8941575381:AAFzS-0e6Zcgz3fjOs978MqtJMU1S7UQ48s"
CHAT_ID = "5839327080"

# ============================================
# Scanner
# ============================================

SCAN_INTERVAL = 600          # Seconds
TOP_RESULTS = 10

# ============================================
# Volume Filter
# ============================================

MIN_VOLUME = 5                # Million USDT
MAX_VOLUME = 5000             # Million USDT

# ============================================
# Volume Expansion (V6)
# ============================================

VOLUME_LOOKBACK = 20

MIN_VOLUME_EXPANSION = 1.10
STRONG_VOLUME_EXPANSION = 1.80
EXTREME_VOLUME_EXPANSION = 3.00

# ============================================
# Open Interest (V5 Compatibility)
# ============================================

MIN_OI_CHANGE = 0.5
STRONG_OI = 3.0
EXTREME_OI = 6.0

# ============================================
# Open Interest Expansion (V6)
# ============================================

MIN_OI_EXPANSION = 1.50
STRONG_OI_EXPANSION = 4.0
EXTREME_OI_EXPANSION = 8.0

# ============================================
# Breakout
# ============================================

BREAKOUT_DISTANCE = 2.50
MAX_BREAKOUT_DISTANCE = 2.50

# ============================================
# ATR
# ============================================

ATR_PERIOD = 14
ATR_LOOKBACK = 20

MIN_ATR_PERCENT = 4.0
# ============================================
# EMA Trend
# ============================================

EMA_FAST = 20
EMA_MID = 50
EMA_SLOW = 200

# ============================================
# Alert Rules
# ============================================

ALERT_MIN_SCORE = 40
FINAL_ALERT_SCORE = 70

# ============================================
# Scoring
# ============================================

VOLUME_SCORE = 10
SPIKE_SCORE = 15
OI_SCORE = 20
BREAKOUT_SCORE = 20
FUNDING_SCORE = 15
TREND_SCORE = 10
VOLATILITY_SCORE = 10

MAX_SCORE = (
    VOLUME_SCORE
    + SPIKE_SCORE
    + OI_SCORE
    + BREAKOUT_SCORE
    + FUNDING_SCORE
    + TREND_SCORE
    + VOLATILITY_SCORE
)