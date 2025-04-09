Bookstore API

A RESTful backend for managing books, built with *FastAPI, **MySQL, and **JWT authentication*. This API allows users to register, login, and perform CRUD operations on books with filtering and search functionality.

 Tech Stack

- *FastAPI* – Web framework
- *SQLAlchemy* – ORM for MySQL
- *MySQL* – Relational database
- *Pydantic* – Data validation
- *JWT* – Authentication and access control



 Setup Instructions

1. Clone the Project

```bash
git clone https://github.com/banshitam12/bookstore.git
cd bookstore-api
2. Create a Virtual Environment
bash
Copy
Edit
python -m venv .venv
source .venv/bin/activate        # Linux/macOS
.venv\Scripts\activate           # Windows
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Configure Environment Variables
Create a .env file in the root:

env
Copy
Edit
DATABASE_URL=mysql+pymysql://<username>:<password>@localhost:3306/bookstore
SECRET_KEY=your_secret_key
ALGORITHM=HS256
5. Set Up MySQL Database
Ensure your MySQL server is running and execute:

sql
Copy
Edit
CREATE DATABASE bookstore;
6. Run the App
bash
Copy
Edit
uvicorn app.main:app --reload --port 8000
Open your browser at http://localhost:8000/docs for Swagger UI.

 Authentication
Register a User
POST /auth/signup

json
Copy
Edit
{
  "email": "user@example.com",
  "password": "string123"
}
 Login to Get Token
POST /auth/login

Send as x-www-form-urlencoded:

ini
Copy
Edit
username=user@example.com
password=string123
Response:

json
Copy
Edit
{
  "access_token": "JWT_TOKEN",
  "token_type": "bearer"
}
Use this token in Swagger UI via the Authorize button.

 Book API Endpoints
Get All Books (with filters & search)
GET /books/

Query Parameters:

author: filter by author

category: filter by category

rating: filter by rating

search: search by title

Example:

bash
Copy
Edit
/books/?author=Coelho&search=alchemist
Get a Book by ID
GET /books/{book_id}

Create a Book (Auth Required)
POST /books/

json
Copy
Edit
{
  "title": "The Alchemist",
  "author": "Paulo Coelho",
  "category": "Fiction",
  "price": 299.99,
  "rating": 4.5,
  "published_date": "1988-05-01"
}
 Update a Book (Partial Update Allowed)
PUT /books/{book_id}

json
Copy
Edit
{
  "price": 149.99
}
Only the fields you provide will be updated.

 Delete a Book
DELETE /books/{book_id}

 Filtering and Search
You can filter and search using query parameters:

bash
Copy
Edit
/books/?author=Coelho&category=Fiction&rating=4.5&search=alch
author, category, rating → optional filters

search → case-insensitive partial match on title
