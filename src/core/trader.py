"""Classe principale du trader"""

from src.utils.logger import get_logger

logger = get_logger("trader")

class Trader:
    """Gère la logique de trading"""
    
    def __init__(self):
        """Initialiser le trader"""
        self.positions = []
        self.balance = 0
        logger.info("Trader initialisé")
    
    def get_position_status(self) -> dict:
        """Obtenir le statut des positions"""
        return {
            'positions': len(self.positions),
            'balance': self.balance,
            'status': 'ready'
        }
    
    def place_order(self, pair: str, side: str, amount: float) -> dict:
        """Placer une commande"""
        logger.info(f"Ordre: {side} {amount} {pair}")
        return {'order_id': '1', 'status': 'pending'}
