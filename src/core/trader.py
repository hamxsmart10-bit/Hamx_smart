"""Classe Trader - Gestion du trading"""

from src.utils.logger import get_logger

logger = get_logger("trader")


class Trader:
    """
    Gère la logique de trading
    """

    def __init__(self):
        """
        Initialiser le trader
        """
        self.positions = []
        self.orders = []
        self.balance = 1000.0  # Solde initial
        self.equity = self.balance
        logger.info("Trader initialisé")

    def get_position_status(self) -> dict:
        """
        Obtenir le statut des positions
        
        Returns:
            Dictionnaire avec le statut
        """
        status = {
            'positions_count': len(self.positions),
            'orders_count': len(self.orders),
            'balance': self.balance,
            'equity': self.equity,
            'status': 'ready'
        }
        logger.info(f"Statut: {status}")
        return status

    def place_order(self, pair: str, side: str, amount: float) -> dict:
        """
        Placer une commande
        
        Args:
            pair: Paire de trading (ex: BTC/USDT)
            side: Côté (buy ou sell)
            amount: Montant
            
        Returns:
            Dictionnaire de la commande
        """
        order = {
            'pair': pair,
            'side': side,
            'amount': amount,
            'status': 'pending',
            'order_id': f"order_{len(self.orders) + 1}"
        }
        self.orders.append(order)
        logger.info(f"Ordre placé: {side} {amount} {pair}")
        return order

    def close_position(self, position_id: str) -> bool:
        """
        Fermer une position
        
        Args:
            position_id: ID de la position
            
        Returns:
            True si succès
        """
        logger.info(f"Fermeture de la position: {position_id}")
        return True
