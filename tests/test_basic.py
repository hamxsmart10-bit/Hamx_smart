"""Tests basiques"""

import pytest
from src.core.trader import Trader
from src.core.risk_manager import RiskManager
from src.utils.config import validate_config

def test_trader_init():
    """Test initialisation du trader"""
    trader = Trader()
    status = trader.get_position_status()
    assert status is not None
    assert 'status' in status

def test_risk_manager_init():
    """Test initialisation du risk manager"""
    rm = RiskManager()
    assert rm.max_loss > 0

def test_trader_order():
    """Test placement d'ordre"""
    trader = Trader()
    order = trader.place_order('BTC/USDT', 'buy', 0.01)
    assert order is not None
    assert 'order_id' in order
