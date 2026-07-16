"""
Indicateurs techniques pour l'analyse du marché
"""

from typing import List, Dict
import pandas as pd
from src.utils.logger import get_logger

logger = get_logger("indicators")


class TechnicalIndicators:
    """Calcul des indicateurs techniques"""
    
    @staticmethod
    def calculate_ma(prices: List[float], period: int) -> List[float]:
        """Calculer la moyenne mobile simple (MA)"""
        if len(prices) < period:
            return []
        df = pd.Series(prices)
        return df.rolling(window=period).mean().tolist()
    
    @staticmethod
    def calculate_ema(prices: List[float], period: int) -> List[float]:
        """Calculer la moyenne mobile exponentielle (EMA)"""
        if len(prices) < period:
            return []
        df = pd.Series(prices)
        return df.ewm(span=period, adjust=False).mean().tolist()
    
    @staticmethod
    def calculate_rsi(prices: List[float], period: int = 14) -> List[float]:
        """Calculer le RSI (Relative Strength Index)"""
        if len(prices) < period:
            return []
        
        deltas = pd.Series(prices).diff()
        seed = deltas[:period+1]
        up = seed[seed >= 0].sum() / period
        down = -seed[seed < 0].sum() / period
        rs = up / down if down != 0 else 0
        rsi = 100 - 100 / (1 + rs)
        return [rsi]
    
    @staticmethod
    def calculate_macd(prices: List[float]) -> Dict:
        """Calculer le MACD (Moving Average Convergence Divergence)"""
        df = pd.Series(prices)
        ema12 = df.ewm(span=12, adjust=False).mean()
        ema26 = df.ewm(span=26, adjust=False).mean()
        macd = ema12 - ema26
        signal = macd.ewm(span=9, adjust=False).mean()
        histogram = macd - signal
        
        return {
            'macd': macd.tolist(),
            'signal': signal.tolist(),
            'histogram': histogram.tolist()
        }
    
    @staticmethod
    def calculate_bollinger_bands(prices: List[float], period: int = 20, std_dev: int = 2) -> Dict:
        """Calculer les bandes de Bollinger"""
        df = pd.Series(prices)
        sma = df.rolling(window=period).mean()
        std = df.rolling(window=period).std()
        
        upper_band = sma + (std * std_dev)
        lower_band = sma - (std * std_dev)
        
        return {
            'middle': sma.tolist(),
            'upper': upper_band.tolist(),
            'lower': lower_band.tolist()
        }
