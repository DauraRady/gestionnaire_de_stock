# 🛒 Stock Management App – Django Web Application

## 🇬🇧 English | 🇫🇷 Français

---

## 🇬🇧 Overview

This is a simple **inventory management web app** built with **Django**, where you can:

- Create and manage products
- Track available stock (`quantity`)
- Use the Django Admin panel to manage your data
- View product listings on a public page

🔗 Live URLs:

- Admin Panel: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
- Register : [http://127.0.0.1:8000/users/register/](http://127.0.0.1:8000/users/register/)
- Product List: [http://127.0.0.1:8000/produits/](http://127.0.0.1:8000/produits/)

---

## 🇬🇧 Features

- Django 4+
- SQLite database
- Stock quantity management
- Admin interface with stock preview
- Front-end styled in HTML/CSS
- Ready for expansion (clients, orders, etc.)

---

## 🇬🇧 Installation Instructions

```bash
git clone <repo_url>
cd gestion-stock
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

✨ Author / Auteur
👩‍💻 Daura RADY
QA Engineer & Django Learner 🚀
