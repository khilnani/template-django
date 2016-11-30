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
	@echo "make admin"
	@echo "make worker"
	@echo "make beat"
	@echo ""
	@echo "Dev:"
	@echo "make run"
	@echo ""
	@echo "Prod:"
	@echo "make static"
	@echo "make start"
	@echo "make stop"
	@echo ""

reset:
	rm -rf $(WORKON_HOME)/{{ project_name }} && rm -rf /tmp/postgresql-data && rm -rf /tmp/rabbitmq-mnesia

cleandb:
	rm -rf /tmp/postgresql-data

cleanq:
	rm -rf /tmp/rabbitmq-mnesia

r:
	$(WORKON_HOME)/{{ project_name }}/bin/pip install -U -r requirements/development.txt

migrate:
	python manage.py makemigrations
	python manage.py migrate --run-syncdb
	python manage.py migrate

admin:
	python manage.py createsuperuser

beat:
	# default
	# celery -A {{ project_name }} beat -s celerybeat-schedule -l info
	# django_celery_beat
	celery -A {{ project_name }} beat -l info --scheduler django

worker:
	celery -A {{ project_name }} worker -l info

worker-root:
	C_FORCE_ROOT="true" celery -A {{ project_name }} worker -l info

worker-beat:
	celery -A {{ project_name }} worker -B --scheduler django -l info

worker-beat-root:
	C_FORCE_ROOT="true" celery -A {{ project_name }} worker -B --scheduler django -l info

run:
	# ENV=development, production
	# PORT=8080
	python manage.py runserver 0.0.0.0:8080

static:
	python manage.py collectstatic

start:
	# ENV=development, production
	# PORT=8080
	# uwsgi --ini uwsgi.ini:production -H $(WORKON_HOME)/{{ project_name }}
	uwsgi --ini uwsgi.ini:production

stop:
	uwsgi --stop uwsgi.pid

flower:
	# ENV=development, production
	flower -A {{ project_name }} --port=8090 --basic_auth={{ project_name }}:{{ project_name }}
