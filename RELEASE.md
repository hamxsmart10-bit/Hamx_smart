# 📦 Comment Créer une Release

## 🎯 Objectif
Publier une version stable de Hamx_smart sur GitHub et PyPI

## ✅ Checklist Avant Release

- [ ] Tous les tests passent: `pytest`
- [ ] Code formaté: `black src tests`
- [ ] Pas d'erreurs lint: `flake8 src`
- [ ] Types corrects: `mypy src`
- [ ] Documentation à jour: README, CHANGELOG
- [ ] Version mise à jour dans `setup.py`
- [ ] Tout commité et pushé à GitHub

## 🚀 Étapes pour Créer une Release

### 1️⃣ Mettre à jour la version

**Dans `setup.py`:**
```python
setup(
    name="hamx-smart",
    version="1.0.0",  # ← Augmentez le numéro
    ...
)
```

### 2️⃣ Mettre à jour CHANGELOG.md

Ajouter une section pour la nouvelle version avec les changements

### 3️⃣ Committer les changements

```bash
git add setup.py CHANGELOG.md
git commit -m "Release v1.0.0"
git push origin main
```

### 4️⃣ Créer un tag Git

```bash
# Créer le tag
git tag -a v1.0.0 -m "Release version 1.0.0"

# Pousser le tag
git push origin v1.0.0
```

### 5️⃣ Créer une Release sur GitHub

```bash
# Aller sur GitHub et aller à: Code → Releases → Draft a new release
# Remplir:
# - Tag version: v1.0.0
# - Release title: Release v1.0.0
# - Description: Copier depuis CHANGELOG.md
# - Attach binaries: (optionnel)
# - Publish release
```

Ou en ligne de commande:
```bash
gh release create v1.0.0 --title "Release v1.0.0" --notes "Voir CHANGELOG.md"
```

### 6️⃣ Publier sur PyPI (Optionnel)

```bash
# Installer les outils
pip install build twine

# Construire le package
python -m build

# Publier sur PyPI
twine upload dist/*
```

⚠️ **Vous devez créer un compte sur pypi.org d'abord**

## 📊 Structure des Versions

```
v1.0.0
│
├─ MAJOR (1): Changements majeurs incompatibles
├─ MINOR (0): Nouvelles fonctionnalités
└─ PATCH (0): Corrections de bugs
```

### Quand augmenter?

- **MAJOR** (1.0.0 → 2.0.0): Changement breaking
- **MINOR** (1.0.0 → 1.1.0): Nouvelle feature compatible
- **PATCH** (1.0.0 → 1.0.1): Correction de bug

## 📌 Cycle de Développement Recommandé

```
main (stable)
  ↑
  └── develop (développement)
      ├── feature/xyz (features)
      ├── bugfix/abc (corrections)
      └── hotfix/123 (urgence)
```

## 🔄 Workflow Exemple

```bash
# 1. Créer une branche
git checkout -b feature/new-indicator develop

# 2. Développer & tester
python main.py --mode=paper

# 3. Committer
git add .
git commit -m "Add new indicator"

# 4. Pull request vers develop
git push origin feature/new-indicator

# 5. Après review & tests, merger vers main
# 6. Créer la release (voir étapes ci-dessus)
```

## 📚 Ressources

- [Semantic Versioning](https://semver.org/)
- [Keeping a Changelog](https://keepachangelog.com/)
- [GitHub Releases](https://docs.github.com/en/repositories/releasing-projects-on-github/)
- [PyPI Upload](https://packaging.python.org/tutorials/packaging-projects/)

---

**Félicitations! Vous venez de créer une release! 🎉**
