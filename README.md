# Social Link Project

# Technology Stack - Backend, DevOps
# Github: https://github.com/features/, https://docs.github.com/en
* Programs: Chrome, Discord, Figma, Postman, Slack, Trello
* Cloud Platform: Digital Ocean App Platform
* IDE: PyCharm -> https://www.jetbrains.com/pycharm/
* Admin Panel: Django Admin, Postman
* Programming Language: Python
* Web Framework: Django
* REST Framework: Django Rest Framework -> https://www.django-rest-framework.org/
* Database: Relational PostgreSQL, NoSQL MongoDB, DynamoDB
* Web Server: NGINX (Serving Static Files)
* Containerization: Docker -> Dockerfile, docker-compose.yml
* Version Control: Git
* Git Management -> .gitignore
* Version Control Hosting: GitHub
* API Documentation: Self Describing (Browsable) APIs Documentation, Swagger, Redoc, Postman Collection -> https://www.django-rest-framework.org/topics/documenting-your-api/
* Authentication & Authorization: JWT -> https://www.django-rest-framework.org/api-guide/authentication/, https://jwt.io/, Claims
  * Other: OAuth2, Auth Token, Basic Authentication, Session Authentication, Token Authentication, JWT Authentication, RemoteUserAuthentication, SessionAuthentication, CustomAuthentication
* Package Installer -> PIP
* Dependency Management -> Virtualenv
* Protecting Resources -> .env by Local, Dev, Prod
* Dependencies -> requirements.txt
* Project Description -> README.md
* LICENSE
* Project Management -> Makefile
* Shell -> python manage.py shell
* Accounts -> Custom User: Auth Custom User, User Manager
* Common Models
* Views -> https://www.django-rest-framework.org/api-guide/views/, Function-Based Views (Line By Line), Class Based Views (APIView, Generic Views, Mixins)
* Generic Views & Mixins -> https://www.django-rest-framework.org/api-guide/generic-views/
* Serializers -> https://www.django-rest-framework.org/api-guide/serializers/
* Permissions -> https://www.django-rest-framework.org/api-guide/permissions/
* Caching -> Redis, Memcached, https://www.django-rest-framework.org/api-guide/caching/
* Routers, Rate Limiting -> https://www.django-rest-framework.org/api-guide/routers/
* Throttling -> https://www.django-rest-framework.org/api-guide/throttling/
* Filtering -> https://www.django-rest-framework.org/api-guide/filtering/, Query Params:Query String:Query Filter, Search Filter
* Pagination -> https://www.django-rest-framework.org/api-guide/pagination/
* Versioning -> https://www.django-rest-framework.org/api-guide/versioning/, https://gearheart.io/articles/api-versioning-with-django-rest-framework/
* Status Codes -> https://www.django-rest-framework.org/api-guide/status-codes/
* Internationalization and Localization -> https://www.django-rest-framework.org/api-guide/internationalization/, https://docs.djangoproject.com/en/4.2/topics/i18n/
* Configuring Celery and RabbitMQ or Redis -> event or processes occur independently and concurrently without blocking the execution of other tasks (async)
* Searching -> ElasticSearch
* Payment Gateway, Stripe, Braintree, Native Bank Integration, Iyzico
* Domain -> Namecheap
* Testing -> TDD, Pytest, Code Coverage -> https://realpython.com/test-driven-development-of-a-django-restful-api/
* Tracking, Logging -> https://treblle.com/, (Application Performance Monitoring & Error Tracking), https://sentry.io/for/django/, https://develop.sentry.dev/serializers/, https://docs.sentry.io/product/, https://docs.sentry.io/platforms/python/guides/django/
* Monitoring -> Prometheus, Grafana
* Deployment -> AWS, Docker Deployment
* CI/CD -> GitHub Actions
* Seeders & Fixtures -> python manage.py loaddata seeds/tags/tags.json
* Use Custom Response Model -> return Response(
                                                    {
                                                        "status": "success",
                                                        "message": "Tag created successfully",
                                                        "errors": None,
                                                        "data": serializer.data
                                                    },
                                                    status=status.HTTP_200_OK
                                                )
* Exception Handler, Error Handling -> https://www.django-rest-framework.org/api-guide/exceptions/, https://medium.com/turkcell/request-validation-and-custom-exception-handling-in-django-rest-framework-649fddecb415

# Technology Stack - Frontend
* Language -> JavaScript
* Framework -> React
* State Management -> Redux
* UI Framework -> Material UI
* UI Components -> React Bootstrap
* UI Design -> Figma
* AI -> Locofy
* IDE -> WebStorm - https://www.jetbrains.com/webstorm/
* .env By Local, Dev, Prod
* .gitignore
* Package Installer -> NPM

# Technology Stack - Mobile
* Language -> JavaScript
* Framework -> React, React Native
* State Management -> Redux
* Mobile Platform -> Expo to iOS, Android
* Design -> Figma
* AI -> Locofy
* IDE -> WebStorm - https://www.jetbrains.com/webstorm/
* .env By Local, Dev, Prod
* .gitignore

# Technology Stack - Project Management
* Project Management -> Trello
* Project Management Approach -> Agile in Trello
* Agile Framework -> Scrum, Kanban
* Agile Methodology -> Sprint
* Agile Ceremonies -> Sprint Planning, Daily Scrum, Sprint Review, Sprint Retrospective
* Agile Artifacts -> Product Backlog, Sprint Backlog, Burndown Chart
* Agile Roles -> Product Owner, Scrum Master, Development Team
* Communication -> Discord, Slack
* Notification -> Slack
* File Sharing -> Google Drive
* Documentation -> Notion
* Design & Boards -> Figma
* Version Control -> Git
* Githost -> GitHub

## About Product
Link in Profile Apps like linktr.ee(admin), linkme, heylink

## Design Samples
* https://www.figma.com/community/file/1187422022288947321/devlinks-projeto-discover
* https://www.figma.com/community/file/1279164071673230245/linktree-ui-free-ui-kit-recreated
* https://www.figma.com/community/file/1140170887273934289/links-ui-design
* https://www.figma.com/community/file/1289786610304060562/cardu
* https://www.figma.com/community/file/1192950040338521792/figtree-social-links
* https://www.figma.com/community/file/846568099968305613/littlelink-template
* https://www.figma.com/community/file/867431645276958703/build-a-link-in-bio-for-free-community
* https://www.figma.com/community/file/1135234747622451930/personal-linktree
* https://www.figma.com/community/file/1063388536323425656/social-network-app-freebies

## Features
* Health Check

## Sources
### Core
* https://hevodata.com/learn/rest-api-best-practices/
* https://swagger.io/resources/articles/best-practices-in-api-design/
* https://medium.com/deliveryherotechhub/rest-api-tasar%C4%B1m%C4%B1-ve-best-practices-37ea7041b27
* https://dev.to/ksaaskil/tips-for-building-a-clean-rest-api-in-django-2pae
* https://django-best-practices.readthedocs.io/en/latest/code.html
* https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/coding-style/
* https://www.toptal.com/django/django-top-10-mistakes
* https://learning.oreilly.com/library/view/django-design-patterns/9781788831345/08d91bf0-986c-415c-9120-1b7e908d7aec.xhtml
* https://cheatsheetseries.owasp.org/cheatsheets/Django_REST_Framework_Cheat_Sheet.html
* https://profil-software.com/blog/development/10-things-you-need-know-effectively-use-django-rest-framework/
* https://stackoverflow.blog/2020/03/02/best-practices-for-rest-api-design/
* https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design
* https://www.freecodecamp.org/news/rest-api-best-practices-rest-endpoint-design-examples/
* https://document360.com/blog/api-design-best-practices/
* https://josipmisko.com/posts/rest-api-best-practices
* https://www.softkraft.co/how-to-build-rest-api-with-django/
* https://www.mindbowser.com/best-practices-for-rest-api-design/
### Github
* https://github.com/saqibur/django-project-structure
* https://github.com/HackSoftware/Django-Styleguide
* https://github.com/Joabsonlg/django-api-template
* https://gist.github.com/TechRancher/6440451a05797d8e1c61642347ca6b69
* https://github.com/PragatiVerma18/Django-For-APIs/blob/master/Best-Practices-In-REST.md
* https://github.com/cunhaax/django-rest-template
* https://github.com/weynelucas/drf-project-template
* https://github.com/rephus/django-rest-template
* https://github.com/xionglilong/django-rest-framework-template
* https://github.com/asapdevelopers/django-rest-framework-template
* https://github.com/Keats/django-drf-template
* https://github.com/bitnob/django-rest-template
* https://github.com/juanbenitezdev/django-rest-framework-crud
* https://github.com/ArchTaqi/django-rest-api
* https://github.com/ukjin1192/django-rest-framework-example
### Samples
* https://medium.com/@ebin7joseph/django-rest-framework-authentication-with-jwt-8687494509d8
* https://blog.logrocket.com/django-rest-framework-create-api/
* https://python.plainenglish.io/building-in-the-update-functionality-with-django-rest-framework-60c3f0436927
* https://levelup.gitconnected.com/restful-django-django-rest-framework-8b62bed31dd8
* https://medium.com/analytics-vidhya/10-must-have-tips-of-django-rest-framework-to-increase-your-coding-efficiency-87ebea0e0099
* https://www.rootstrap.com/blog/django-best-practices-and-beginner-tips
* https://djangostars.com/blog/rest-apis-django-development/
* https://medium.com/crowdbotics/how-to-write-an-api-in-3-lines-of-code-with-django-rest-framework-59b0971edfa4
* https://articles.wesionary.team/preparing-your-django-application-for-production-key-considerations-and-best-practices-6125386df748

## Best Practices
* Use Django & DRF Business Logic Layer (Services) to test better
* Use Layers Presentation Layer (Views), Business Logic Layer (Services), Data Access Layer (Models)
* Use Custom Response Model
* Client-Server Architecture
* Ensure that the API scales
* Use an international design standard The OpenAPI v3
* Cacheable -> Caching Responses -> Cache frequently requested API responses to improve performance and reduce the load on your server. DRF supports various caching strategies that can be easily integrated.
* Stateless
* Use Nouns Instead of Verbs in Endpoints -> https://mysite.com/posts not https://mysite.com/createPost
* Don't use POST: /articles/createNewArticle/ Do use POST: /articles/
* Name Collections with Plural Nouns -> So, instead of https://mysite.com/post/123, it should be https://mysite.com/posts/123, GET /cars/123, POST /cars, GET /cars
* Use Status Codes in Error Handling -> Informational Responses, Redirects, Client-side errors, Server-side errors
* Use Nesting on Endpoints to Show Relationships and Nested Serializers and Related Data -> https://mysite.com/posts/postId/comments, You should avoid nesting that is more than 3 levels deep as this can make the API less elegant and readable
    * /users // list all users
    * /users/123 // specific user
    * /users/123/orders // list of orders that belong to a specific user
    * /users/123/orders/0001 // specific order of a specific users order list
* Use Filtering, Sorting, and Pagination to Retrieve the Data Requested -> https://mysite.com/posts?sortBy=createdAt&sortOrder=desc&limit=10&offset=0
* Use SSL for Security -> https://mysite.com/posts
* Return Error Details in the Response Body -> 
    {
    "error": "Invalid payload.",
    "detail": {
        "surname": "This field is required."
    }
}
* Provide Accurate API Documentation -> Documentation with Swagger and API Docs for API Consumers
  * The documentation should contain:
    * relevant endpoints of the API
    * example requests of the endpoints
    * implementation in several programming languages
    * messages listed for different errors with their status codes
* Tests should cover all API endpoints, be sure to use mock to mock external API calls, Be sure to include tests that cover all possible error conditions, Write comprehensive unit tests using DRF’s testing tools to validate the functionality of your API endpoints. Test-driven development (TDD) ensures a robust and bug-free API.
* Check that valid data is returned for 201 or 200 responses, make sure the proper error codes/messages are being returned for 4xx responses
* Use exception handling and custom response model
* Response message with status codes { ‘status’:’success|error’, ‘data’:{ 'result':{} || [] , '' }, 200 OK — Success — GET/PUT — return resource/status message 201 Created — Success — POST — provide status message or return newly created object 204 No Content — Success — DELETE 304 Unchanged — Redirect — ALL — Indicates no changes since last request 400 Bad Request — Failure — GET/PUT/POST — invalid request, return error messages 401 Unauthorized — Failure — ALL — missing credentials/Authentication required 403 Forbidden — Failure — ALL — restricted content 404 Not Found — Failure — Resource not found 405 Method Not Allowed Failure — Failure — ALL — An invalid HTTP method was attempted
* Versioning Your APIs -> https://mysite.com/v2 for version 2, Implement API versioning from the beginning to ensure backward compatibility as your API evolves. DRF provides easy-to-use tools for versioning, allowing you to handle changes gracefully.
* Validation and Error Handling -> DRF provides comprehensive validation tools to ensure data integrity. Handle errors gracefully and provide meaningful error responses to API consumers.
* Optimizing Database Queries -> Avoid the N+1 query problem by using DRF’s queryset optimization techniques like select_related and prefetch_related to minimize database queries.
* Use UUIDS for Primary Keys -> Use UUIDs instead of auto-incrementing integers for primary keys to avoid exposing internal IDs to API consumers.

### Business Logic Layer (Services)
* https://emcarrio.medium.com/business-logic-in-a-django-project-a25abc64718c
* https://jairvercosa.medium.com/business-logic-in-django-projects-7fe700db9b0a
* https://breadcrumbscollector.tech/how-to-implement-a-service-layer-in-django-rest-framework/
* https://dev.to/ksaaskil/tips-for-building-a-clean-rest-api-in-django-2pae
* https://sunscrapers.com/blog/where-to-put-business-logic-django/
* https://forum.djangoproject.com/t/where-to-put-business-logic-in-django/282/10
* https://aliashkevich.com/business-logic-in-django-rest-framework-applications/
* https://stackoverflow.com/questions/30197637/django-rest-framework-business-logic
* https://www.youtube.com/watch?v=t6qbY_Z02tk

## Structure
myproject_website/
├── commands/
├── db_backups/
├── mockups/
├── src/
│   └── django-myproject/
│       ├── externals/
│       │   ├── apps/
│       │   │   └── README.md
│       │   └── libs/
│       │       └── README.md
│       ├── locale/
│       ├── media/
│       ├── myproject/
│       │   ├── apps/
│       │   │   ├── core/
│       │   │   │   ├── __init__.py
│       │   │   │   └── versioning.py
│       │   │   └── __init__.py
│       │   ├── settings/
│       │   │   ├── __init__.py
│       │   │   ├── _base.py
│       │   │   ├── dev.py
│       │   │   ├── production.py
│       │   │   ├── sample_secrets.json
│       │   │   ├── secrets.json
│       │   │   ├── staging.py
│       │   │   └── test.py
│       │   ├── site_static/
│       │   │   └── site/
│       │   │  django-admin.py startproject myproject     ├── css/
│       │   │       │   └── style.css
│       │   │       ├── img/
│       │   │       │   ├── favicon-16x16.png
│       │   │       │   ├── favicon-32x32.png
│       │   │       │   └── favicon.ico
│       │   │       ├── js/
│       │   │       │   └── main.js
│       │   │       └── scss/
│       │   │           └── style.scss
│       │   ├── templates/
│       │   │   ├── base.html
│       │   │   └── index.html
│       │   ├── __init__.py
│       │   ├── urls.py
│       │   └── wsgi.py
│       ├── requirements/
│       │   ├── _base.txt
│       │   ├── dev.txt
│       │   ├── production.txt
│       │   ├── staging.txt
│       │   └── test.txt
│       ├── static/
│       ├── LICENSE
│       └── manage.py
└── env/

## Code Quality Tools
* black -> pip install black, black views.py
* flake8 -> pip install flake8, flake8 views.py

## How to Run
### Docker
* Docker: docker-compose up --build, docker-compose -f docker-compose.dev.yml up --build
    * docker exec -it name_of_container pytest -rP -vv
#### DEV
* Build the Docker image -> docker build -t nodeme .
* Push the Docker image to a container registry -> 
    * aws ecr get-login-password --region us-west-2 | docker login --username AWS --password-stdin aws_account_id.dkr.ecr.eu-central-1.amazonaws.com
    * docker tag my-django-app:latest aws_account_id.dkr.ecr.us-west-2.amazonaws.com/my-django-app:latest
    * docker push aws_account_id.dkr.ecr.us-west-2.amazonaws.com/my-django-app:latest
* Create an Elastic Beanstalk environment -> 
    * eb init -p docker my-django-app --region us-west-2
    * eb create my-django-app-env --instance-type t2.micro --region us-west-2
* Step 5: Deploy your Django application to Elastic Beanstalk -> eb deploy

### Django
#### Local
  * python manage.py makemigrations
  * python manage.py migrate
  * python manage.py collectstatic
  * python manage.py createsuperuser
  * python manage.py runserver

#### DEV in AWS Elastic Beanstalk
* deactivate
* eb --version
* eb init --region eu-central-1 -p python-3.11 nodeme-backend
* eb init
* eb create nodeme-backend-env
* eb logs
* eb status -> CNAME in allowed_host
* git commit -am "commit message", git push
* eb deploy -> to deploy any changes, for instance changed allowed_host
* eb open
* To save instance hours and other AWS resources between development sessions, terminate your Elastic Beanstalk environment with eb terminate ->eb terminate nodeme-backend-env
* eb console
* eb ssh

## TODOs
* //TODO