# ============================================
# AI COIN HUNTER V4
# Configuration File
# ============================================

# Binance

BINANCE_API_KEY = ""
BINANCE_API_SECRET = ""

# Telegram

BOT_TOKEN = "8941575381:AAFzS-0e6Zcgz3fjOs978MqtJMU1S7UQ48s"
CHAT_ID = "5839327080"

# Scanner

SCAN_INTERVAL = 300          # seconds
TOP_RESULTS = 10

# Filters

MIN_VOLUME = 5              # Million USDT
MAX_VOLUME = 80             # Million USDT

MIN_SPIKE = 1.8             # 20% Above Average

MIN_OI_CHANGE = 0.0

BREAKOUT_DISTANCE = 1.50     # %

# Alert Rules

ALERT_MIN_SCORE = 42

# Scoring

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