#!/bin/sh

if [ "$VIRTUAL_ENV" != "" ]; then
  echo "Running setup.sh using virtualenv: $VIRTUAL_ENV"
  read -p "Continue? (y/n):" yn

  if [ "$yn" == "y" ]; then
    pip install -r requirements.txt
    mkdir static
    mkdir logs
  else
    echo ""
    echo "Don't forget: ./run bin/setup.sh"
  fi
else
  echo "No \$VIRTUAL_ENV found"
fi
