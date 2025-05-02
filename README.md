# api-theatre-service

🎭 Theatre Service API

Welcome to the Theatre Service API! This API provides an efficient and scalable backend system for managing a theatre's plays, performances, tickets, reservations, and users. The service supports both authenticated and unauthenticated users, with endpoints that allow interaction with various theatre data, such as plays, performances, actors, tickets, and reservations.

🚀 Features

Play and Performance Management: Manage plays, actors, genres, and performances.
Ticket Reservations: Allow users to book tickets for performances.
Authentication: Secure endpoints for users to make reservations and manage tickets.

📚 Table of Contents
Installation
Usage
API Endpoints
API Documentation
Testing
Contributing
License

💻 Installation
Prerequisites
Make sure you have the following installed:
Python 3.8 or higher
Django 3.x or above
Django Rest Framework (DRF)
SQLite or PostgreSQL (database)

Steps to Install
1. Clone the repository:
git clone https://github.com/weuis/api-theatre-service.git
cd theatre-service-api 
2. Set up a virtual environment:
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
3. Install dependencies:
pip install -r requirements.txt
4. Run migrations to set up the database:
python manage.py migrate
5. Create a superuser for the admin interface (optional):
python manage.py createsuperuser
6. Start the development server:
python manage.py runserver
The API should now be accessible at http://localhost:8000.

🛠 Usage

Authentication
For authenticated endpoints, you need to log in as a user. You can create a user through the admin interface or by calling the /auth/register/ and /auth/login/ endpoints (if implemented).

API Endpoints
Public Endpoints (No Authentication Required)

GET /public/plays/ – List all plays.
GET /public/performances/ – List all performances.
GET /public/genres/ – List all genres.
GET /public/actors/ – List all actors.
GET /public/theatrehalls/ – List all theatre halls.
Authenticated Endpoints (Requires Authentication)

POST /authenticated_only/reservations/ – Create a reservation.
POST /authenticated_only/tickets/ – Create a ticket.
GET /authenticated_only/reservations/ – View all reservations.
GET /authenticated_only/tickets/ – View all tickets.

Testing

The project uses Django’s testing framework along with DRF's test tools. To ensure the system is working as expected, you can run the tests included in the project.

Running Tests
Ensure your environment is activated and dependencies are installed.
Run the tests with:
python manage.py test
This will execute all tests located in the tests/ directory.

👥 Contributing

We welcome contributions to this project! To get started, follow these steps:

Fork this repository.
Create a new branch for your feature or bugfix.
Implement your changes and write tests.
Make sure all tests pass before submitting a pull request.
Please follow the PEP 8 guidelines and ensure that your code is well-documented.

🔧 Technologies Used

Django - Framework for web development.
Django Rest Framework (DRF) - Toolkit for building APIs in Django.
SQLite - Database used in development (you can switch to PostgreSQL in production).
Python 3.8+ - Programming language used.

Thank you for checking out the Theatre Service API! We hope it serves your theatre management needs efficiently.
