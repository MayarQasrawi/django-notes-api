# Django Notes API

A simple **Note Keeping REST API** built with **Django REST Framework**.
It allows users to create, read, update, delete, and search notes.

---

## 🚀 Features

* Create, read, update, delete (CRUD) notes
* Each note has a **title, content, and creation date**
* Search notes by title or content (`/notes/search/?query=...`)
* Pagination for listing notes
* Django REST Framework browsable API

---

## 🛠 Tech Stack

* **Django 4.2+**
* **Django REST Framework**
* **SQLite / PostgreSQL** (default is SQLite, easy to swap to Postgres)
* **Python Decouple** for `.env` management (optional)

---

## ⚙️ Setup Instructions

1. **Clone the repository**

   ```bash
   git clone https://github.com/MayarQasrawi/django-notes-api.git
   cd notekeeping
   ```

2. **Create virtual environment & activate**

   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Start the server**

   ```bash
   python manage.py runserver
   ```

---

## 📌 API Endpoints

| Method | Endpoint                    | Description                   |
| ------ | --------------------------- | ----------------------------- |
| GET    | `/notes/`                   | List all notes (paginated)    |
| POST   | `/notes/`                   | Create a new note             |
| GET    | `/notes/{id}/`              | Get a note by ID              |
| PUT    | `/notes/{id}/`              | Update a note completely      |
| PATCH  | `/notes/{id}/`              | Update a note partially       |
| DELETE | `/notes/{id}/`              | Delete a note                 |
| GET    | `/notes/search/?query=TEXT` | Search notes by title/content |

---

## 🔑 Example Note Object

```json
{
  "id": 1,
  "title": "Shopping List",
  "content": "Buy milk, eggs, and bread",
  "created_at": "2025-09-20T14:30:00Z"
}
```

---

## 📖 Notes

* By default, pagination returns **5 notes per page**. You can change it in `settings.py`.
* The browsable API is enabled → visit endpoints in your browser to test easily.

---
