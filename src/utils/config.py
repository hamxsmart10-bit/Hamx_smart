"""Configuration et validation du système"""

import os
from dotenv import load_dotenv

def validate_config() -> dict:
    """Valider et charger la configuration"""
    # Charger le fichier .env
    load_dotenv()
    
    # Variables requises
    required_vars = ['EXCHANGE_NAME', 'API_KEY', 'API_SECRET']
    
    for var in required_vars:
        if not os.getenv(var):
            raise ValueError(f"Variable d'environnement manquante: {var}")
    
    config = {
        'exchange': os.getenv('EXCHANGE_NAME', 'binance'),
        'api_key': os.getenv('API_KEY'),
        'api_secret': os.getenv('API_SECRET'),
        'sandbox': os.getenv('EXCHANGE_SANDBOX', 'true').lower() == 'true',
        'base_currency': os.getenv('BASE_CURRENCY', 'USDT'),
        'trade_pair': os.getenv('TRADE_PAIR', 'BTC/USDT'),
    }
    
    return config

def get_config() -> dict:
    """Obtenir la configuration"""
    return validate_config()
