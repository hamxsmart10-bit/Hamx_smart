# 🚀 Guide de Déploiement

## Où déployer Hamx_smart?

### 1️⃣ Localement sur votre machine
```bash
# Parfait pour les tests et développement
python main.py --mode=paper
```

### 2️⃣ Sur un serveur VPS

**Services recommandés:**
- DigitalOcean ($5/mois)
- Linode
- AWS EC2
- Google Cloud

**Installation sur VPS:**
```bash
# 1. SSH sur le serveur
ssh root@your_server_ip

# 2. Installer Python
sudo apt update
sudo apt install python3.9 python3-venv python3-pip git

# 3. Cloner le repo
git clone https://github.com/hamxsmart10-bit/Hamx_smart.git
cd Hamx_smart

# 4. Setup
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# Éditer .env avec vos credentials

# 5. Lancer avec systemd (pour persistance)
sudo nano /etc/systemd/system/hamx-smart.service
```

**Fichier systemd:**
```ini
[Unit]
Description=Hamx Smart Trading Bot
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=/root/Hamx_smart
ExecStart=/root/Hamx_smart/venv/bin/python /root/Hamx_smart/main.py --mode=live
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

**Activer le service:**
```bash
sudo systemctl enable hamx-smart
sudo systemctl start hamx-smart
sudo systemctl status hamx-smart
```

### 3️⃣ Avec Docker

**Créer un Dockerfile:**
```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "main.py", "--mode=live"]
```

**Créer un docker-compose.yml:**
```yaml
version: '3.8'

services:
  hamx-smart:
    build: .
    environment:
      - EXCHANGE_NAME=binance
      - API_KEY=${API_KEY}
      - API_SECRET=${API_SECRET}
    volumes:
      - ./logs:/app/logs
      - ./data:/app/data
    restart: always
```

**Lancer:**
```bash
docker-compose up -d
```

### 4️⃣ Sur Heroku (FREE tier supprimé - payant maintenant)

Non recommandé pour production (coûteux et ressources limitées)

## 🔐 Sécurité

### Checklist Sécurité

- [ ] Jamais commiter `.env` (vérifier `.gitignore`)
- [ ] Utiliser des secrets GitHub Actions
- [ ] API keys en variables d'environnement
- [ ] Utiliser HTTPS pour les connections
- [ ] Activer 2FA sur votre compte GitHub
- [ ] Utiliser SSH keys au lieu de tokens
- [ ] Firewall configuré (port 8000 seulement si dashboard)

### Secrets GitHub Actions

```bash
# Ajouter des secrets via GitHub CLI
gh secret set API_KEY --body "your_api_key"
gh secret set API_SECRET --body "your_api_secret"
```

## 📊 Monitoring

### Logs
```bash
# Voir les logs
tail -f logs/hamx_smart.log

# Avec grep
grep ERROR logs/hamx_smart.log
```

### Health Check
```bash
# Vérifier que le bot est vivant
curl http://localhost:8000/health
```

## 🔄 Mises à jour

```bash
# Mettre à jour depuis GitHub
cd Hamx_smart
git pull origin main
pip install -r requirements.txt

# Redémarrer le service
sudo systemctl restart hamx-smart
```

## 🆘 Dépannage Déploiement

**Erreur: Permission denied**
```bash
sudo chmod +x venv/bin/python
```

**Erreur: Port 8000 en utilisation**
```bash
lsof -i :8000  # Voir ce qui occupe le port
kill -9 <PID>  # Tuer le processus
```

**Erreur: API connection failed**
```bash
# Vérifier les credentials
echo $API_KEY
echo $API_SECRET

# Vérifier la connexion internet
ping binance.com
```

---

**Prêt pour la production? 🚀**
