#!/bin/bash
set -o errexit
set -o pipefail
set -o nounset
#python /src/backend_api/manage.py wait_for_db
python /src/manage.py migrate
python /src/manage.py runserver 0.0.0.0:8000
