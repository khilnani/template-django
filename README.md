
To use this Template:

- Install Django - `pip install Django==1.10.3 --upgrade`
- Create a directory for the project 'mkdir project_dir'
- Generate the project from the template:
```
django-admin startproject project_name project_dir \
  --template=https://github.com/khilnani/template-django/zipball/master \
  --extension=py,md,yml,ini \
  --name=Makefile,.coveragerc,.gitignore
```
- in the project directory, run:
  - Create Virtual Env and install dependencies - `make setup`
  - Switch to Virtual Env - `workon project_name`
  - Setup DB (sqlite3 by default) - `make migrations`
  - Admin user setup - `make user`
  - Django server
    - Development config - `make dev`
  - uWsgi server:
    - Collect static files - `make static`
    - Start - `make start`
    - Stop - `make stop`
