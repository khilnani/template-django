
Environment Variables

If you are using virtualenv, switch to virtualenv and then ensure the below variables are set. If not, please set this up in your `~/.bashrc`, `~/.profile` or similar.

- `export ENV=local|dev|stage|production`
  - These match the `./src/uwsgi.ini` file. You may customize that file as needed.
- `export CONFIG_DIR=/conf/`
  - Application configuration json files are read from this directory.
- `export PORT=8888`
  - Port to be used by Django or uWSGI.

Commands

> If you get an error like [: Unexpected operator, use `bash run.sh ...`

- `./run.sh`
  - If no `$VIRTUAL_ENV` or `./venv` is found, will attempt to create a new virtualenv
- `./run.sh COMMAND` if you know the command to run. This will setup the env variables and run your command
  - eg. `./run.sh python manage.py validate`
- `./run.sh bin/ACTION.sh`
  - `ACTION` can be one of the following: 
    - `setup.sh` - to install dependencies and create required directories etc.
    - `syncdb.sh`
    - `migrate.sh`
    - `collectstatic.sh` to agregate static files to /static/
    - `debug.sh` to use Django server
    - `start.sh` or `stop.sh` to use uWSGI
