---

## 📘 Grocery List Backend — README.md

```markdown
# Grocery List Backend

A Django REST API for managing grocery items.  
Provides CRUD endpoints for a single-family grocery list.

---

## Features

- Create, edit, delete grocery items
- Mark items as purchased
- Duplicate item validation
- RESTful API with JSON responses
- Dockerized for easy setup

---

## Tech Stack

- [Django](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [PostgreSQL](https://www.postgresql.org/) (via Docker)
- [pytest](https://docs.pytest.org/) for testing

---

## Setup

### Local development

```bash
git clone https://github.com/nageshkatna/grocery-list-backend.git
cd grocery-list-backend
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### Environment File

- Create a `.env` file and add

```bash
DJANGO_SECRET_KEY=your-secret
DB_URL=postgres://postgres:postgres@db:5432/postgres
ALLOWED_HOSTS=localhost,127.0.0.1
CORS_ALLOWED_ORIGINS=http://localhost:3000
```

### Docker

- Use docker to run the containers

```bash
cd docker
docker-compose up -d
```

This will start:

- Django backend (port 8000)
- PostgreSQL database (port 5432)

# Testing

- Run tests using

```bash
python manage.py test api.tests
```
