"""
Tests unitaires pour le module Trader
"""

import pytest
from unittest.mock import Mock, patch
from src.core.trader import Trader
from src.core.exchange import ExchangeConnector


@pytest.fixture
def mock_exchange():
    """Fixture: Mock de l'exchange"""
    with patch('src.core.trader.ExchangeConnector'):
        trader = Trader()
        trader.exchange = Mock()
        return trader


def test_get_current_price_success(mock_exchange):
    """Test: Obtenir le prix actuel (succès)"""
    mock_exchange.exchange.get_ticker.return_value = {'last': 45000.0}
    price = mock_exchange.get_current_price("BTC/USDT")
    assert price == 45000.0


def test_get_current_price_failure(mock_exchange):
    """Test: Obtenir le prix actuel (échec)"""
    mock_exchange.exchange.get_ticker.return_value = {}
    price = mock_exchange.get_current_price("BTC/USDT")
    assert price is None


def test_buy_order(mock_exchange):
    """Test: Passer un ordre d'achat"""
    mock_exchange.exchange.get_ticker.return_value = {'last': 45000.0}
    mock_exchange.exchange.place_order.return_value = {'id': 'order123'}
    
    order = mock_exchange.buy("BTC/USDT", 0.01)
    
    assert order['id'] == 'order123'
    assert mock_exchange.current_position is not None
    assert mock_exchange.current_position['side'] == 'buy'


def test_sell_order(mock_exchange):
    """Test: Passer un ordre de vente"""
    # Setup: Position ouverte
    mock_exchange.current_position = {
        'side': 'buy',
        'entry_price': 44000.0,
        'amount': 0.01
    }
    mock_exchange.exchange.get_ticker.return_value = {'last': 45000.0}
    mock_exchange.exchange.place_order.return_value = {'id': 'order456'}
    
    order = mock_exchange.sell("BTC/USDT", 0.01)
    
    assert order['id'] == 'order456'
    assert mock_exchange.current_position is None
    assert len(mock_exchange.trades) == 1


def test_get_position_status_no_position(mock_exchange):
    """Test: Status sans position ouverte"""
    status = mock_exchange.get_position_status()
    assert status['status'] == 'no_position'


def test_get_position_status_with_position(mock_exchange):
    """Test: Status avec position ouverte"""
    mock_exchange.current_position = {
        'side': 'buy',
        'entry_price': 44000.0,
        'amount': 0.01,
        'pair': 'BTC/USDT'
    }
    mock_exchange.exchange.get_ticker.return_value = {'last': 45000.0}
    
    status = mock_exchange.get_position_status()
    
    assert status['current_price'] == 45000.0
    assert status['unrealized_roi'] > 0
