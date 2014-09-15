
Environment Variables

If you are using VirtualEnv, switch to VirtualEnv and then ensure the below variables are set. If not, please set this up in your `~/.bashrc`, `~/.profile` or similar.

- `export ENV=local|dev|stage|production`
  - These match the `./src/uwsgi.ini` file. You may customize that file as needed.
- `export CONFIG_DIR=/conf/`
  - Application configuration json files are read from this directory.
- `export PORT=8888`
  - Port to be used by Django or uWSGI.

Commands

- `./run.sh`
  - If no `VIRTUAL_ENV` or `./venv` is found, will attempt to create a new VirtualEnv
- `./run.sh bin/ACTION.sh`
  - `ACTION` can be one of the following: 
    - `setup.sh` - to install dependencies and create required directories etc.
    - `syncdb.sh`
    - `migrate.sh`
    - `collectstatic.sh` to agregate static files to /static/
    - `debug.sh` to use Django server
    - `start.sh` or `stop.sh` to use uWSGI
