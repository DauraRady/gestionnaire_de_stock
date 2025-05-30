
# 🛒 Stock Management App – Django Web Application  
👩‍💻 by **Daura RADY** | QA Engineer & Django Learner 🚀  

## 🇬🇧 English | 🇫🇷 Français

---

## 🇬🇧 Overview

A simple **inventory management web app** built with **Django**, designed to:

- ✅ Create and manage products
- 📦 Track available stock (`quantity`)
- 🔐 Use the Django Admin to manage your data
- 🌐 Display product listings on a public page

### 🔗 Live URLs (local development):

- Admin Panel → [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)  
- Product List → [http://127.0.0.1:8000/produits/](http://127.0.0.1:8000/produits/)  
- Create Company Request → [http://127.0.0.1:8000/demande-entreprise/](http://127.0.0.1:8000/demande-entreprise/)

---

## 🇬🇧 Features

- 🔧 Django 4+ & Python 3.10+
- 🗃 SQLite for quick dev setup
- 📉 Stock quantity tracking with movement logic
- ✅ Admin interface with stock overview
- 🎨 Bootstrap styling (HTML/CSS)
- 💡 Ready to expand with users, roles, and company onboarding

---

## 🇬🇧 Installation Instructions

```bash
git clone <repo_url>
cd gestion-stock
python -m venv venv
source venv/Scripts/activate  # Or 'source venv/bin/activate' on macOS/Linux
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

---

## 🇫🇷 Aperçu

Une application web Django de **gestion de stock** simple mais extensible :

- 📋 Création et suivi des produits
- 📦 Suivi des quantités disponibles
- 🔐 Interface d'administration Django intégrée
- 🌐 Affichage public des produits
- 🧩 Demandes d’inscription entreprise avec workflow d’approbation

---

## 🇫🇷 Fonctionnalités

- Django 4+ / Python 3.10+
- Base SQLite légère
- Mouvements d’entrée/sortie avec mise à jour des quantités
- Interface admin ergonomique
- Front-end responsive avec Bootstrap 5
- Prête à être enrichie : utilisateurs, rôles, exports, tableaux de bord...

---

## ✨ Author / Auteur

👩‍💻 **Daura RADY**  
QA Engineer | Automatisation | Exploratory Testing | Django Learner  
📍 France | 🔍 Passionnée par l’expérience utilisateur & la qualité produit

