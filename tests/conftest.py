"""
Configuration pytest et fixtures globales
"""

import pytest
import sys
from pathlib import Path

# Ajouter le répertoire racine au path
sys.path.insert(0, str(Path(__file__).parent.parent))


@pytest.fixture(scope="session")
def test_config():
    """Fixture: Configuration de test"""
    return {
        'exchange': 'binance',
        'test_pair': 'BTC/USDT',
        'test_amount': 0.01
    }
