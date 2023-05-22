#!/bin/sh
set -e

# Start the backend server
cd /app/todo-app-backend
python3 -m gunicorn --bind 0.0.0.0:5000 app:app &

# Start the frontend server
cd /app/todo-app-frontend
npm start