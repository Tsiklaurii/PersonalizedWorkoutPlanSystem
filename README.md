# PersonalizedWorkoutPlanSystem

A simple Flask REST API for managing users, workout plans, exercises, and weight tracking.  
Includes JWT authentication, Swagger documentation, and a database seed script.

---
## Features
- Secure registration and login
- JWT access and refresh tokens for session management
- CRUD operations for workout plans
- Predefined exercises from database seed
- Track user weight over time
- Automatically populates initial exercises and sample users
- Swagger UI for easy endpoint testing and interaction
---

## ⚙️ Setup

### 1. Clone the project
```bash
git clone https://github.com/Tsiklaurii/PersonalizedWorkoutPlanSystem.git
```
### 2. Create a virtual environment & activate it
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Installing dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Initialize the database
```bash
flask init_db
flask populate_db
```

### 5. Run the Flask server
```bash
flask run
```

### 6. Access API documentation
Open your browser and go to: http://127.0.0.1:5000/