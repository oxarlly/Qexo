#!/bin/bash

# Add debugging output to check the current status
echo "Starting dependency installation..."

# Install dependencies
python3 -m pip install -r requirements.txt
if [ $? -ne 0 ]; then
  echo "Error: Failed to install dependencies."
  exit 1
fi

echo "Dependencies installed successfully."

# Migrate database
echo "Starting database migrations..."

python3 manage.py makemigrations
if [ $? -ne 0 ]; then
  echo "Error: Failed to make migrations."
  exit 1
fi

python3 manage.py migrate
if [ $? -ne 0 ]; then
  echo "Error: Failed to migrate database."
  exit 1
fi

echo "Database migrations completed successfully."

echo "Script completed successfully."
