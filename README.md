# News Management System

A full-stack web application where users can publish and manage news articles with role-based access control. Built with Django and deployed on Render.

## Live Demo

[**→ View the live app**](https://news-8u3v.onrender.com/articles/1/)

**GitHub:** [github.com/DivyaUdayakumar21/news](https://github.com/DivyaUdayakumar21/news.git)

---

## Features

- **Custom user model** — extends Django's `AbstractUser` with additional fields
- **Role-based access control** — admin and editor roles using Django session handling
- **Article management** — authenticated users can create, read, update, and delete articles
- **Comments** — users can comment on articles via a clean `SingleObjectMixin` + `FormView` pattern
- **Authorization** — only the author of an article can edit or delete it (`UserPassesTestMixin`)
- **Authentication** — login, logout, and signup with custom registration form
- **Admin panel** — articles display inline comments; full CRUD via Django admin

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python 3, Django 4 |
| Database | PostgreSQL (production), SQLite (development) |
| Auth | Django `AbstractUser` |
| Deployment | Render |

---

## API Endpoints

| Method | URL | Description | Auth required |
|---|---|---|---|
| GET | `/articles/` | List all articles | Yes |
| GET | `/articles/<id>/` | View article detail | Yes |
| POST | `/articles/<id>/` | Post a comment | Yes |
| GET | `/articles/<id>/edit/` | Edit an article | Author only |
| GET | `/articles/<id>/delete/` | Delete an article | Author only |
| GET | `/articles/new/` | Create a new article | Yes |
| GET | `/accounts/signup/` | User registration | No |

---

## Getting Started

### Prerequisites
- Python 3.10+
- pip

### Installation

```bash
# 1. Clone the repo
git clone https://github.com/DivyaUdayakumar21/news.git
cd news

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Apply migrations
python manage.py migrate

# 5. Create a superuser (optional)
python manage.py createsuperuser

# 6. Run the development server
python manage.py runserver
```

Then visit `http://127.0.0.1:8000`.

---

## Running Tests

```bash
python manage.py test
```

Tests cover:
- Custom user model creation (regular and superuser)
- Signup page URL, view, and form submission

---

## Project Structure

```
├── accounts/          # Custom user model, signup view, auth forms
├── articles/          # Article + Comment models, views, forms
├── pages/             # Static pages (home)
├── templates/         # All HTML templates
├── static/            # CSS, JS, images
└── config/            # Project settings and root URLs
```

---

## Key Design Decisions

**Custom user model** — extending `AbstractUser` from the start is best practice. Allows flexibility to add fields without database restructuring later.

**SingleObjectMixin + FormView** — combining these two mixins handles GET and POST in the article detail view cleanly without duplicating logic across two separate views.

**UserPassesTestMixin** — enforces object-level permissions so only the article author can edit or delete their own content.

---

## How this differs from my Blog API project

This is a full-stack project with server-rendered templates, session-based authentication, and a comment system. My [Blog REST API](https://github.com/DivyaUdayakumar21/blogapi) focuses purely on API design with DRF, ViewSets, custom permissions, and Swagger documentation.

---

## What I Learned

- Implementing a custom user model from scratch using `AbstractUser`
- Combining `SingleObjectMixin` with `FormView` to handle GET and POST in a detail view without duplicating logic
- Enforcing object-level permissions with `UserPassesTestMixin`
- Deploying a Django app with a production database on Render

---

## Potential Improvements

- [ ] Pagination for the article list
- [ ] Search and filter articles
- [ ] User profile pages
- [ ] JWT authentication for API access
- [ ] Expanded test coverage for article and comment views
- [ ] Environment variable management via `python-decouple`

---

## License

MIT
