"""Gestion des risques"""

from src.utils.logger import get_logger

logger = get_logger("risk_manager")

class RiskManager:
    """Gère les risques du trading"""
    
    def __init__(self):
        """Initialiser le gestionnaire de risques"""
        self.max_loss = 0.02  # 2%
        self.stop_loss = 0.02
        self.take_profit = 0.05
        logger.info("Risk Manager initialisé")
    
    def validate_order(self, order: dict) -> bool:
        """Valider une commande"""
        logger.info(f"Validation de l'ordre: {order}")
        return True
    
    def check_risk(self, position: dict) -> bool:
        """Vérifier les limites de risque"""
        return True
