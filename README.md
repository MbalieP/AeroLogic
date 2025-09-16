AeroLogic: Flight Management System
https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green
https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white
https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue
https://img.shields.io/badge/GIT-E44C30?style=for-the-badge&logo=git&logoColor=white

AeroLogic is a full-stack web application built with Django that demonstrates core backend development principles. It efficiently manages a relational database of airports and flights, showcasing a clean implementation of the Model-View-Template (MVT) architecture.

🚀 Features
Comprehensive Data Models: Define Airport and Flight entities with appropriate fields and relationships.

Relational Database Design: Implements sophisticated One-to-Many relationships using Django's ForeignKey field, linking flights to their origin and destination airports.

Django ORM Proficiency: Interact with the database using Django's Object-Relational Mapper (ORM) for all CRUD (Create, Read, Update, Delete) operations, eliminating the need for raw SQL.

Database Migrations: Utilizes Django's built-in migration system to version-control and evolve the database schema.

Dynamic Templates: Renders data dynamically to HTML using Django's templating engine.

Shell Interaction: Provides examples of creating and querying data directly from the Django shell.

🗃️ Database Schema
The application uses two main models, demonstrating a classic relational database design:

1. Airport Model
Represents an airport with the following attributes:

code (CharField): The 3-letter IATA code (e.g., "JFK").

city (CharField): The city where the airport is located.

2. Flight Model
Represents a flight between two airports with the following attributes:

origin (ForeignKey): Links to the Airport model as the departure point. Uses on_delete=models.CASCADE and has a related_name="departures".

destination (ForeignKey): Links to the Airport model as the arrival point. Uses on_delete=models.CASCADE and has a related_name="arrivals".

duration (IntegerField): The duration of the flight in minutes.

This structure allows for powerful queries, such as finding all flights departing from a specific airport.

🛠️ Installation & Setup
Follow these steps to run the project locally:

Clone the Repository

bash
git clone https://github.com/your-username/aerologic.git
cd aerologic
Create a Virtual Environment (Recommended)

bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install Dependencies

bash
pip install -r requirements.txt
Apply Database Migrations
This will create the SQLite database with the necessary tables.

bash
python manage.py makemigrations
python manage.py migrate
Run the Development Server

bash
python manage.py runserver
View the Application
Open your web browser and go to http://127.0.0.1:8000/flights/ to see the list of flights.

💻 Usage Examples
Using the Django Shell
A key feature of this project is demonstrating interaction with the ORM. You can open the Django shell with python manage.py shell and execute commands like:

python
# Import models
from flights.models import Airport, Flight

# Create new airports
jfk = Airport(code="JFK", city="New York")
jfk.save()
lhr = Airport(code="LHR", city="London")
lhr.save()

# Create a new flight linking the airport objects
f = Flight(origin=jfk, destination=lhr, duration=415)
f.save()

# Query all flights
Flight.objects.all()
# <QuerySet [<Flight: 1: New York (JFK) to London (LHR)>]>

# Query a flight's details
f.origin.city # 'New York'
f.destination.code # 'LHR'

# Use related_name for reverse lookups (Find all flights departing from JFK)
jfk.departures.all()
# <QuerySet [<Flight: 1: New York (JFK) to London (LHR)>]>
📁 Project Structure
text
aerologic/
│
├── flights/                 # Main application directory
│   ├── migrations/          # Database migration files
│   ├── templates/           # HTML templates
│   │   └── flights/
│   │       └── index.html
│   ├── __init__.py
│   ├── admin.py             # Register models for Django admin
│   ├── apps.py
│   ├── models.py            # Contains Airport and Flight models
│   ├── tests.py
│   ├── urls.py              # Application-specific URL routes
│   └── views.py             # Application logic (e.g., index view)
│
├── airline/                 # Project settings directory
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py          # Main project settings
│   ├── urls.py              # Project-wide URL routes
│   └── wsgi.py
│
├── db.sqlite3               # SQLite database (created after migrate)
└── manage.py                # Django command-line utility
🧠 Skills Demonstrated
Backend Development: Django framework, Python.

Database Management: SQL schema design, relational integrity, Foreign Keys.

Django ORM: Creating models, performing queries, managing relationships (related_name).

Migrations: Evolving a database schema using makemigrations and migrate.

Version Control: Git for project tracking.

🔮 Future Enhancements
Potential features to add:

Add a Passenger model with a Many-to-Many relationship to Flight.

Implement user authentication.

Create forms for adding new flights and airports.

Add a REST API using Django REST Framework.

Enhance the front-end with CSS/JavaScript or a modern framework.

Developed by Mbali Phulwane

This project was built for educational purposes to showcase proficiency with Django and SQL database management.

