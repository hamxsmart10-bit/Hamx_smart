"""
Tests unitaires pour le RiskManager
"""

import pytest
from src.core.risk_manager import RiskManager


@pytest.fixture
def risk_manager():
    """Fixture: RiskManager"""
    return RiskManager()


def test_calculate_stop_loss(risk_manager):
    """Test: Calcul du stop-loss"""
    entry_price = 100.0
    sl = risk_manager.calculate_stop_loss(entry_price)
    
    # À 2% par défaut
    assert sl < entry_price
    assert sl == pytest.approx(98.0, 0.1)


def test_calculate_take_profit(risk_manager):
    """Test: Calcul du take-profit"""
    entry_price = 100.0
    tp = risk_manager.calculate_take_profit(entry_price)
    
    # À 5% par défaut
    assert tp > entry_price
    assert tp == pytest.approx(105.0, 0.1)


def test_check_stop_loss_triggered(risk_manager):
    """Test: Stop-loss atteint"""
    entry_price = 100.0
    current_price = 97.0  # Moins de 2%
    
    triggered = risk_manager.check_stop_loss(entry_price, current_price)
    assert triggered is True


def test_check_stop_loss_not_triggered(risk_manager):
    """Test: Stop-loss non atteint"""
    entry_price = 100.0
    current_price = 99.5
    
    triggered = risk_manager.check_stop_loss(entry_price, current_price)
    assert triggered is False


def test_check_take_profit_triggered(risk_manager):
    """Test: Take-profit atteint"""
    entry_price = 100.0
    current_price = 105.5  # Plus de 5%
    
    triggered = risk_manager.check_take_profit(entry_price, current_price)
    assert triggered is True


def test_check_take_profit_not_triggered(risk_manager):
    """Test: Take-profit non atteint"""
    entry_price = 100.0
    current_price = 104.0
    
    triggered = risk_manager.check_take_profit(entry_price, current_price)
    assert triggered is False


def test_validate_order_success(risk_manager):
    """Test: Validation d'ordre (succès)"""
    is_valid = risk_manager.validate_order(100.0, 1.0)
    assert is_valid is True


def test_validate_order_max_trades_exceeded(risk_manager):
    """Test: Validation d'ordre (limite dépassée)"""
    risk_manager.trades_today = 10  # Dépasse MAX_TRADES
    is_valid = risk_manager.validate_order(100.0, 1.0)
    assert is_valid is False


def test_record_trade_result_profit(risk_manager):
    """Test: Enregistrement d'un profit"""
    initial_trades = risk_manager.trades_today
    risk_manager.record_trade_result(2.5)  # +2.5%
    
    assert risk_manager.trades_today == initial_trades + 1
    assert risk_manager.daily_loss == 0


def test_record_trade_result_loss(risk_manager):
    """Test: Enregistrement d'une perte"""
    initial_trades = risk_manager.trades_today
    risk_manager.record_trade_result(-3.0)  # -3%
    
    assert risk_manager.trades_today == initial_trades + 1
    assert risk_manager.daily_loss == 3.0
