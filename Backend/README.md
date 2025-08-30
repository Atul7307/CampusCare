# CampusCare API

Django REST Framework API with custom user roles, JWT auth, and dj-rest-auth/allauth.

## Quick start (local)

1. Create venv and install deps
```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```
2. Configure env vars (PowerShell example)
```
$env:DJANGO_DEBUG = "true"
$env:DJANGO_ALLOWED_HOSTS = "127.0.0.1,localhost"
```
3. Migrate and run
```
python manage.py migrate
python manage.py runserver 127.0.0.1:8000
```

## Deployment

- Build an environment with Python 3.12+
- Set environment variables (examples):
```
$env:DJANGO_DEBUG = "false"
$env:DJANGO_SECRET_KEY = "<strong-secret>"
$env:DJANGO_ALLOWED_HOSTS = "api.example.com"
$env:DB_ENGINE = "django.db.backends.postgresql"
$env:DB_NAME = "campuscare"
$env:DB_USER = "postgres"
$env:DB_PASSWORD = "<password>"
$env:DB_HOST = "127.0.0.1"
$env:DB_PORT = "5432"
$env:CORS_ALLOWED_ORIGINS = "https://app.example.com"
$env:CSRF_TRUSTED_ORIGINS = "https://app.example.com"
$env:SECURE_SSL_REDIRECT = "true"
```
- Install deps and collect static files
```
pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate
```
- Run with a process manager (gunicorn/uvicorn+daphne) behind Nginx with HTTPS.

## Endpoints
- `GET /` health + API index (index only shown when DEBUG=true)
- Auth: `POST /api/auth/login/`, `POST /api/auth/registration/`, `POST /api/auth/token/refresh/`, `POST /api/auth/token/verify/`
- App: `GET /api/me/`, `GET /api/me/student_area/`, `GET /api/me/counsellor_area/`, `GET /api/me/admin_area/`

## Notes
- Custom user with role is stored in `auth_user` table.
- Admin accounts only via Django admin.
- Email verification is mandatory when `DEBUG=false`.
