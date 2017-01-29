#!/bin/bash

if [ "$#" -ne 1 ]; then
  echo "Usage: $0 <PORT>" >&2
  echo "Example: $0 8000" >&2
  exit 1
fi


echo 'Starting the BATS webserver in the foreground'
python manage.py runserver $1
