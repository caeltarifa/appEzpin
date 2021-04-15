#!/bin/bash

NAME="appEzpin"                              #Name of the application (*)
DJANGODIR=/var/www/nuclear/appEzpin             # Django project directory (*)
SOCKFILE=/var/www/nuclear/appEzpin/appEzpin.sock        # we will communicate using this unix socket (*)
USER=root                                        # the user to run as (*)
GROUP=root                                     # the group to run as (*)
ADDRESS=127.0.0.1:8002
NUM_WORKERS=1                                     # how many worker processes should Gunicorn spawn (*)
DJANGO_SETTINGS_MODULE=appEzpin.settings             # which settings file should Django use (*)
DJANGO_WSGI_MODULE=appEzpin.wsgi                     # WSGI module name (*)

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd $DJANGODIR
source /root/envNuclear/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
