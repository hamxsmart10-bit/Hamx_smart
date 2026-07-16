# Hamx_smart 🤖

**Un robot trader intelligent alimenté par l'IA pour l'automatisation du trading**

## 📋 Table des matières
- [À propos](#à-propos)
- [Fonctionnalités](#fonctionnalités)
- [Installation](#installation)
- [Configuration](#configuration)
- [Utilisation](#utilisation)
- [Architecture](#architecture)
- [Contribuer](#contribuer)
- [Licence](#licence)

## À propos

Hamx_smart est un système de trading automatisé utilisant l'intelligence artificielle pour :
- Analyser les marchés financiers en temps réel
- Générer des signaux de trading basés sur des indicateurs techniques et ML
- Exécuter des ordres automatiquement avec gestion des risques
- Tracker les performances et générer des rapports

## Fonctionnalités

✨ **Core Features**
- 🔄 Connexion multi-exchange (Binance, Kraken, etc.)
- 📊 Analyse technique avancée avec TA-Lib
- 🧠 Modèles ML pour prédiction de prix
- ⚡ Exécution haute performance des ordres
- 🛡️ Gestion des risques et stop-loss automatique
- 📈 Dashboard de monitoring en temps réel
- 💾 Logging complet et backtesting

## Installation

### Prérequis
- Python 3.9+
- pip ou conda
- Compte d'exchange (Binance, Kraken, etc.)

### Étapes

```bash
# 1. Cloner le repository
git clone https://github.com/hamxsmart10-bit/Hamx_smart.git
cd Hamx_smart

# 2. Créer un environnement virtuel
python -m venv venv
source venv/bin/activate  # Sur Windows: venv\Scripts\activate

# 3. Installer les dépendances
pip install -r requirements.txt

# 4. Configurer les variables d'environnement
cp .env.example .env
# Éditer .env avec vos credentials
```

## Configuration

### Variables d'environnement (.env)

```env
# Exchange Configuration
EXCHANGE_NAME=binance
API_KEY=your_api_key_here
API_SECRET=your_api_secret_here

# Trading Parameters
BASE_CURRENCY=USDT
TRADE_PAIR=BTC/USDT
POSITION_SIZE=0.01

# Risk Management
STOP_LOSS_PERCENT=2.0
TAKE_PROFIT_PERCENT=5.0
MAX_TRADES=5

# AI Model
MODEL_PATH=./models/price_predictor.pkl
PREDICTION_HORIZON=1h

# Logging
LOG_LEVEL=INFO
LOG_FILE=./logs/hamx_smart.log
```

## Utilisation

### Démarrer le robot en mode simulation

```bash
python main.py --mode=backtest --pair=BTC/USDT --start-date=2024-01-01
```

### Démarrer en mode trading réel (avec prudence)

```bash
python main.py --mode=live --pair=BTC/USDT
```

### Générer un rapport de performance

```bash
python scripts/generate_report.py --date-range=30d
```

## Architecture

```
Hamx_smart/
├── src/
│   ├── core/
│   │   ├── exchange.py        # Intégration exchanges
│   │   ├── trader.py          # Logique de trading
│   │   └── risk_manager.py    # Gestion des risques
│   ├── ai/
│   │   ├── predictor.py       # Modèles de prédiction
│   │   ├── indicators.py      # Indicateurs techniques
│   │   └── features.py        # Feature engineering
│   ├── utils/
│   │   ├── logger.py          # Logging centralisé
│   │   ├── config.py          # Configuration
│   │   └── helpers.py         # Utilitaires
│   └── api/
│       └── dashboard.py       # API du dashboard
├── tests/
│   ├── unit/                  # Tests unitaires
│   ├── integration/           # Tests d'intégration
│   └── fixtures/              # Données de test
├── models/                    # Modèles ML pré-entraînés
├── data/                      # Historique des données
├── logs/                      # Fichiers de logs
├── scripts/
│   ├── backtest.py           # Script de backtesting
│   ├── train_models.py       # Entraînement ML
│   └── generate_report.py    # Génération de rapports
├── config/
��   ├── exchanges.yaml        # Config exchanges
│   ├── strategies.yaml       # Config stratégies
│   └── risk_profiles.yaml    # Profils de risque
├── requirements.txt           # Dépendances Python
├── main.py                    # Point d'entrée
├── .env.example              # Template variables d'env
└── README.md                 # Cette documentation
```

### Flux de données

```
Market Data (Exchange API)
    ↓
Technical Indicators & Features
    ↓
AI Model Prediction
    ↓
Signal Generation
    ↓
Risk Manager (Validation)
    ↓
Order Execution (Trader)
    ↓
Monitoring & Logging
```

## Tests

```bash
# Tous les tests
pytest

# Tests unitaires seulement
pytest tests/unit/

# Tests avec couverture
pytest --cov=src tests/
```

## Contribuer

Les contributions sont bienvenues ! Pour contribuer :

1. Fork le projet
2. Créer une branche pour votre feature (`git checkout -b feature/AmazingFeature`)
3. Commit vos changements (`git commit -m 'Add some AmazingFeature'`)
4. Push vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrir une Pull Request

## Avertissements ⚠️

- Le trading algorithmique comporte des risques significatifs
- Commencez avec le mode backtest et simulation
- Ne déployez pas d'argent réel sans tests approfondis
- Respectez les conditions d'utilisation de votre exchange
- Gardez vos API keys sécurisées

## Licence

Ce projet est sous licence [GPL-3.0](LICENSE) - voir le fichier LICENSE pour les détails.

## Contact & Support

- 📧 Email: hamxsmart10-bit@example.com
- 🐛 Issues: [Ouvrir une issue](https://github.com/hamxsmart10-bit/Hamx_smart/issues)
- 💬 Discussions: [Rejoindre les discussions](https://github.com/hamxsmart10-bit/Hamx_smart/discussions)

---

**⭐ Si ce projet vous aide, n'hésitez pas à lui donner une star !**
