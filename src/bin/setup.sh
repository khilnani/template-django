#!/bin/sh

echo "$1"

if [ "$VIRTUAL_ENV" != "" ]; then
  echo "Run setup.sh using virtualenv: $VIRTUAL_ENV"
  if [ "$1" != "-f" ]; then
    read -p "Continue? (y/n):" yn
  fi

  if [ "$1"=="-f" ] || [ "$yn"=="y" ]; then
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
