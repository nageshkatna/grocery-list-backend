## 📘 Grocery List Backend — README.md

# Grocery List Backend

A Django REST API for managing grocery items.  
Provides CRUD endpoints for a single-family grocery list.

### Live example
http://ec2-3-99-216-136.ca-central-1.compute.amazonaws.com:8080/api/v1/groceryItems/?page=1
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
DATABASE_NAME=<your_postgres_name>
DATABASE_USER=<your_postgres_user>
DATABASE_PASSWORD=<your_postgres_password>
DATABASE_HOST=<your_postgres_host>
DATABASE_PORT=<your_postgres_port>
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

# API Endpoints

- `GET /groceryItems/` list all items
- `POST /groceryItems/` create item
- `PATCH /groceryItems/` update item to mark purchased
- `PUT /groceryItems/` update item to edit
- `DELETE /groceryItems/` delete item

### Example payload

```bash
{
  count: 2,
  current_page: 1,
  total_pages: 1,
  next: null,
  previous: null,
  results: [
    { id: "1", name: "Milk", description: "Protien Rich Milk", quantity: 2, unit: "Packs", purchased: false },
    { id: "2", name: "Bread", description: "Brown Bread", quantity: 2, unit: "Packs", purchased: false },
  ],
}
```

# Testing

- Run tests using

```bash
python manage.py test api.tests
```
