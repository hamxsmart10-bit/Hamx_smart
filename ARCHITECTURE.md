# Architecture de Hamx_smart

## Vue d'ensemble

Hamx_smart est un système modulaire de trading automatisé basé sur l'IA.

```
┌─────────────────────────────────────────────┐
│          Main Entry Point (main.py)         │
├─────────────────────────────────────────────┤
│                                             │
│  ┌──────────────────────────────────────┐  │
│  │  Trader (Exécution des ordres)       │  │
│  └──────────────────────────────────────┘  │
│           │                │                │
│           v                v                │
│  ┌──────────────┐  ┌─────────────────┐    │
│  │  Exchange    │  │ Risk Manager    │    │
│  │  Connector   │  │ (Stop-loss/TP)  │    │
│  └──────────────┘  └─────────────────┘    │
│           │                                 │
│           v                                 │
│  ┌──────────────────────────────────────┐  │
│  │  Strategies (MA, RSI, MACD, Bollinger)│ │
│  └──────────────────────────────���───────┘  │
│           │                                 │
│           v                                 │
│  ┌──────────────────────────────────────┐  │
│  │  Technical Indicators                │  │
│  └──────────────────────────────────────┘  │
│                                             │
└─────────────────────────────────────────────┘
```

## Modules Principaux

### 1. **Core (`src/core/`)**
- `exchange.py` - Connexion multi-exchange
- `trader.py` - Logique de trading
- `risk_manager.py` - Gestion des risques

### 2. **AI (`src/ai/`)**
- `indicators.py` - Indicateurs techniques
- `strategies/__init__.py` - 5 stratégies de trading

### 3. **Utils (`src/utils/`)**
- `config.py` - Configuration centralisée
- `logger.py` - Logging unifié
- `helpers.py` - Utilitaires

### 4. **Scripts (`scripts/`)**
- `backtest.py` - Backtesting complet
- `train_models.py` - Entraînement ML
- `generate_report.py` - Rapports de performance

## Flux de Données

```
1. Market Data (Exchange) 
   ↓
2. Price Processing 
   ↓
3. Indicator Calculation 
   ↓
4. Strategy Analysis 
   ↓
5. Signal Generation 
   ↓
6. Risk Validation 
   ↓
7. Order Execution 
   ↓
8. Monitoring & Logging
```

## Stratégies Disponibles

1. **MA Crossover** - Croisement de moyennes mobiles
2. **RSI** - Relative Strength Index
3. **Bollinger Bands** - Bandes de Bollinger
4. **MACD** - Moving Average Convergence Divergence
5. **Combined** - Consensus de stratégies

## Configuration

Tous les paramètres sont gérés dans `.env`:

- Exchange (API keys, sandbox mode)
- Trading (pair, position size, leverage)
- Risk (stop-loss, take-profit, max trades)
- AI (models, confidence threshold)
- Logging (level, file, rotation)

## Testing

- **Unit tests** - Tests des composants individuels
- **Integration tests** - Tests des flux complets
- **Backtesting** - Simulation sur données historiques

Couverture cible: 80%+
