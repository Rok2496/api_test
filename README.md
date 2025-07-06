

## Setup

Make sure you have Python 3.8 or higher installed.
Install the dependencies:
pip install -r requirements.txt
Run the server:
uvicorn main:app --reload


The API docs will be available at http://127.0.0.1:8000/docs or http://127.0.0.1:8000/redoc

## API Endpoints

- POST /items - Create a new item
- GET /items - Get all items
- GET /items/{id} - Get a specific item
- PUT /items/{id} - Update an item
- DELETE /items/{id} - Delete an item



## Project Structure

```
main.py              - Main application file
requirements.txt     - Python dependencies
render.yaml         - Render deployment configuration
.gitignore          - Git ignore file
app/
  __init__.py       - Package initialization
  models.py         - Data models
  database.py       - In-memory database
  routers.py        - API routes
```

##  Test 
 
 test folder  -  postman testing (images)
