"""
Module d'intégration avec les exchanges de crypto
Supporte Binance, Kraken, Coinbase via CCXT
"""

from typing import Dict, List, Optional
import ccxt
from src.utils.logger import get_logger
from src.utils.config import (
    EXCHANGE_NAME, API_KEY, API_SECRET, EXCHANGE_SANDBOX
)

logger = get_logger("exchange")


class ExchangeConnector:
    """Connecteur universel pour les exchanges"""
    
    def __init__(self):
        """Initialiser la connexion à l'exchange"""
        self.exchange_name = EXCHANGE_NAME.lower()
        self._init_exchange()
        logger.info(f"✓ Connecté à {EXCHANGE_NAME}")
    
    def _init_exchange(self):
        """Initialiser l'exchange selon la config"""
        exchange_class = getattr(ccxt, self.exchange_name)
        self.exchange = exchange_class({
            'apiKey': API_KEY,
            'secret': API_SECRET,
            'sandbox': EXCHANGE_SANDBOX,
            'enableRateLimit': True
        })
    
    def get_ticker(self, pair: str) -> Dict:
        """Obtenir les données de prix pour une paire"""
        try:
            return self.exchange.fetch_ticker(pair)
        except Exception as e:
            logger.error(f"Erreur lors de la récupération du ticker: {e}")
            return {}
    
    def get_ohlcv(self, pair: str, timeframe: str = "1h", limit: int = 100) -> List:
        """Obtenir les données OHLCV (bougies)"""
        try:
            return self.exchange.fetch_ohlcv(pair, timeframe, limit=limit)
        except Exception as e:
            logger.error(f"Erreur lors de la récupération OHLCV: {e}")
            return []
    
    def get_balance(self) -> Dict:
        """Obtenir le solde du compte"""
        try:
            return self.exchange.fetch_balance()
        except Exception as e:
            logger.error(f"Erreur lors de la récupération du solde: {e}")
            return {}
    
    def place_order(self, pair: str, side: str, amount: float, price: Optional[float] = None) -> Dict:
        """Passer une commande"""
        try:
            if price:
                order = self.exchange.create_limit_order(pair, side, amount, price)
            else:
                order = self.exchange.create_market_order(pair, side, amount)
            logger.info(f"Commande {side} {amount} {pair} créée: {order['id']}")
            return order
        except Exception as e:
            logger.error(f"Erreur lors de la création de commande: {e}")
            return {}
    
    def cancel_order(self, pair: str, order_id: str) -> bool:
        """Annuler une commande"""
        try:
            self.exchange.cancel_order(order_id, pair)
            logger.info(f"Commande {order_id} annulée")
            return True
        except Exception as e:
            logger.error(f"Erreur lors de l'annulation: {e}")
            return False
    
    def get_order(self, pair: str, order_id: str) -> Dict:
        """Obtenir les infos d'une commande"""
        try:
            return self.exchange.fetch_order(order_id, pair)
        except Exception as e:
            logger.error(f"Erreur lors de la récupération de la commande: {e}")
            return {}
