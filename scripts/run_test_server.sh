#!/bin/bash

source virtualenv_utils.sh
activate_virtualenv


if [ "$#" -ne 1 ]; then
  echo "Usage: $0 <PORT>" >&2
  echo "Example: $0 8000" >&2
  exit 1
fi


# django assumes that everything is run from the base directory
pushd "${BASE_DIR}"

echo 'Starting the BATS PITCH webserver in the foreground'
python manage.py runserver $1

popd
