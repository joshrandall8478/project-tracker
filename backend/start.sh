#!/bin/sh
mkdir db
python3 init_db.py
flask --app api run --host 0.0.0.0