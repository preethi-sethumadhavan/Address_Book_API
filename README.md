# Address Book API (FastAPI)

## Overview

This project implements a **minimal Address Book REST API** using **FastAPI** and **SQLite**.
The API allows users to create, update, delete, and retrieve addresses along with their geographic coordinates.

Additionally, the API provides functionality to **retrieve addresses within a specified distance from given latitude and longitude coordinates**.

FastAPI automatically generates interactive API documentation using **Swagger UI**, making it easy to test the endpoints.

---

## Features

* Create a new address
* Update an existing address
* Delete an address
* Retrieve all saved addresses
* Store address coordinates (latitude and longitude)
* Validate input using Pydantic
* Retrieve addresses within a specified distance from coordinates
* SQLite database storage
* Logging for API operations
* Interactive Swagger API documentation

---

## Technologies Used

* Python
* FastAPI
* SQLAlchemy
* SQLite
* Pydantic
* Uvicorn

---

## Project Structure

```
Address_Book_API
│
├── app
│   ├── main.py        # FastAPI application and API endpoints
│   ├── database.py    # Database connection configuration
│   ├── models.py      # SQLAlchemy database models
│   ├── schemas.py     # Pydantic request/response schemas
│   ├── crud.py        # CRUD database operations
│   └── utils.py       # Utility functions (distance calculation)
│
├── requirements.txt   # Project dependencies
├── README.md          # Project documentation
└── .gitignore         # Files ignored by Git
```

---

## Installation

### 1. Clone the Repository

```
git clone https://github.com/preethi-sethumadhavan/Address_Book_API.git
```

```
cd Address_Book_API
```

---

### 2. Create a Virtual Environment

```
py -3.11 -m venv venv
```

---

### 3. Activate the Virtual Environment

```
venv\Scripts\activate
```

---

### 4. Install Dependencies

```
pip install -r requirements.txt
```

---

## Running the Application

Start the FastAPI server using:

```
uvicorn app.main:app --reload
```

The server will start at:

```
http://127.0.0.1:8000
```

---

## API Documentation

FastAPI automatically generates interactive documentation.

Open the following URL in your browser:

```
http://127.0.0.1:8000/docs
```

From this interface you can:

* Create addresses
* Update addresses
* Delete addresses
* Retrieve stored addresses
* Search nearby addresses

---

## Example API Request

### Create Address

Endpoint:

```
POST /addresses
```

Example request body:

```
{
  "name": "Home",
  "street": "MG Road",
  "city": "Bangalore",
  "latitude": 12.9716,
  "longitude": 77.5946
}
```

---

## Nearby Address Search

Endpoint:

```
GET /addresses/nearby
```

Example query parameters:

```
lat=12.97
lon=77.59
distance=5
```

This returns addresses within **5 km** of the specified coordinates.

---

## Logging

The application uses Python’s built-in **logging module** to log important operations such as:

* Address creation
* Address updates
* Address deletion
* Nearby address searches

---

## Database

The application uses **SQLite** as the database.

The database file is automatically created when the application runs:

```
addresses.db
```

---

## Review Considerations

This project follows several best practices:

* Modular project structure
* Separation of concerns (models, schemas, CRUD logic)
* Input validation using Pydantic
* Logging implementation
* RESTful API design
* Automatic API documentation using FastAPI Swagger
* SQLite database integration

---

## Author

Developed as part of a FastAPI assignment to demonstrate backend development skills using Python and FastAPI.
