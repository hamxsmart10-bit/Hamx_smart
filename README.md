# Hamx_smart 🤖

**Un robot trader intelligent alimenté par l'IA pour l'automatisation du trading**

## 📋 Table des matières
- [À propos](#à-propos)
- [Installation Rapide](#installation-rapide)
- [Utilisation](#utilisation)
- [Architecture](#architecture)
- [Licence](#licence)

## À propos

Hamx_smart est un système de trading automatisé utilisant l'intelligence artificielle pour :
- Analyser les marchés financiers en temps réel
- Générer des signaux de trading basés sur des indicateurs techniques et ML
- Exécuter des ordres automatiquement avec gestion des risques
- Tracker les performances et générer des rapports

## ✨ Fonctionnalités

- 🤖 Robot trader intelligent
- 📊 Analyse technique avancée
- 🧠 Modèles ML pour prédiction de prix
- ⚡ Exécution haute performance
- 🛡️ Gestion des risques automatique
- 📈 Monitoring en temps réel
- 💾 Logging complet

## 🚀 Installation Rapide

### Prérequis
- Python 3.9+
- pip

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

## 📖 Utilisation

### Mode PAPIER (Simulation - Sans risque) ✅

```bash
python main.py --mode=paper --pair=BTC/USDT
```

### Mode BACKTEST (Historique)

```bash
python main.py --mode=backtest --pair=BTC/USDT --start-date=2024-01-01
```

### Mode LIVE (Argent réel) ⚠️

```bash
python main.py --mode=live --pair=BTC/USDT
```

## 🏗️ Architecture

```
Hamx_smart/
├── src/
│   ├── core/           # Cœur du trading
│   │   ├── trader.py
│   │   └── risk_manager.py
│   ├── ai/             # Modèles IA
│   │   └── predictor.py
│   ├── api/            # Dashboard
│   │   └── dashboard.py
│   └── utils/          # Utilitaires
│       ├── logger.py
│       └── config.py
├── tests/              # Tests
├── main.py            # Point d'entrée
├── requirements.txt   # Dépendances
└── .env.example      # Template config
```

## 🧪 Tests

```bash
# Tous les tests
pytest

# Avec couverture
pytest --cov=src
```

## ⚠️ Avertissements

- Le trading algorithmique comporte des risques significatifs
- Commencez avec le mode PAPER
- Ne déployez pas d'argent réel sans tests approfondis
- Gardez vos API keys sécurisées

## 📝 Licence

Ce projet est sous licence [GPL-3.0](LICENSE)

## 🆘 Support

- 📖 [Guide d'Installation](INSTALLATION_GUIDE.md)
- ⚡ [Démarrage Rapide](QUICKSTART.md)
- 🚀 [Guide de Déploiement](DEPLOYMENT.md)
- 🔄 [Guide de Release](RELEASE.md)

---

**⭐ Si ce projet vous aide, n'hésitez pas à lui donner une star !**
