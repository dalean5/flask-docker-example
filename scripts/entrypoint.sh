#!/bin/bash
exec gunicorn --config /app/bin/gunicorn_config.py app.wsgi:app