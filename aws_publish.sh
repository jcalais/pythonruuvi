#!/bin/bash
# This script works on Unix-likes.
# It is designed to be callable from a crontab and will activate venv and run the aws_publish python script.

cd "$(dirname "$0")"

. venv/bin/activate
python aws_publish.py

