"""Modèles de prédiction ML"""

from src.utils.logger import get_logger

logger = get_logger("predictor")

class PricePredictor:
    """Prédiction du prix des actifs"""
    
    def __init__(self):
        """Initialiser le prédicteur"""
        self.model = None
        logger.info("Price Predictor initialisé")
    
    def predict(self, data: list) -> float:
        """Prédire le prix"""
        return 0.0  # TODO: Implémenter
