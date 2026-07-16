"""Logging centralisé"""

import logging
import os
from pathlib import Path


def get_logger(name: str, level=logging.INFO) -> logging.Logger:
    """
    Obtenir un logger configuré
    
    Args:
        name: Nom du logger
        level: Niveau de log (par défaut INFO)
        
    Returns:
        Logger configuré
    """
    logger = logging.getLogger(name)
    
    # Ne pas reconfigurer si déjà fait
    if logger.handlers:
        return logger
    
    logger.setLevel(level)
    
    # Format du log
    formatter = logging.Formatter(
        '[%(asctime)s] %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # Handler console
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    # Handler fichier
    log_dir = Path('logs')
    log_dir.mkdir(exist_ok=True)
    
    file_handler = logging.FileHandler(log_dir / 'hamx_smart.log')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    
    return logger
