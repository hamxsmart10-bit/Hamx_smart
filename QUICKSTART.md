# ⚡ Démarrage Rapide en 5 Minutes

## Vous êtes impatient? Voici les 5 commandes essentielles:

### 1️⃣ Installation (2 min)
```bash
git clone https://github.com/hamxsmart10-bit/Hamx_smart.git
cd Hamx_smart
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
```

### 2️⃣ Configuration (1 min)
Éditez `.env`:
```env
EXCHANGE_NAME=binance
API_KEY=votre_clé
API_SECRET=votre_secret
EXCHANGE_SANDBOX=true  # Très important!
```

### 3️⃣ Test (1 min)
```bash
python main.py --mode=paper
```

### 4️⃣ Backtest (1 min)
```bash
python main.py --mode=backtest --start-date=2024-01-01
```

### 5️⃣ LIVE (seulement après tests!)
```bash
python main.py --mode=live
```

## 🎯 Les 3 modes expliqués simplement

| Mode | Utilisation | Risque | Commande |
|------|-----------|--------|----------|
| **PAPER** | Comprendre l'IA | ❌ Aucun | `python main.py --mode=paper` |
| **BACKTEST** | Tester stratégies | ❌ Aucun | `python main.py --mode=backtest` |
| **LIVE** | Trader réel | ⚠️ Réel argent | `python main.py --mode=live` |

## 📊 Voir les résultats

```bash
# Logs temps réel
tail -f logs/hamx_smart.log

# Dashboard web
# http://localhost:8000
```

## ❓ Questions fréquentes

**Q: Puis-je perdre de l'argent?**
- Pas avec PAPER ou BACKTEST ✅
- Oui avec LIVE, commencez petit! ⚠️

**Q: Quel exchange utiliser?**
- Binance (recommandé) ou Kraken

**Q: Comment arrêter le bot?**
- CTRL+C dans le terminal

**Q: Où sont les données?**
- `logs/` - fichiers de log
- `data/` - données historiques
- `models/` - modèles ML

---

**→ Prêt? Allez-y! 🚀**
