# Django Todolist

## Creating Environment in Python

```bash
python -m venv env
env\Scripts\activate
```

## Installing Django and create a project

```bash
pip install django
django-admin startproject todolist
```

## Running Django

```bash
python manage.py runserver
```

## Creating an app

```bash
python manage.py startapp todo
```

## In settings.py should add these folder names

`todolist/setting.py`

### To add static files

```py
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
```

### To add apps

```py
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "todo",
]
```

### To add templates

```py
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["templates"],      # here
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]
```
