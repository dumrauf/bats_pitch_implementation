#!/bin/bash

function activate_virtualenv {
    source environment_variables.sh
    source "${VIRTUALENV_LOCATION}/bin/activate"
}
