.PHONY: help install test run backtest clean lint format

help:
	@echo "Hamx_smart - Robot trader IA"
	@echo ""
	@echo "Commandes disponibles:"
	@echo "  make install    - Installer les dépendances"
	@echo "  make test       - Lancer tous les tests"
	@echo "  make test-unit  - Tests unitaires seulement"
	@echo "  make run        - Démarrer le robot en mode paper"
	@echo "  make backtest   - Lancer un backtest"
	@echo "  make lint       - Vérifier la qualité du code"
	@echo "  make format     - Formater le code"
	@echo "  make clean      - Nettoyer les fichiers générés"

install:
	pip install -r requirements.txt

test:
	pytest tests/ -v --cov=src

test-unit:
	pytest tests/unit/ -v

test-integration:
	pytest tests/integration/ -v

run:
	python main.py --mode=paper

backtest:
	python scripts/backtest.py --strategy=combined

train:
	python scripts/train_models.py

report:
	python scripts/generate_report.py --date-range=30d

lint:
	flake8 src/ tests/ --max-line-length=100

format:
	black src/ tests/ scripts/ main.py
	isort src/ tests/ scripts/ main.py

clean:
	rm -rf __pycache__ .pytest_cache .coverage htmlcov
	find . -type d -name '__pycache__' -exec rm -rf {} +
	find . -type f -name '*.pyc' -delete
