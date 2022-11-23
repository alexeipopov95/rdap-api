PORT := 8000
HOST := 127.0.0.1

run:
	python manage.py runserver $(HOST):$(PORT)

superuser:
	python manage.py createsuperuser

migrations:
	python manage.py makemigrations

migration:
	python manage.py migrate

application:
	python manage.py startapp $(NAME)