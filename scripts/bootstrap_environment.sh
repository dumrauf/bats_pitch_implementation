#!/bin/bash

source environment_variables.sh

echo "Step 1: Installing 'virtualenv'..."
pip install virtualenv
echo "...done"


echo "Step 2: Creating the virtualenv for 'bats_pitch_implementation'..."
mkdir -p "${VIRTUALENV_DIR}"
pushd "${VIRTUALENV_DIR}"
virtualenv "${VIRTUALENV_NAME}"
popd
echo "...done"


echo "Step 3: Installing all site-packages in the 'bats_pitch_implementation' virtualenv..."
source "${VIRTUALENV_LOCATION}/bin/activate"
pip install -r "${BASE_DIR}/requirements.txt"
echo "...done"

echo "All Steps completed successfully."
