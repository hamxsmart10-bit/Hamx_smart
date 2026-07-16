"""
Logique principale du robot trader
Gère l'exécution des stratégies et les ordres
"""

from typing import Dict, Optional
from datetime import datetime
from src.utils.logger import get_logger
from src.utils.helpers import format_price, format_percentage
from src.core.exchange import ExchangeConnector
from src.utils.config import TRADE_PAIR, POSITION_SIZE

logger = get_logger("trader")


class Trader:
    """Gestionnaire principal du trading"""
    
    def __init__(self):
        """Initialiser le trader"""
        self.exchange = ExchangeConnector()
        self.current_position = None
        self.trades = []
        logger.info("✓ Robot trader initialisé")
    
    def get_current_price(self, pair: str = TRADE_PAIR) -> Optional[float]:
        """Obtenir le prix actuel d'une paire"""
        ticker = self.exchange.get_ticker(pair)
        if ticker and 'last' in ticker:
            price = ticker['last']
            logger.debug(f"Prix actuel {pair}: {format_price(price)}")
            return price
        return None
    
    def buy(self, pair: str = TRADE_PAIR, amount: float = POSITION_SIZE) -> Dict:
        """Acheter une paire"""
        current_price = self.get_current_price(pair)
        if not current_price:
            logger.error("Impossible d'obtenir le prix pour acheter")
            return {}
        
        logger.info(f"🟢 Achat de {amount} {pair} à {format_price(current_price)}")
        order = self.exchange.place_order(pair, 'buy', amount)
        
        if order:
            self.current_position = {
                'side': 'buy',
                'pair': pair,
                'amount': amount,
                'entry_price': current_price,
                'entry_time': datetime.now(),
                'order_id': order.get('id')
            }
        
        return order
    
    def sell(self, pair: str = TRADE_PAIR, amount: float = POSITION_SIZE) -> Dict:
        """Vendre une paire"""
        current_price = self.get_current_price(pair)
        if not current_price:
            logger.error("Impossible d'obtenir le prix pour vendre")
            return {}
        
        logger.info(f"🔴 Vente de {amount} {pair} à {format_price(current_price)}")
        order = self.exchange.place_order(pair, 'sell', amount)
        
        if order and self.current_position:
            roi = ((current_price - self.current_position['entry_price']) / 
                   self.current_position['entry_price']) * 100
            logger.info(f"Position fermée - ROI: {format_percentage(roi)}")
            self.trades.append({
                'entry_price': self.current_position['entry_price'],
                'exit_price': current_price,
                'roi': roi,
                'timestamp': datetime.now()
            })
            self.current_position = None
        
        return order
    
    def get_position_status(self) -> Dict:
        """Obtenir le statut de la position actuelle"""
        if not self.current_position:
            return {'status': 'no_position'}
        
        current_price = self.get_current_price(self.current_position['pair'])
        if not current_price:
            return self.current_position
        
        unrealized_roi = ((current_price - self.current_position['entry_price']) / 
                          self.current_position['entry_price']) * 100
        
        return {
            **self.current_position,
            'current_price': current_price,
            'unrealized_roi': unrealized_roi
        }
