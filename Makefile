PROJECT_NAME = {{ project_name }}

default: lint test

test:
	python manage.py makemigrations --dry-run | grep 'No changes detected' || \
		(echo 'There are changes with migrations.' && exit 1)
	coverage run manage.py test
	coverage report -m --fail-under 80

lint:
	flake8

clean:
	find . -name "*.pyc" -exec rm -rf {} \;
	rm -rf {{ project_name }}/static

# Generate a random string of desired length
generate-secret: length = 32
generate-secret:
	@strings /dev/urandom | grep -o '[[:alnum:]]' | head -n $(length) | tr -d '\n'; echo

init:
	virtualenv -p `which python2.7` $(WORKON_HOME)/{{ project_name }}
	$(WORKON_HOME)/{{ project_name }}/bin/pip install -U pip wheel
	$(WORKON_HOME)/{{ project_name }}/bin/pip install -Ur requirements/development.txt
	$(WORKON_HOME)/{{ project_name }}/bin/pip freeze
	@echo ""
	@echo "workon {{ project_name }}"
	@echo "docker-compose up"
	@echo "make migrate"
	@echo "make user"
	@echo "make worker"
	@echo ""
	@echo "Dev:"
	@echo "make dev"
	@echo ""
	@echo "Prod:"
	@echo "make static"
	@echo "make start"
	@echo "make stop"
	@echo ""

delete:
	@echo "rm -rf $(WORKON_HOME)/{{ project_name }}"
	@echo "rm -rf ."

r:
	$(WORKON_HOME)/{{ project_name }}/bin/pip install -U -r requirements/development.txt

migrate:
	python manage.py makemigrations
	python manage.py migrate --run-syncdb
	python manage.py migrate

user:
	python manage.py createsuperuser

worker:
	celery -A {{ project_name }} worker -l info

dev:
	ENV=development python manage.py runserver

prod:
	ENV=production python manage.py runserver

static:
	python manage.py collectstatic

start:
	ENV=production PORT=8000 uwsgi --ini uwsgi.ini:production -H $(WORKON_HOME)/{{ project_name }}

stop:
	uwsgi --stop uwsgi.pid
