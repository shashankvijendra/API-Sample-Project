# API-Sample-Project

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

