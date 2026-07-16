"""
Utilitaires et fonctions helper pour Hamx_smart
"""

from datetime import datetime, timedelta
from typing import Dict, List, Tuple
import json


def format_price(price: float, decimals: int = 2) -> str:
    """Formater un prix avec la bonne précision"""
    return f"${price:,.{decimals}f}"


def format_percentage(value: float, decimals: int = 2) -> str:
    """Formater un pourcentage"""
    sign = "+" if value >= 0 else ""
    return f"{sign}{value:.{decimals}f}%"


def calculate_roi(initial: float, final: float) -> float:
    """Calculer le ROI (Return on Investment)"""
    if initial == 0:
        return 0
    return ((final - initial) / initial) * 100


def get_time_range(days: int) -> Tuple[datetime, datetime]:
    """Obtenir une plage de temps pour les derniers N jours"""
    end_time = datetime.now()
    start_time = end_time - timedelta(days=days)
    return start_time, end_time


def validate_pair(pair: str) -> bool:
    """Valider le format d'une paire de trading"""
    try:
        base, quote = pair.split("/")
        return len(base) > 0 and len(quote) > 0
    except ValueError:
        return False


def merge_dicts(*dicts: Dict) -> Dict:
    """Fusionner plusieurs dictionnaires"""
    result = {}
    for d in dicts:
        result.update(d)
    return result


def safe_json_encode(obj, default_handler=str):
    """Encoder en JSON de façon sécurisée"""
    try:
        return json.dumps(obj, default=default_handler)
    except Exception as e:
        return json.dumps({"error": str(e)})
