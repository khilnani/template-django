PROJECT_NAME = console

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
	rm -rf console/static

# Generate a random string of desired length
generate-secret: length = 32
generate-secret:
	@strings /dev/urandom | grep -o '[[:alnum:]]' | head -n $(length) | tr -d '\n'; echo

setup:
	virtualenv -p `which python2.7` $(WORKON_HOME)/console
	$(WORKON_HOME)/console/bin/pip install -U pip wheel
	$(WORKON_HOME)/console/bin/pip install -Ur requirements/development.txt
	$(WORKON_HOME)/console/bin/pip freeze
	echo "DJANGO_SETTINGS_MODULE=console.settings" > .env
	@echo
	@echo "workon console"
	@echo "createdb console -U console -W -h 127.0.0.1"
	@echo "python manage.py migrate"
	@echo

worker:
	celery -A console worker -l info

update:
	$(WORKON_HOME)/console/bin/pip install -U -r requirements/development.txt

migrate:
	python manage.py makemigrations
	python manage.py migrate --run-syncdb
	python manage.py migrate

user:
	python manage.py createsuperuser

dev:
	ENV=development python manage.py runserver

prod:
	ENV=production python manage.py runserver

static:
	python manage.py collectstatic

start:
	ENV=production PORT=8000 uwsgi --ini uwsgi.ini:production -H $(WORKON_HOME)/console

stop:
	uwsgi --stop uwsgi.pid
