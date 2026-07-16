#!/usr/bin/env python
"""
Point d'entrée principal du robot trader Hamx_smart
Gère le démarrage et la boucle principale
"""

import argparse
import sys
from src.utils.logger import get_logger
from src.utils.config import validate_config
from src.core.trader import Trader
from src.core.risk_manager import RiskManager

logger = get_logger("main")


def main():
    """Fonction principale"""
    parser = argparse.ArgumentParser(description="Hamx_smart - Robot trader IA")
    parser.add_argument("--mode", choices=["backtest", "live", "paper"], 
                       default="paper", help="Mode d'exécution")
    parser.add_argument("--pair", default="BTC/USDT", help="Paire de trading")
    parser.add_argument("--start-date", help="Date de début (pour backtest)")
    parser.add_argument("--debug", action="store_true", help="Mode debug")
    
    args = parser.parse_args()
    
    try:
        # Valider la configuration
        validate_config()
        logger.info("🤖 Hamx_smart - Robot trader IA v0.1.0")
        logger.info(f"Mode: {args.mode.upper()}")
        logger.info(f"Paire: {args.pair}")
        
        # Initialiser les composants
        trader = Trader()
        risk_manager = RiskManager()
        
        if args.mode == "backtest":
            logger.info("🔄 Lancement du backtest...")
            # TODO: Implémenter le backtest
            logger.info("Backtest en construction")
        
        elif args.mode == "live":
            logger.warning("⚠️ MODE TRADING RÉEL - Être prudent!")
            logger.info("🟢 Robot en mode LIVE")
            # TODO: Implémenter la boucle de trading live
        
        elif args.mode == "paper":
            logger.info("📝 Mode papier (simulation)")
            # Afficher le statut
            status = trader.get_position_status()
            logger.info(f"Statut position: {status}")
        
        logger.info("✓ Robot trader prêt")
        
    except ValueError as e:
        logger.error(f"Erreur de configuration: {e}")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Erreur fatale: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
