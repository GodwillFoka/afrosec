# AfroSec — Hub Technologique Africain en Allemagne

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy)

AfroSec connecte les talents africains en Allemagne dans la cybersécurité, le Cloud, l'IA et les technologies numériques.

## Stack

- **Backend** : Django 5 + Django REST Framework
- **Frontend** : Bootstrap 5 + CSS personnalisé
- **Base de données** : PostgreSQL (prod) / SQLite (dev)
- **Hébergement** : Render.com (gratuit)

## Déploiement sur Render

1. **Forker le repo** sur GitHub
2. **Créer un compte** sur [render.com](https://render.com) (gratuit, sans CB)
3. Cliquer sur **"New +" → Web Service**
4. Connecter GitHub et sélectionner le repo
5. Render détecte automatiquement `render.yaml`
6. C'est tout ! Le site sera en ligne en 2-3 minutes

## Installation locale

```bash
git clone https://github.com/votre-compte/afrosec.git
cd afrosec
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Structure

```
afrosec/
├── core/          # Accueil, À propos, Contact
├── resources/     # Blog
├── accounts/      # Inscription membres
├── static/        # CSS, JS, images
├── templates/     # HTML
├── Dockerfile
├── render.yaml    # Config Render
└── build.sh       # Build script Render
```

## Auteur

Créé par Godwill FOKA — Initiator & Tech Ambassador @AfroSec
