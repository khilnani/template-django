
To use this Template:

- Install Django - `pip install Django==1.10.3 --upgrade`
- Create a directory for the project - `mkdir -p project_dir`
- Generate the project from the template:
```
django-admin startproject project_name project_dir \
  --template=https://github.com/khilnani/template-django/zipball/master \
  --extension=py,md,yml,ini,sh \
  --name=Makefile,.coveragerc,.gitignore
```
- in the project directory, run:
  - Create Virtual Env and install dependencies - `make setup`
  - Switch to Virtual Env - `workon project_name`
  - Setup DB (sqlite3 by default) - `make migrate`
  - Admin user setup - `make user`
  - Start Celery worker - `make worker`
  - Django server
    - Development config - `make dev`
  - uWsgi server:
    - Collect static files - `make static`
    - Start - `make start`
    - Stop - `make stop`
  - Urls
    - Admin
      - http://127.0.0.1:8000/admin/
      - http://127.0.0.1:8000/swagger/
    - Apis
      - http://127.0.0.1:8000/api/detail/
      - http://127.0.0.1:8000/api/task/
      - http://127.0.0.1:8000/api/task/ID
      - http://127.0.0.1:8000/api/list/ (Requires auth, create a token in the admin)n
