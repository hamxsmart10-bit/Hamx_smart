"""Configuration du système"""

import os
from pathlib import Path
from dotenv import load_dotenv

from src.utils.logger import get_logger

logger = get_logger("config")


def load_env():
    """
    Charger les variables d'environnement depuis .env
    """
    env_path = Path('.env')
    
    if not env_path.exists():
        logger.warning(f"Fichier .env non trouvé")
        return False
    
    load_dotenv(env_path)
    logger.info("Variables d'environnement chargées")
    return True


def validate_config() -> dict:
    """
    Valider la configuration
    
    Returns:
        Dictionnaire de configuration
        
    Raises:
        ValueError: Si une variable requise est manquante
    """
    # Variables requises
    required_vars = ['EXCHANGE_NAME', 'API_KEY', 'API_SECRET']
    
    missing_vars = []
    for var in required_vars:
        value = os.getenv(var)
        if not value or value == 'your_value_here' or value.startswith('your_'):
            missing_vars.append(var)
    
    if missing_vars:
        error_msg = f"Variables d'environnement manquantes ou non configurées: {', '.join(missing_vars)}. Configurez votre fichier .env"
        logger.error(error_msg)
        raise ValueError(error_msg)
    
    config = {
        'exchange': os.getenv('EXCHANGE_NAME', 'binance'),
        'api_key': os.getenv('API_KEY'),
        'api_secret': os.getenv('API_SECRET'),
        'sandbox': os.getenv('EXCHANGE_SANDBOX', 'true').lower() == 'true',
        'base_currency': os.getenv('BASE_CURRENCY', 'USDT'),
        'trade_pair': os.getenv('TRADE_PAIR', 'BTC/USDT'),
        'stop_loss': float(os.getenv('STOP_LOSS_PERCENT', '2.0')),
        'take_profit': float(os.getenv('TAKE_PROFIT_PERCENT', '5.0')),
    }
    
    logger.info(f"Configuration validée - Exchange: {config['exchange']}, Pair: {config['trade_pair']}")
    return config


def get_config() -> dict:
    """
    Obtenir la configuration
    
    Returns:
        Dictionnaire de configuration
    """
    return validate_config()
