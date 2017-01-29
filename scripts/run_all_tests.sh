#!/bin/bash

source virtualenv_utils.sh
activate_virtualenv


# django assumes that everything is run from the base directory
pushd "${BASE_DIR}"

echo 'Running tests in bats_pitch_web.tests'
python manage.py test -v 3 bats_pitch_web.tests

echo 'Running tests in bats_pitch.data_types.tests'
python manage.py test -v 3 bats_pitch.data_types.tests

echo 'Running tests in bats_pitch.message_types.tests'
python manage.py test -v 3 bats_pitch.message_types.tests

popd