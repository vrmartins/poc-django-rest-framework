DJANGO_CMD = python api/manage.py

clean:
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*.pyo" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf
	@find . -name ".cache" -type d | xargs rm -rf
	@rm -rf dist

migrate:
	$(DJANGO_CMD) migrate

install:
	pip install -r requirements-to-freeze.txt && \
	make migrate

runserver:
	$(DJANGO_CMD) runserver

createsuperuser:
	$(DJANGO_CMD) createsuperuser

makemigrations: clean
	$(DJANGO_CMD) makemigrations