# 📦 Guide d'Installation Complet - Hamx_smart

## 🚀 Installation Rapide (Débutant)

### Étape 1: Prérequis
```bash
# Vérifiez que vous avez Python 3.9+
python --version

# Si vous n'avez pas Python: installez depuis python.org
```

### Étape 2: Cloner le projet
```bash
# Créer un dossier pour vos projets
mkdir mes-projets
cd mes-projets

# Cloner le repository
git clone https://github.com/hamxsmart10-bit/Hamx_smart.git
cd Hamx_smart
```

### Étape 3: Créer un environnement virtuel
```bash
# Sur Windows:
python -m venv venv
venv\Scripts\activate

# Sur macOS/Linux:
python3 -m venv venv
source venv/bin/activate
```

### Étape 4: Installer les dépendances
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Étape 5: Configurer les variables d'environnement
```bash
# Copier le template
cp .env.example .env

# Éditer .env avec un éditeur de texte
# Windows: notepad .env
# macOS/Linux: nano .env
# VS Code: code .env
```

## 🔑 Configuration de l'API

### Binance (Recommandé pour les tests)
1. Aller sur https://www.binance.com
2. Créer un compte
3. Aller dans "API Management"
4. Créer une clé API
5. Copier la clé et le secret dans `.env`:
```env
EXCHANGE_NAME=binance
API_KEY=votre_clé_ici
API_SECRET=votre_secret_ici
EXCHANGE_SANDBOX=true  # Pour tester sans argent réel
```

⚠️ **IMPORTANT**: Ne partagez JAMAIS votre API_SECRET!

## ✅ Vérifier l'installation

```bash
# Test simple
python main.py --mode=paper

# Vous devriez voir:
# 🤖 Hamx_smart - Robot trader IA v1.0.0
# Mode: PAPER
# Paire: BTC/USDT
# 📝 Mode papier (simulation)
```

## 🎮 Premiers pas

### Mode 1: Simulation (PAPIER) - Sans risque ✅
```bash
# Teste sans argent réel
python main.py --mode=paper --pair=BTC/USDT
```

### Mode 2: Backtest - Analyze historique
```bash
# Teste sur les données passées
python main.py --mode=backtest --pair=BTC/USDT --start-date=2024-01-01
```

### Mode 3: LIVE - Argent réel ⚠️
```bash
# Utilisez SEULEMENT après avoir testé les modes 1 et 2!
python main.py --mode=live --pair=BTC/USDT
```

## 🧪 Exécuter les tests

```bash
# Tous les tests
pytest

# Tests avec couverture de code
pytest --cov=src

# Tests d'un module spécifique
pytest tests/unit/
```

## 🔧 Dépannage

### Erreur: "command not found: python"
```bash
# Utilisez python3 au lieu de python
python3 --version
python3 -m venv venv
```

### Erreur: "ImportError: No module named 'src'"
```bash
# Assurez-vous d'être dans le bon dossier
cd Hamx_smart
# Réactivez l'environnement virtuel
source venv/bin/activate  # ou venv\Scripts\activate
```

### Erreur: "API connection failed"
```bash
# Vérifiez votre .env
cat .env  # ou type .env

# Vérifiez votre connexion internet
ping binance.com
```

### Erreur avec ta-lib
```bash
# ta-lib est difficile à installer, essayez:
pip install --upgrade ta-lib

# Si ça échoue, commentez-le dans requirements.txt et utilisez 'ta' à la place
```

## 📚 Documentation additionnelle

- `README.md` - Vue d'ensemble
- `ARCHITECTURE.md` - Architecture du système
- `CONTRIBUTING.md` - Comment contribuer

## 🆘 Besoin d'aide?

- 📖 Lire la documentation
- 🐛 Ouvrir une issue: https://github.com/hamxsmart10-bit/Hamx_smart/issues
- 💬 Discussions: https://github.com/hamxsmart10-bit/Hamx_smart/discussions

---

**Vous êtes prêt! 🎉 Commencez par le Mode PAPIER pour comprendre comment ça marche.**
