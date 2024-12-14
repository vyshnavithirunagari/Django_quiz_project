# Django Quiz Application

## Project Overview
This is a simple quiz application with user registration, login, and quiz functionality.

## Assumptions
1. Single user role with quiz-taking capabilities
2. Questions are pre-loaded in the database
3. Quiz consists of multiple-choice questions
4. Timer is set to 15 minutes for the entire quiz
5. User can take the quiz only once per session

## Setup and Installation

### Prerequisites
- Python 3.8+
- Django 4.2+
- pip

### Installation Steps
1. Clone the repository
2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install dependencies
```bash
pip install django
pip install django-crispy-forms
```

4. Set up the database
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create a superuser (for initial question setup)
```bash
python manage.py createsuperuser
```

6. Run the server
```bash
python manage.py runserver
```

## Features
- User Registration
- User Login
- Random Question Selection
- Quiz Timer
- Results Tracking

## Technology Stack
- Backend: Django
- Frontend: HTML, CSS, Bootstrap
- Database: SQLite (default)

## Usage Instructions
1. Register a new account
2. Login
3. Start Quiz
4. Answer questions within the time limit
5. View results after quiz completion
