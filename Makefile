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

setup:
	virtualenv -p `which python2.7` $(WORKON_HOME)/{{ project_name }}
	$(WORKON_HOME)/{{ project_name }}/bin/pip install -U pip wheel
	$(WORKON_HOME)/{{ project_name }}/bin/pip install -Ur requirements/development.txt
	$(WORKON_HOME)/{{ project_name }}/bin/pip freeze
	echo "DJANGO_SETTINGS_MODULE={{ project_name }}.settings" > .env
	@echo
	@echo "workon {{ project_name }}"
	@echo "If postgres:"
	@echo "createdb {{ project_name }} -U {{ project_name }} -W -h 127.0.0.1"
	@echo
	@echo "If memcached:"
	@echo "sudo apt-get install memcached"
	@echo
	@echo "If RabbitMQ:"
	@echo "rabbitmqctl add_user {{ project_name }} {{ project_name }}"
	@echo "rabbitmqctl add_vhost {{ project_name }}"
	@echo "rabbitmqctl set_permissions -p {{ project_name }} {{ project_name }} '.*' '.*' '.*'"

	@echo


update:
	$(WORKON_HOME)/{{ project_name }}/bin/pip install -U -r requirements/development.txt

migrations:
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
	ENV=production PORT=8000 uwsgi --ini uwsgi.ini:production -H $(WORKON_HOME)/{{ project_name }}

stop:
	uwsgi --stop uwsgi.pid
