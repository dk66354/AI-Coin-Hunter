# ============================================
# AI COIN HUNTER V5
# Configuration File
# ============================================

# Binance

BINANCE_API_KEY = ""
BINANCE_API_SECRET = ""

# Telegram

BOT_TOKEN = "8941575381:AAFzS-0e6Zcgz3fjOs978MqtJMU1S7UQ48s"
CHAT_ID = "5839327080"

# ============================================
# Scanner
# ============================================

SCAN_INTERVAL = 300          # 5 Minutes
TOP_RESULTS = 10

# ============================================
# Volume Filter
# ============================================

MIN_VOLUME = 30              # Million USDT
MAX_VOLUME = 250             # Million USDT

# ============================================
# Volume Spike
# ============================================

MIN_SPIKE = 1.30

STRONG_SPIKE = 2.00
EXTREME_SPIKE = 3.00

# ============================================
# Open Interest
# ============================================

MIN_OI_CHANGE = 3.0

STRONG_OI = 5.0
EXTREME_OI = 10.0

# ============================================
# Breakout
# ============================================

BREAKOUT_DISTANCE = 0.80     # %

# ============================================
# ATR Filter
# ============================================

ATR_PERIOD = 14
MIN_ATR_PERCENT = 2.5

# ============================================
# Alert Rules
# ============================================

ALERT_MIN_SCORE = 45

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