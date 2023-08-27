# Tech Stack
* Programming Language: Python
* Web Framework: Django
* REST Framework: Django Rest Framework -> https://www.django-rest-framework.org/
* Database: PostgreSQL
* Web Server: NGINX (Serving Static Files)
* Containerization: Docker
* Version Control: Git
* Version Control Hosting: GitHub
* API Documentation: Self Describing (Browsable) APIs Documentation, Swagger, Redoc, Postman Collection -> https://www.django-rest-framework.org/topics/documenting-your-api/
* Authentication & Authorization: JWT -> https://jwt.io/
* Views -> https://www.django-rest-framework.org/api-guide/views/
* Serializers -> https://www.django-rest-framework.org/api-guide/serializers/
* Permissions -> https://www.django-rest-framework.org/api-guide/permissions/
* Routers
* Throttling

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