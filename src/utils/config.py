"""
Configuration du robot trader IA Hamx_smart
Charge les paramètres depuis les variables d'environnement
"""

import os
from dotenv import load_dotenv
from pathlib import Path

# Charger les variables d'environnement
load_dotenv()

# Base paths
BASE_DIR = Path(__file__).parent.parent.parent
LOGS_DIR = BASE_DIR / "logs"
MODELS_DIR = BASE_DIR / "models"
DATA_DIR = BASE_DIR / "data"

# Créer les répertoires s'ils n'existent pas
LOGS_DIR.mkdir(exist_ok=True)
MODELS_DIR.mkdir(exist_ok=True)
DATA_DIR.mkdir(exist_ok=True)

# ====== EXCHANGE CONFIGURATION ======
EXCHANGE_NAME = os.getenv("EXCHANGE_NAME", "binance")
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
EXCHANGE_SANDBOX = os.getenv("EXCHANGE_SANDBOX", "true").lower() == "true"

# ====== TRADING PARAMETERS ======
BASE_CURRENCY = os.getenv("BASE_CURRENCY", "USDT")
TRADE_PAIR = os.getenv("TRADE_PAIR", "BTC/USDT")
POSITION_SIZE = float(os.getenv("POSITION_SIZE", "0.01"))
LEVERAGE = int(os.getenv("LEVERAGE", "1"))

# ====== RISK MANAGEMENT ======
STOP_LOSS_PERCENT = float(os.getenv("STOP_LOSS_PERCENT", "2.0"))
TAKE_PROFIT_PERCENT = float(os.getenv("TAKE_PROFIT_PERCENT", "5.0"))
MAX_TRADES = int(os.getenv("MAX_TRADES", "5"))
MAX_DAILY_LOSS_PERCENT = float(os.getenv("MAX_DAILY_LOSS_PERCENT", "10.0"))
TRAILING_STOP_PERCENT = float(os.getenv("TRAILING_STOP_PERCENT", "1.0"))

# ====== AI MODEL ======
MODEL_PATH = os.getenv("MODEL_PATH", str(MODELS_DIR / "price_predictor.pkl"))
PREDICTION_HORIZON = os.getenv("PREDICTION_HORIZON", "1h")
CONFIDENCE_THRESHOLD = float(os.getenv("CONFIDENCE_THRESHOLD", "0.65"))
UPDATE_MODEL_FREQ = os.getenv("UPDATE_MODEL_FREQ", "24h")

# ====== LOGGING ======
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
LOG_FILE = os.getenv("LOG_FILE", str(LOGS_DIR / "hamx_smart.log"))
LOG_MAX_BYTES = int(os.getenv("LOG_MAX_BYTES", "10485760"))
LOG_BACKUP_COUNT = int(os.getenv("LOG_BACKUP_COUNT", "5"))

# ====== DATABASE ======
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./hamx_smart.db")
DB_ECHO = os.getenv("DB_ECHO", "false").lower() == "true"

# ====== API DASHBOARD ======
API_HOST = os.getenv("API_HOST", "0.0.0.0")
API_PORT = int(os.getenv("API_PORT", "8000"))
API_DEBUG = os.getenv("API_DEBUG", "false").lower() == "true"

# ====== NOTIFICATIONS ======
SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

# ====== PERFORMANCE TRACKING ======
ENABLE_METRICS = os.getenv("ENABLE_METRICS", "true").lower() == "true"
METRICS_PORT = int(os.getenv("METRICS_PORT", "9090"))


def validate_config():
    """Valide les paramètres de configuration critiques"""
    errors = []
    
    if not API_KEY or not API_SECRET:
        errors.append("❌ API_KEY et API_SECRET sont requis")
    
    if STOP_LOSS_PERCENT <= 0 or STOP_LOSS_PERCENT > 50:
        errors.append("❌ STOP_LOSS_PERCENT doit être entre 0 et 50%")
    
    if POSITION_SIZE <= 0:
        errors.append("❌ POSITION_SIZE doit être positif")
    
    if errors:
        for error in errors:
            print(error)
        raise ValueError("Configuration invalide")
    
    return True
