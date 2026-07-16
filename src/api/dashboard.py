"""Dashboard web - Monitoring"""

from src.utils.logger import get_logger

logger = get_logger("dashboard")


class Dashboard:
    """
    Dashboard de monitoring
    """

    def __init__(self, host: str = '0.0.0.0', port: int = 8000):
        """
        Initialiser le dashboard
        
        Args:
            host: Adresse du serveur
            port: Port du serveur
        """
        self.host = host
        self.port = port
        self.is_running = False
        logger.info(f"Dashboard initialisé sur {host}:{port}")

    def start(self):
        """
        Démarrer le dashboard
        """
        self.is_running = True
        logger.info(f"Dashboard démarré sur http://{self.host}:{self.port}")
        logger.info("Dashboard en construction")

    def stop(self):
        """
        Arrêter le dashboard
        """
        self.is_running = False
        logger.info("Dashboard arrêté")
