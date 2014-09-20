#!/bin/sh

if [ "$VIRTUAL_ENV" != "" ]; then
  echo "Using virtualenv: $VIRTUAL_ENV"
  source $VIRTUAL_ENV/bin/activate
elif [ -d ../venv ]; then
  echo "Using virtualenv: ../venv"
  source ../venv/bin/activate
else
  read -p "No virtualenv found. Create a virtualenv? (y/n):" yn
  if [ "$yn" == "y" ]; then 
    virtualenv ../venv
    source ../venv/bin/activate
    ./bin/setup.sh
    echo ""
    echo "If no errors occured, please repeat your prior command"
  else
    echo "Please setup env \$VIRTUAL_ENV and then run: $0 bin/setup.sh"
    fi
  exit 1
fi

if [ -z "$ENV" ]; then
  echo "No ENV found"
  exit 1
else
  echo "Using ENV: $ENV"
fi

if [ -z "$PORT" ]; then
  echo "No PORT found"
  exit 1
else
  echo "Using PORT: $PORT"
fi

if [ -z "$CONFIG_DIR" ]; then
  echo "No CONFIG_DIR found"
  exit 1
else
  echo "Using CONFIG_DIR: $CONFIG_DIR"
fi

if [ "$#" -lt 1 ]; then
  echo "USAGE: $0 ./bin/ACTION.sh   eg. $0 ./bin/setup.sh"
  echo "USAGE: $0 COMMAND           eg. $0 python manage.py validate"
  exit 1
fi

export DJANGO_SETTINGS_MODULE=api.settings
export CONFIG_URL=file://$CONFIG_DIR/$ENV.json

${@}
