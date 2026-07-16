"""Tests basiques du système"""

import pytest
from src.core.trader import Trader
from src.core.risk_manager import RiskManager
from src.ai.predictor import PricePredictor


class TestTrader:
    """Tests du Trader"""
    
    def test_trader_init(self):
        """Test initialisation du trader"""
        trader = Trader()
        assert trader is not None
        assert trader.balance > 0
    
    def test_trader_position_status(self):
        """Test statut des positions"""
        trader = Trader()
        status = trader.get_position_status()
        assert status is not None
        assert 'status' in status
        assert status['status'] == 'ready'
    
    def test_trader_place_order(self):
        """Test placement d'ordre"""
        trader = Trader()
        order = trader.place_order('BTC/USDT', 'buy', 0.01)
        assert order is not None
        assert order['side'] == 'buy'
        assert order['pair'] == 'BTC/USDT'


class TestRiskManager:
    """Tests du Risk Manager"""
    
    def test_risk_manager_init(self):
        """Test initialisation"""
        rm = RiskManager()
        assert rm is not None
        assert rm.max_loss_percent > 0
    
    def test_validate_order(self):
        """Test validation d'ordre"""
        rm = RiskManager()
        order = {'side': 'buy', 'amount': 0.01}
        result = rm.validate_order(order)
        assert result is True
    
    def test_position_size(self):
        """Test calcul de taille de position"""
        rm = RiskManager()
        size = rm.calculate_position_size(1000, 0.02)
        assert size == 20  # 1000 * 0.02


class TestPredictor:
    """Tests du Prédicteur"""
    
    def test_predictor_init(self):
        """Test initialisation"""
        predictor = PricePredictor()
        assert predictor is not None
        assert predictor.is_trained is False
    
    def test_train_model(self):
        """Test entraînement du modèle"""
        predictor = PricePredictor()
        result = predictor.train([1, 2, 3], [4, 5, 6])
        assert result is True
        assert predictor.is_trained is True
