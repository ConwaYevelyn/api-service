"""
api-service
-----------

A high-quality, scalable REST API service built with Python.

Installation
------------

To install the service, run the following command:

```bash
pip install -r requirements.txt
```

Configuration
-------------

Create a `.env` file in the root directory with the following format:

```makefile
API_PORT=8000
DB_HOST=localhost
DB_USER=your_username
DB_PASSWORD=your_password
DB_NAME=your_database
```

Run the service
---------------

To start the API service, run the following command:

```bash
python -m api_service.run
```

API Endpoints
-------------

### GET /users

Returns a list of all users.

### POST /users

Creates a new user.

### GET /users/{id}

Returns a user by ID.

### PUT /users/{id}

Updates a user by ID.

### DELETE /users/{id}

Deletes a user by ID.

API Documentation
-----------------

For detailed API documentation, visit [http://localhost:8000/docs](http://localhost:8000/docs).

Tests
-----

To run the tests, execute the following command:

```bash
pytest
```

License
-------

This project is licensed under the MIT License.