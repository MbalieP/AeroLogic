# AeroLogic: Flight Management System

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)
![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![Git](https://img.shields.io/badge/GIT-E44C30?style=for-the-badge&logo=git&logoColor=white)

---

##  Overview
**AeroLogic** is a full-stack web application built with **Django** that demonstrates key backend development principles.  
It manages a relational database of airports and flights, highlighting a clean implementation of the **Model–View–Template (MVT)** architecture.

---

##  Features
- **Comprehensive Data Models** – Define `Airport` and `Flight` entities with appropriate fields and relationships.  
- **Relational Database Design** – Implements one-to-many relationships via Django’s `ForeignKey`, linking flights to their origin and destination airports.  
- **Django ORM Proficiency** – Perform CRUD (Create, Read, Update, Delete) operations using Django ORM without raw SQL.  
- **Database Migrations** – Manage schema evolution with Django’s built-in migration system.  
- **Dynamic Templates** – Render data to HTML using Django’s templating engine.  
- **Shell Interaction** – Create and query data directly from the Django shell.  

---

##  Database Schema

### Airport Model
- `code` *(CharField)* – The 3-letter IATA code (e.g., `JFK`).  
- `city` *(CharField)* – The city where the airport is located.  

### Flight Model
- `origin` *(ForeignKey → Airport)* – Departure airport (`related_name="departures"`).  
- `destination` *(ForeignKey → Airport)* – Arrival airport (`related_name="arrivals"`).  
- `duration` *(IntegerField)* – Duration of the flight in minutes.  

This schema allows for powerful queries, such as retrieving all flights departing from a specific airport.

---

##  Installation & Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/aerologic.git
   cd aerologic
