
To use this Template:

- Install Django - `pip install Django==1.10.3 --upgrade`
- Create a directory for the project - `mkdir -p {{ project_name }}`
- Generate the project from the template:
```
PROJECT_NAME="project_name"; mkdir $PROJECT_NAME && django-admin startproject $PROJECT_NAME $PROJECT_NAME --template=https://github.com/khilnani/template-django/zipball/master --extension=py,md,yml,ini,sh --name=Makefile,.coveragerc,.gitignore
```
- In the project directory, run:
  - Initialize the project
    - Create Virtual Env and install dependencies
    - Run - `make init`
    - Switch to Virtual Env - `workon {{ project_name }}`
  - Update settings:
    - Services:
      - Requires a running RabbitMQ, Postgres and Memcached service
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
