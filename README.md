# Tech Stack
* Programming Language: Python
* Web Framework: Django
* REST Framework: Django Rest Framework -> https://www.django-rest-framework.org/
* Database: PostgreSQL
* Web Server: NGINX (Serving Static Files)
* Containerization: Docker -> Dockerfile, docker-compose.yml
* Version Control: Git
* Git Management -> .gitignore
* Version Control Hosting: GitHub
* API Documentation: Self Describing (Browsable) APIs Documentation, Swagger, Redoc, Postman Collection -> https://www.django-rest-framework.org/topics/documenting-your-api/
* Authentication & Authorization: JWT -> https://jwt.io/
* Package Installer -> PIP
* Dependency Management -> Virtualenv
* Dependencies -> requirements.txt
* Project Description -> README.md
* Views -> https://www.django-rest-framework.org/api-guide/views/, Function-Based Views, Class Based (APIView, Generic Views, Mixins)
* Serializers -> https://www.django-rest-framework.org/api-guide/serializers/
* Permissions -> https://www.django-rest-framework.org/api-guide/permissions/
* Routers -> https://www.django-rest-framework.org/api-guide/routers/
* Throttling -> https://www.django-rest-framework.org/api-guide/throttling/

## Tools
* black -> pip install black, black views.py
* flake8 -> pip install flake8, flake8 views.py

## How to Run
### Docker
* Docker: docker-compose up --build
### Django
  * python manage.py makemigrations
  * python manage.py migrate
  * python manage.py collectstatic
  * python manage.py createsuperuser
  * python manage.py runserver

## TODOs
* //TODO