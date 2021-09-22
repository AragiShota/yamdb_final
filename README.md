![yamdb](https://github.com/AragiShota/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

API развернут по адресу http://84.201.135.117/api/v1/ (Только попробуй не развернуться!)
# Описание проекта
YaMDb - проект, собирающий отзывы на произведения(книги, фильмы, музыка и т.д.). 
Сами произведения в проекте не хранятся.
### Технологии
- [Django REST Framework](https://www.django-rest-framework.org/) - is a powerful and flexible toolkit for building Web APIs.
- [Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/) - a JSON Web Token authentication plugin for the Django REST Framework.
- [Python](https://www.python.org/) - is an interpreted high-level general-purpose programming language.
- [Django Framework](https://www.djangoproject.com/) - is a high-level Python Web framework that encourages rapid development and clean, pragmatic design.
- [PostgeSQL](https://www.postgresql.org/) - is an open source object-relational database system that uses and extends the SQL language combined with many features.
- [Docker](https://www.docker.com/) - is a set of platform as a service (PaaS) products that use OS-level virtualization to deliver software in packages (containers).
- [Gunicorn](https://gunicorn.org/) - is a Python WSGI HTTP Server for UNIX.
- [Nginx](https://nginx.org/) - is a web server that can also be used as a reverse proxy, load balancer, mail proxy and HTTP cache.
### Как развернуть проект (на сервере)
 - сделать fork проекта в свой аккаунт

[![](https://img.shields.io/badge/my%20project-fork!-informational?style=for-the-badge&logo=appveyor)](https://github.com/AragiShota/yamdb_final/fork)
- добавить свои данные для переменных в secrets:
```
DB_ENGINE
DB_HOST
DB_NAME
DB_PORT
DOCKER_PASSWORD
DOCKER_USERNAME
HOST
POSTGRES_PASSWORD
POSTGRES_USER
SSH_KEY
TELEGRAM_TO
TELEGRAM_TOKEN
USER
PASSPHRASE
```

- скачать репозиторий, перейти в директорию с проектом

```git clone git@github.com:ваш-логин/yamdb_final.git```
```cd /<путь-до-директории>/```

- создать виртуальное окружение, активировать его

```python3 -m venv venv```
```. venv/bin/activate```

- установить зависимости

```python -m pip install -r requirements.txt```

- сделать пуш с любым изменением в проекте

```git push```

### После каждого обновления будет осуществляться:

1. Проверка кода на соответствие стандарту PEP8 (с помощью пакета flake8) и запуск pytest из репозитория yamdb_final
2. Сборка и доставка докер-образов на Docker Hub.
3. Автоматический деплой.
4. Отправка уведомления в Telegram.
  
### Как развернуть проект (локально)
- отредактировать docker-compose.yaml
```
web:
  image: <DOCKER_USERNAME>/<DOCKER_REPO>:latest
--->

web:
  build: .
```

- собрать образ, запустить

```sudo docker build -t <задать название образа> .```

```sudo docker-compose up```

- применить миграции для приложения

```sudo docker-compose exec web python manage.py migrate --noinput```

- создать суперпользователя

```sudo docker-compose exec web python manage.py createsuperuser```

- собираем статические данные

```sudo docker-compose exec web python manage.py collectstatic --no-input```
