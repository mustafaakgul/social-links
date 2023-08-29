server:
	python manage.py runserver
worker:
	python -m celery -A project_name worker --loglevel info
beat:
	python -m celery -A project_name beat --loglevel info

migrate:
	python manage.py migrate