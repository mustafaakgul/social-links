# Tech Stack
* Programming Lang: Python
* Web Framework: Django
* REST Framework: Django Rest Framework -> https://www.django-rest-framework.org/
* Database: PostgreSQL
* Web Server: NGINX (Serve Static Files)
* Containerization: Docker
* Version Control: Git
* Version Control Hosting: GitHub
* API Documentation: Self Describing (Browsable) APIs Documentation, Swagger, Redoc, Postman Collection -> https://www.django-rest-framework.org/topics/documenting-your-api/
* Authentication & Authorization: JWT -> https://jwt.io/
* Views -> https://www.django-rest-framework.org/api-guide/views/
* Serializers -> https://www.django-rest-framework.org/api-guide/serializers/
* Permissions -> https://www.django-rest-framework.org/api-guide/permissions/
* Status Codes -> https://www.django-rest-framework.org/api-guide/status-codes/
* Routers
* Throttling

## To Do
* CI/CD: GitHub Actions
* Localization
* AWS
* Heroku
* Logging
* Caching, Redis, Memcached
* Docker Deployment
* Renderers
* Filtering
* Ordering
* Pagination
* Versioning
* Mixins
* Shell
* Testing, Selenium, JMeter, Django testing with pytest -> see localhost 5500/htmlcon see code coverage
* ElasticSearch
* https://www.django-rest-framework.org/api-guide/views/#function-based-views, API View, Generic View, Function Based
* Views / Viewsets / Generic Views / API View / Model ViewSets: Class and Function Based
* The Browsable API
* CRUD & Endpoints
* Search_fields -> url de, querystrings, queryset filter ve search
* Authentication & Authorization, OAuth, Auth Token
* Payment Gateway, Stripe, Braintree
* DB Management: Cassandra, SQL & Dynamo DB
* Configure celery and Redis : event or processes occur independly and concurrently without blocking the execution of other tasks
* Api, django, drf, https, shell scripts, UUIDS, testing, logs, token auth, nginx, docker, sync, async, git, celery, jwt, docker hub, elastic search, digital ocean, Namecheap, pytest, postman, venv, gitignore, requirements
* Code Quality -> pyproject.toml, make down, make build, make black-check, make black-diff, make black
* Django Business Logic Layer?
* api/comment/list?q=12    12. post a ait yorumlar
* Timestamped & profile models: timestamped common models, profile model, signals
* Custom User: Auth Custom User, User Manager, Auth Token
* Track, https://treblle.com/
* https://www.freecodecamp.org/news/rest-api-best-practices-rest-endpoint-design-examples/
* https://docs.microsoft.com/en-us/azure/architecture/best-practices/api-design

## Tools
* black -> pip install black, black views.py
* flake8 -> pip install flake8, flake8 views.py

## How to Run
### Docker
* Docker: docker-compose up --build
### Django
  * python manage.py makemigrations
    * python manage.py migrate
    * python manage.py runserver