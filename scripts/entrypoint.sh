#!/bin/bash
exec gunicorn --config /app/scripts/gunicorn_config.py app.wsgi:app