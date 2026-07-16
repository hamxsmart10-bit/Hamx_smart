"""
Tests pour les stratégies de trading
"""

import pytest
from src.strategies import (
    MovingAverageCrossover,
    RSIStrategy,
    BollingerBandsStrategy,
    MACDStrategy,
    CombinedStrategy,
    get_strategy
)


# Données de test
@pytest.fixture
def sample_prices():
    """Fixture: Données de prix synthétiques"""
    # Trend haussier graduel
    return [
        100, 101, 102, 103, 104, 105, 106, 107, 108, 109,
        110, 111, 112, 113, 114, 115, 116, 117, 118, 119,
        120, 121, 122, 123, 124, 125, 126, 127, 128, 129,
        130, 131, 132, 133, 134, 135, 136, 137, 138, 139,
        140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150
    ]


@pytest.fixture
def sample_prices_downtrend():
    """Fixture: Données de prix en baisse"""
    return list(range(150, 99, -1))


class TestMovingAverageCrossover:
    """Tests pour la stratégie MA Crossover"""
    
    def test_ma_strategy_initialized(self):
        """Test: Initialisation"""
        strategy = MovingAverageCrossover()
        assert strategy.name == "MA Crossover"
        assert strategy.short_period == 20
        assert strategy.long_period == 50
    
    def test_ma_strategy_analyze_uptrend(self, sample_prices):
        """Test: Analyse d'un trend haussier"""
        strategy = MovingAverageCrossover()
        result = strategy.analyze(sample_prices)
        
        assert 'signal' in result or 'type' in result
    
    def test_ma_strategy_analyze_insufficient_data(self):
        """Test: Données insuffisantes"""
        strategy = MovingAverageCrossover()
        result = strategy.analyze([1, 2, 3])
        
        assert result['signal'] == 'HOLD' or result['reason']


class TestRSIStrategy:
    """Tests pour la stratégie RSI"""
    
    def test_rsi_strategy_initialized(self):
        """Test: Initialisation"""
        strategy = RSIStrategy()
        assert strategy.name == "RSI Strategy"
        assert strategy.overbought == 70
        assert strategy.oversold == 30
    
    def test_rsi_strategy_analyze(self, sample_prices):
        """Test: Analyse RSI"""
        strategy = RSIStrategy()
        result = strategy.analyze(sample_prices)
        
        assert 'signal' in result or 'type' in result


class TestStrategyFactory:
    """Tests pour la factory de stratégies"""
    
    def test_get_strategy_ma_crossover(self):
        """Test: Obtenir MA Crossover"""
        strategy = get_strategy('ma_crossover')
        assert isinstance(strategy, MovingAverageCrossover)
    
    def test_get_strategy_rsi(self):
        """Test: Obtenir RSI"""
        strategy = get_strategy('rsi')
        assert isinstance(strategy, RSIStrategy)
    
    def test_get_strategy_combined(self):
        """Test: Obtenir Combined"""
        strategy = get_strategy('combined')
        assert isinstance(strategy, CombinedStrategy)
    
    def test_get_strategy_invalid(self):
        """Test: Stratégie invalide"""
        strategy = get_strategy('invalid_strategy')
        assert strategy is None
