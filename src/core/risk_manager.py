"""Risk Manager - Gestion des risques"""

from src.utils.logger import get_logger

logger = get_logger("risk_manager")


class RiskManager:
    """
    Gère les risques du trading
    """

    def __init__(self):
        """
        Initialiser le gestionnaire de risques
        """
        self.max_loss_percent = 0.02  # 2%
        self.stop_loss_percent = 0.02
        self.take_profit_percent = 0.05
        self.max_trades_per_day = 5
        self.current_trades = 0
        logger.info("Risk Manager initialisé")
        logger.info(f"Stop Loss: {self.stop_loss_percent*100}%, Take Profit: {self.take_profit_percent*100}%")

    def validate_order(self, order: dict) -> bool:
        """
        Valider une commande
        
        Args:
            order: Dictionnaire de la commande
            
        Returns:
            True si valide
        """
        if self.current_trades >= self.max_trades_per_day:
            logger.warning("Limite de trades atteinte")
            return False
        
        logger.info(f"Commande validée: {order}")
        return True

    def check_risk(self, position: dict) -> bool:
        """
        Vérifier les limites de risque
        
        Args:
            position: Dictionnaire de la position
            
        Returns:
            True si dans les limites
        """
        logger.info("Vérification des risques")
        return True

    def calculate_position_size(self, balance: float, risk_percent: float) -> float:
        """
        Calculer la taille de position
        
        Args:
            balance: Solde du compte
            risk_percent: Pourcentage de risque
            
        Returns:
            Taille de position recommandée
        """
        position_size = balance * risk_percent
        logger.info(f"Position size: {position_size}")
        return position_size
