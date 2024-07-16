# User Authentication Service

This project is a Flask-based web application that demonstrates how to implement user authentication services. The main objectives of this project are to show how to declare API routes, handle cookies, retrieve form data, and return various HTTP status codes.

## Objectives

1. **How to declare API routes in a Flask app**
2. **How to get and set cookies**
3. **How to retrieve request form data**
4. **How to return various HTTP status codes**

## Requirements

- Python 3.7+
- Flask

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/muhamedhaamdy/alx-backend-user-data.git
    cd alx-backend-user-data
    ```

2. Create a virtual environment and activate it:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Flask application:
    ```bash
    flask run
    ```

2. Access the following endpoints in your web browser or via an API client like Postman:

    - `GET /` - Welcome to the Home Page
    - `GET /login` - Login Page
    - `POST /login` - Handle login form data
    - `GET /set_cookie` - Set a cookie with the username
    - `GET /get_cookie` - Retrieve the username cookie
    - `GET /not_found` - Returns a 404 status code
    - `GET /unauthorized` - Returns a 401 status code

## Code Overview

### Declaring API Routes

In `app.py`, API routes are declared using the `@app.route` decorator. For example:

```python
@app.route('/')
def home():
    return "Welcome to the Home Page!"

