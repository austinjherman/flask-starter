#!/bin/sh

## For development
export FLASK_APP=app:app
python -m flask run --host=0.0.0.0 --port=80