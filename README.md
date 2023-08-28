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
* Authentication & Authorization: JWT -> https://jwt.io/, Other: OAuth, Auth Token, Basic Authentication, Session Authentication, Token Authentication, JWT Authentication, RemoteUserAuthentication, SessionAuthentication, CustomAuthentication
* Package Installer -> PIP
* Dependency Management -> Virtualenv
* Dependencies -> requirements.txt
* Project Description -> README.md
* LICENSE
* Views -> https://www.django-rest-framework.org/api-guide/views/, Function-Based Views (Line By Line), Class Based Views (APIView, Generic Views, Mixins)
* Generic Views & Mixins -> https://www.django-rest-framework.org/api-guide/generic-views/
* Serializers -> https://www.django-rest-framework.org/api-guide/serializers/
* Permissions -> https://www.django-rest-framework.org/api-guide/permissions/
* Routers -> https://www.django-rest-framework.org/api-guide/routers/
* Throttling -> https://www.django-rest-framework.org/api-guide/throttling/
* Filtering -> https://www.django-rest-framework.org/api-guide/filtering/, Query Params:Query String:Query Filter, Search Filter
* Pagination -> https://www.django-rest-framework.org/api-guide/pagination/

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