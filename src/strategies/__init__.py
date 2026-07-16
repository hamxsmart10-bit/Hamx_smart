"""
Stratégies de trading implémentables
"""

from abc import ABC, abstractmethod
from typing import Dict, Optional, List
from datetime import datetime
from src.utils.logger import get_logger
from src.ai.indicators import TechnicalIndicators

logger = get_logger("strategies")


class BaseStrategy(ABC):
    """Classe de base pour les stratégies de trading"""
    
    def __init__(self, name: str):
        self.name = name
        self.signals = []
        logger.info(f"Stratégie {name} initialisée")
    
    @abstractmethod
    def analyze(self, prices: List[float]) -> Dict:
        """Analyser les prix et générer un signal"""
        pass
    
    def generate_signal(self, signal_type: str, strength: float, reason: str):
        """Générer un signal de trading"""
        signal = {
            'type': signal_type,  # 'BUY', 'SELL', 'HOLD'
            'strength': strength,  # 0-1
            'reason': reason,
            'timestamp': datetime.now()
        }
        self.signals.append(signal)
        return signal


class MovingAverageCrossover(BaseStrategy):
    """Stratégie: Croisement des moyennes mobiles (Golden Cross)"""
    
    def __init__(self, short_period: int = 20, long_period: int = 50):
        super().__init__("MA Crossover")
        self.short_period = short_period
        self.long_period = long_period
    
    def analyze(self, prices: List[float]) -> Dict:
        """Analyser avec le croisement MA"""
        if len(prices) < self.long_period:
            return {'signal': 'HOLD', 'reason': 'Pas assez de données'}
        
        ma_short = TechnicalIndicators.calculate_ma(prices, self.short_period)
        ma_long = TechnicalIndicators.calculate_ma(prices, self.long_period)
        
        if not ma_short or not ma_long:
            return {'signal': 'HOLD', 'reason': 'Calcul MA échoué'}
        
        current_short = ma_short[-1]
        current_long = ma_long[-1]
        prev_short = ma_short[-2] if len(ma_short) > 1 else current_short
        prev_long = ma_long[-2] if len(ma_long) > 1 else current_long
        
        # Golden Cross: MA court dépasse MA long
        if prev_short <= prev_long and current_short > current_long:
            signal = self.generate_signal(
                'BUY', 0.8, 
                f"Golden Cross: MA{self.short_period} > MA{self.long_period}"
            )
            return signal
        
        # Death Cross: MA court descend sous MA long
        elif prev_short >= prev_long and current_short < current_long:
            signal = self.generate_signal(
                'SELL', 0.8,
                f"Death Cross: MA{self.short_period} < MA{self.long_period}"
            )
            return signal
        
        return {'signal': 'HOLD', 'reason': 'Pas de crossover détecté'}


class RSIStrategy(BaseStrategy):
    """Stratégie: RSI (Relative Strength Index)"""
    
    def __init__(self, overbought: float = 70, oversold: float = 30):
        super().__init__("RSI Strategy")
        self.overbought = overbought
        self.oversold = oversold
    
    def analyze(self, prices: List[float]) -> Dict:
        """Analyser avec RSI"""
        if len(prices) < 15:
            return {'signal': 'HOLD', 'reason': 'Pas assez de données'}
        
        rsi_values = TechnicalIndicators.calculate_rsi(prices)
        if not rsi_values:
            return {'signal': 'HOLD', 'reason': 'Calcul RSI échoué'}
        
        current_rsi = rsi_values[-1]
        
        if current_rsi < self.oversold:
            signal = self.generate_signal(
                'BUY', 0.7,
                f"RSI Oversold: {current_rsi:.2f} < {self.oversold}"
            )
            return signal
        
        elif current_rsi > self.overbought:
            signal = self.generate_signal(
                'SELL', 0.7,
                f"RSI Overbought: {current_rsi:.2f} > {self.overbought}"
            )
            return signal
        
        return {'signal': 'HOLD', 'reason': f'RSI neutral: {current_rsi:.2f}'}


class BollingerBandsStrategy(BaseStrategy):
    """Stratégie: Bandes de Bollinger"""
    
    def __init__(self, period: int = 20, std_dev: int = 2):
        super().__init__("Bollinger Bands")
        self.period = period
        self.std_dev = std_dev
    
    def analyze(self, prices: List[float]) -> Dict:
        """Analyser avec Bollinger Bands"""
        if len(prices) < self.period:
            return {'signal': 'HOLD', 'reason': 'Pas assez de données'}
        
        bands = TechnicalIndicators.calculate_bollinger_bands(
            prices, self.period, self.std_dev
        )
        
        current_price = prices[-1]
        upper = bands['upper'][-1]
        lower = bands['lower'][-1]
        middle = bands['middle'][-1]
        
        # Prix touche la bande basse: BUY
        if current_price <= lower:
            signal = self.generate_signal(
                'BUY', 0.75,
                f"Prix at lower band: {current_price:.2f} <= {lower:.2f}"
            )
            return signal
        
        # Prix touche la bande haute: SELL
        elif current_price >= upper:
            signal = self.generate_signal(
                'SELL', 0.75,
                f"Prix at upper band: {current_price:.2f} >= {upper:.2f}"
            )
            return signal
        
        return {'signal': 'HOLD', 'reason': 'Prix within bands'}


class MACDStrategy(BaseStrategy):
    """Stratégie: MACD (Moving Average Convergence Divergence)"""
    
    def __init__(self):
        super().__init__("MACD Strategy")
    
    def analyze(self, prices: List[float]) -> Dict:
        """Analyser avec MACD"""
        if len(prices) < 30:
            return {'signal': 'HOLD', 'reason': 'Pas assez de données'}
        
        macd_data = TechnicalIndicators.calculate_macd(prices)
        
        macd_line = macd_data['macd']
        signal_line = macd_data['signal']
        histogram = macd_data['histogram']
        
        if not macd_line or not signal_line:
            return {'signal': 'HOLD', 'reason': 'Calcul MACD échoué'}
        
        current_macd = macd_line[-1]
        current_signal = signal_line[-1]
        current_histogram = histogram[-1]
        prev_histogram = histogram[-2] if len(histogram) > 1 else current_histogram
        
        # MACD croise au-dessus de la ligne de signal
        if prev_histogram <= 0 and current_histogram > 0:
            signal = self.generate_signal(
                'BUY', 0.8,
                "MACD bullish crossover"
            )
            return signal
        
        # MACD croise au-dessous de la ligne de signal
        elif prev_histogram >= 0 and current_histogram < 0:
            signal = self.generate_signal(
                'SELL', 0.8,
                "MACD bearish crossover"
            )
            return signal
        
        return {'signal': 'HOLD', 'reason': 'MACD no crossover'}


class CombinedStrategy(BaseStrategy):
    """Stratégie combinée: Consensus de plusieurs stratégies"""
    
    def __init__(self):
        super().__init__("Combined Strategy")
        self.strategies = [
            MovingAverageCrossover(),
            RSIStrategy(),
            BollingerBandsStrategy(),
            MACDStrategy()
        ]
    
    def analyze(self, prices: List[float]) -> Dict:
        """Analyser avec consensus de stratégies"""
        buy_signals = 0
        sell_signals = 0
        
        for strategy in self.strategies:
            result = strategy.analyze(prices)
            if result.get('signal') == 'BUY':
                buy_signals += 1
            elif result.get('signal') == 'SELL':
                sell_signals += 1
        
        total_signals = buy_signals + sell_signals
        
        if buy_signals > sell_signals and buy_signals >= 2:
            strength = buy_signals / len(self.strategies)
            signal = self.generate_signal(
                'BUY', strength,
                f"Consensus BUY: {buy_signals}/{len(self.strategies)} stratégies"
            )
            return signal
        
        elif sell_signals > buy_signals and sell_signals >= 2:
            strength = sell_signals / len(self.strategies)
            signal = self.generate_signal(
                'SELL', strength,
                f"Consensus SELL: {sell_signals}/{len(self.strategies)} stratégies"
            )
            return signal
        
        return {'signal': 'HOLD', 'reason': 'Pas de consensus'}


def get_strategy(name: str) -> Optional[BaseStrategy]:
    """Factory pour obtenir une stratégie par son nom"""
    strategies = {
        'ma_crossover': MovingAverageCrossover,
        'rsi': RSIStrategy,
        'bollinger': BollingerBandsStrategy,
        'macd': MACDStrategy,
        'combined': CombinedStrategy
    }
    
    strategy_class = strategies.get(name.lower())
    if strategy_class:
        return strategy_class()
    
    logger.warning(f"Stratégie '{name}' non trouvée")
    return None
