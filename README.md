# AeroLogic: Flight Management System

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)
![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![Git](https://img.shields.io/badge/GIT-E44C30?style=for-the-badge&logo=git&logoColor=white)

---

##  Overview
**AeroLogic** is a full-stack web application built with **Django** that demonstrates key backend development principles.  
It manages a relational database of airports and flights, highlighting a clean implementation of the **Model–View–Template (MVT)** architecture.

In this Capstone extension, AeroLogic evolves into an operations-focused tool with passenger check‑in (interactive seat map) and operations dashboards (crew/aircraft assignment and irregular-operations re‑accommodation suggestions).

---

## Distinctiveness and Complexity
AeroLogic is not an e‑commerce storefront or a social network. It focuses on airline operations, which introduces different data models, constraints, and workflows.

- Interactive, JavaScript-driven check‑in flow with seat selection and QR boarding pass generation (frontend logic beyond simple form posts).
- Operational dashboards for crew/aircraft assignment and conflict detection (time overlaps, turnaround, qualifications).
- Irregular Operations (IROPs) console to generate re‑accommodation suggestions using heuristic scoring.
- Multi-app Django architecture (`flights`, `users`, `checkin`, `ops`) with non-trivial relationships and business logic.
- Mobile-responsive UI via Bootstrap.

This scope is more complex than earlier projects: it introduces concurrent state (seat locks), scheduling constraints, and cross-model validation. The README documents the architecture and decisions to demonstrate complexity and distinctiveness.

---

## What’s in Each File/App
- `flights/`: Core domain models (`Airport`, `Flight`, `Passenger`) and existing pages.
- `checkin/`: `BoardingPass` model, check‑in view, and template stub.
- `ops/`: `IrOpsEvent`, `ReaccommodationSuggestion`, dashboard view and template stub.
- `users/`: Authentication-related views/templates (as provided).
- `airline/airline/`: Project settings and URL routing.
- `requirements.txt`: Python dependencies.

---

## How to Run
1. Create and activate a virtual environment.
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows PowerShell
   ```
2. Install dependencies.
   ```bash
   pip install -r requirements.txt
   ```
3. Apply migrations.
   ```bash
   python airline/manage.py migrate
   ```
4. Run the development server.
   ```bash
   python airline/manage.py runserver
   ```
5. Visit:
   - Flights: `/flights/`
   - Check‑in (example): `/flight/1/checkin`
   - Ops Dashboard: `/ops/`

---

## Roadmap (Capstone Milestones)
- Seat map rendering and selection with concurrency-safe locking.
- Crew/aircraft assignment UI with conflict detection rules.
- IROPs suggestions and application workflow.
- Comprehensive tests and documentation.

---

## Notes
- All dependencies are captured in `requirements.txt`.
- The project is mobile-responsive using Bootstrap (via CDN in templates; to be expanded).

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
