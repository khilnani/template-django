
To use:

- Create dir for the project 'mkdir project_name'
- Generate the project from the template:
```
django-admin startproject project_name project_name
    --template=https://github.com/khilnani/template-django/zipball/master \
    --extension=py,md,yml \
    --name=Makefile,.coveragerc,.gitignore
```
- Create an admin user: `python manage.py createsuperuser`
