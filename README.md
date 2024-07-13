# API-Sample-Project
# Overview
API-Sample-Project is a demonstration of a simple yet powerful API built using Django REST Framework (DRF). This API serves as a foundation for understanding how to build, test, and deploy RESTful services. It covers various aspects such as CRUD operations, authentication, and partial updates.

# Getting Started
These instructions will help you get started with the API-Sample-Project on your local machine for development and testing purposes.

Prerequisites
Python 3.10
Django 4.0
Django REST Framework
PostgreSQL (or another supported database)

# Installation
1. Clone the repository:
    git clone https://github.com/yourusername/API-Sample-Project.git
    cd API-Sample-Project
2. Install dependencies:
pip install -r requirements.txt

3. Run migrations:
python manage.py migrate

4. Start the development server:
python manage.py runserver

5. Access the API documentation at http://localhost:8000/api



# Fetch specific values
curl --location 'http://localhost:8000/api/task/1' \
--header 'Content-Type: application/json'

# Fetch All Values
curl --location 'http://localhost:8000/api/task' \
--header 'Content-Type: application/json'

# Post Method
curl --location 'http://localhost:8000/api/task/1' \
--header 'Content-Type: application/json' \
--data '{
    "task_for": "Testing 1th data",
    "lk_status_code":"task1"
}'

# PUT Method
curl --location --request PUT 'http://localhost:8000/api/task/1' \
--header 'Content-Type: application/json' \
--data '{
    "task_for": "Testing 1th data",
    "lk_status_code":"task1",
    "id": 1
}'

