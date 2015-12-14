#!/bin.bash

TIME="$(date +%Y-%m-%d)"
PYTHON="python"

$PYTHON manage.py countmodels 2>> $TIME.dat