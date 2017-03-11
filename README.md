
To use this Template:

- Install Django - `pip install Django==1.10.3 --upgrade`
- Generate the project from the template
  - Creates a new directory
  - Replace `project_name`
  ```
PROJECT_NAME="project_name"; mkdir $PROJECT_NAME && django-admin startproject $PROJECT_NAME $PROJECT_NAME --template=https://github.com/khilnani/template-django/zipball/master --extension=py,md,yml,ini,sh --name=Makefile,.coveragerc,.gitignore
  ```

- Manual / Ubuntu
  - Ubuntu dependencies:
    - Run - `apt-get install -y build-essential libpq-dev python-dev postgresql-server-dev-all`
  - Initialize the project
    - Create Virtual Env and install dependencies
    - Run - `make init`
    - Switch to Virtual Env - `workon {{ project_name }}`
  - Update settings:
    - Services:
      - Requires a running RabbitMQ, Postgres and Memcached service
- Docker
  - Use docker compose to start up needed services and python dependencies already setup
    - `docker-compose up`
  - Check the `Makefile` for docker specific shortcuts for psql, ssh into containers etc.
- Setup DB
    - Update DB schema - `make migrate`
    - Admin user setup - `make admin`
- Run the App
  - Common:
    - Start Celery worker - `make worker`
    - Start Celery schedular - `make beat`
    - Export `ENV=development` or `ENV=production`
    - Export `PORT=8080`
  - Development:
    - `make run`
  - Production:
    - Collect static files - `make static`
    - Start - `make start`
    - Stop - `make stop`
- Urls
  - Admin
    - http://127.0.0.1:8080/admin/ - Use user/pass created earlier
    - http://127.0.0.1:8080/swagger/ - API browser
  - Apis
    - http://127.0.0.1:8080/api/detail/ - Mock, No Auth
    - http://127.0.0.1:8080/api/list/ - Mock, with Token Auth created in the Admin
    - http://127.0.0.1:8080/api/task/ - Run a task
    - http://127.0.0.1:8080/api/task/ID - Fetch the task result
