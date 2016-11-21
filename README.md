
To use this Template:

- Install Django - `pip install Django==1.10.3 --upgrade`
- Create a directory for the project - `mkdir -p {{ project_name }}`
- Generate the project from the template:
```
django-admin startproject {{ project_name }} {{ project_name }} \
  --template=https://github.com/khilnani/template-django/zipball/master \
  --extension=py,md,yml,ini,sh \
  --name=Makefile,.coveragerc,.gitignore
```
- In the project directory, run:
  - Initialize the project
    - Create Virtual Env and install dependencies
    - Run - `make init`
    - Switch to Virtual Env - `workon {{ project_name }}`
  - Update settings:
    - Defaults:
      - DB - sqlite3 by default
      - Cache - file by default
    - Services:
      - Requires a running RabbitMQ service
      - Update settings to Postgress/Memcached if using included docker compose
  - Setup the App
    - Update DB schema - `make migrate`
    - Admin user setup - `make user`
  - Start the App
    - Common:
      - Start Celery worker - `make worker`
      - Start Celery schedular - `make beat`
    - Development:
      - `make dev`
    - Production:
      - Collect static files - `make static`
      - Start - `make start`
      - Stop - `make stop`
- Urls
  - Admin
    - http://127.0.0.1:8000/admin/ - Use user/pass created earlier
    - http://127.0.0.1:8000/swagger/ - API browser
  - Apis
    - http://127.0.0.1:8000/api/detail/ - Mock, No Auth
    - http://127.0.0.1:8000/api/list/ - Mock, with Token Auth created in the Admin
    - http://127.0.0.1:8000/api/task/ - Run a task
    - http://127.0.0.1:8000/api/task/ID - Fetch the task result
