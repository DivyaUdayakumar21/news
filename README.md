Django Newspaper App
A full-stack web application where users can publish articles and comment on each other's posts. Built with Django, deployed to production.
Live Demo
→ View the live app https://news-8u3v.onrender.com/articles/1/

Features

Custom user model — extends Django's AbstractUser with age and occupation fields
Article management — authenticated users can create, read, update, and delete their own articles
Comments — users can comment on any article; handled via a clean SingleObjectMixin + FormView pattern
Authorization — only the author of an article can edit or delete it (UserPassesTestMixin)
Authentication — login, logout, and signup with custom registration form
Admin panel — articles display inline comments; full CRUD via Django admin


Tech Stack
LayerTechnologyBackendPython 3, Django 4DatabasePostgreSQL (production), SQLite (development)AuthDjango AbstractUserDeployment[Render]

Getting Started
Prerequisites

Python 3.10+
pip

Installation
bash# 1. Clone the repo
git clone https://github.com/DivyaUdayakumar21/news.git
cd news

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up environment variables
cp .env.example .env
# Edit .env and fill in SECRET_KEY and DATABASE_URL

# 5. Apply migrations
python manage.py migrate

# 6. Create a superuser (optional)
python manage.py createsuperuser

# 7. Run the development server
python manage.py runserver
Then visit http://127.0.0.1:8000.

Project Structure
├── accounts/          # Custom user model, signup view, auth forms
├── articles/          # Article + Comment models, views, forms
├── pages/             # Static pages (home)
├── templates/         # All HTML templates
├── static/            # CSS, JS, images
└── config/            # Project settings and root URLs

Running Tests
bashpython manage.py test
Tests cover:

Custom user model creation (regular and superuser)
Signup page URL, view, and form submission


What I Learned

Implementing a custom user model from scratch using AbstractUser
Combining SingleObjectMixin with FormView to handle GET and POST in a detail view without duplicating logic
Enforcing object-level permissions with UserPassesTestMixin
Deploying a Django app with a production database


Potential Improvements

 Pagination for the article list
 Search and filter articles
 User profile pages
 Like / upvote system
 Expanded test coverage for article and comment views
 Environment variable management via python-decouple
