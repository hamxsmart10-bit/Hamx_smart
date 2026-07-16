"""Dashboard web pour monitoring"""

from src.utils.logger import get_logger

logger = get_logger("dashboard")

class Dashboard:
    """Dashboard de monitoring"""
    
    def __init__(self, host='0.0.0.0', port=8000):
        """Initialiser le dashboard"""
        self.host = host
        self.port = port
        logger.info(f"Dashboard initialisé sur {host}:{port}")
    
    def start(self):
        """Démarrer le dashboard"""
        logger.info(f"Dashboard démarré sur http://{self.host}:{self.port}")
