"""
Gestion des risques et validation des ordres
"""

from typing import Optional, Dict
from src.utils.logger import get_logger
from src.utils.config import (
    STOP_LOSS_PERCENT, TAKE_PROFIT_PERCENT, MAX_TRADES, MAX_DAILY_LOSS_PERCENT
)

logger = get_logger("risk_manager")


class RiskManager:
    """Gestionnaire des risques de trading"""
    
    def __init__(self):
        """Initialiser le gestionnaire de risques"""
        self.daily_loss = 0
        self.trades_today = 0
        logger.info("✓ Gestionnaire de risques initialisé")
    
    def validate_order(self, entry_price: float, amount: float) -> bool:
        """Valider un ordre avant l'exécution"""
        if self.trades_today >= MAX_TRADES:
            logger.warning(f"❌ Limite du nombre de trades atteinte ({MAX_TRADES})")
            return False
        
        if self.daily_loss >= MAX_DAILY_LOSS_PERCENT:
            logger.warning(f"❌ Limite de perte quotidienne atteinte ({MAX_DAILY_LOSS_PERCENT}%)")
            return False
        
        return True
    
    def calculate_stop_loss(self, entry_price: float) -> float:
        """Calculer le prix de stop-loss"""
        sl = entry_price * (1 - STOP_LOSS_PERCENT / 100)
        logger.debug(f"Stop-loss calculé: {sl}")
        return sl
    
    def calculate_take_profit(self, entry_price: float) -> float:
        """Calculer le prix de take-profit"""
        tp = entry_price * (1 + TAKE_PROFIT_PERCENT / 100)
        logger.debug(f"Take-profit calculé: {tp}")
        return tp
    
    def check_stop_loss(self, entry_price: float, current_price: float) -> bool:
        """Vérifier si le stop-loss est atteint"""
        sl = self.calculate_stop_loss(entry_price)
        if current_price <= sl:
            logger.warning(f"⚠️ Stop-loss atteint: {current_price} <= {sl}")
            return True
        return False
    
    def check_take_profit(self, entry_price: float, current_price: float) -> bool:
        """Vérifier si le take-profit est atteint"""
        tp = self.calculate_take_profit(entry_price)
        if current_price >= tp:
            logger.info(f"✓ Take-profit atteint: {current_price} >= {tp}")
            return True
        return False
    
    def record_trade_result(self, pnl_percent: float):
        """Enregistrer le résultat d'une transaction"""
        self.trades_today += 1
        if pnl_percent < 0:
            self.daily_loss += abs(pnl_percent)
        logger.info(f"Trade #{self.trades_today} - PnL: {pnl_percent:.2f}%")
