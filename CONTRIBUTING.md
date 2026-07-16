# Guide de Contribution à Hamx_smart

## Comment contribuer?

### 1. Fork et Clone
```bash
git clone https://github.com/YOUR_USERNAME/Hamx_smart.git
cd Hamx_smart
```

### 2. Créer une branche
```bash
git checkout -b feature/ma-feature
```

### 3. Développer
- Respectez le code style (black, flake8)
- Ajoutez des tests pour votre code
- Documentez vos changements

### 4. Tester
```bash
make lint
make format
make test
```

### 5. Commit et Push
```bash
git commit -m "feat: description de la fonctionnalité"
git push origin feature/ma-feature
```

### 6. Pull Request
Ouvrez une PR avec une description claire de vos changements.

## Standards de Code

- **Langue**: Python 3.9+
- **Formattage**: Black
- **Linting**: Flake8
- **Type hints**: Requis pour les nouvelles fonctions
- **Tests**: Coverage minimum 80%
- **Docstrings**: Format Google

## Types de Contributions

- 🐛 **Bug fixes** - Corrections de bugs
- ✨ **Features** - Nouvelles fonctionnalités
- 📚 **Documentation** - Amélioration de la doc
- 🧪 **Tests** - Amélioration de la couverture de tests
- ♻️ **Refactoring** - Amélioration du code

## Questions?

Ouvrez une issue pour discuter de vos idées!
