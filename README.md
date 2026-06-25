# Medicare - Premium Doctor Consultation & Appointment System

Medicare is a professional, responsive, and feature-rich clinical portal built with Django. It enables patients to explore specialized medical departments, search for qualified healthcare specialists, schedule consultations online, and manage appointments via a personalized dashboard.

---

## Key Features

- **Premium Front-end Redesign**: Clean layouts using the modern **Outfit** typography system, subtle gradients, micro-animations, and glassmorphic navigation menus.
- **Dynamic Specialists Directory**: Real-time doctor search bar and department filters powered by vanilla JavaScript (no heavy libraries needed).
- **Personal Booking Dashboard ("My Bookings")**: Secure tracking of scheduled appointments. Patient data is associated directly with their registered account.
- **Safe Cancellations**: Integrated cancellation workflow including a Bootstrap confirmation modal to prevent accidental deletion of consultation slots.
- **Custom-Themed Django Admin**: Custom branded admin panel style utilizing linear gradient headers, proper columns listing, real-time search, and sidebar filters.
- **Automated Tests**: Unit tests covering permission validations, dashboard data isolation, booking constraints, and page loading states.

---

## Technology Stack

- **Framework**: Django 5.x
- **Database**: SQLite (standard development)
- **Styling**: Custom Vanilla CSS + Bootstrap 5.3 & Bootstrap Icons
- **Logic**: Vanilla JavaScript & Django ORM

---

## Directory Structure

```
django_project/
├── .venv/                   # Python Virtual Environment
├── django_project/
│   ├── db.sqlite3           # SQLite Database
│   ├── manage.py            # Django CLI Manager
│   ├── django_project/      # Root Settings and Routing Configurations
│   ├── home/                # Main Application Package
│   │   ├── static/          # Custom CSS stylesheets and assets
│   │   ├── templates/       # HTML layouts (base, booking, doctors, dashboard)
│   │   ├── admin.py         # Custom ModelAdmin views
│   │   ├── models.py        # Database models (dept, Doctors, Booking)
│   │   ├── views.py         # Business logic and user flows
│   │   ├── tests.py         # Automated unit test suite
│   │   └── urls.py          # App level routes mapping
└── README.md                # System documentation (this file)
```

---

## Setup & Running the Application

### 1. Prerequisite Environment
On Windows, activate the Python virtual environment:
```powershell
# Open terminal in root folder
.venv\Scripts\activate
```

### 2. Prepare Database & Migrations
Create and run the database migrations:
```powershell
python manage.py makemigrations
python manage.py migrate
```

### 3. Run Seed Data script
To populate the database with **14 departments** and **52 doctors** instantly, run the seed data script:
```powershell
# Run from the directory containing manage.py
python C:\Users\ashiq\.gemini\antigravity-ide\brain\e92be683-ae3f-49b0-a3bc-fa2dff9ffefd\scratch\populate_data.py
```

### 4. Start Development Server
Start the local server:
```powershell
python manage.py runserver
```
Visit the application at: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

### 5. Running Automated Unit Tests
To execute the comprehensive test suite verifying the business rules:
```powershell
python manage.py test
```

---

## Default Access Credentials

The database contains seeded user accounts for instant testing:

### **1. Administrator Account**
- **Admin Dashboard**: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
- **Username**: `admin`
- **Password**: `adminpassword123`

### **2. Patient Account**
- **Main Portal**: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **Username**: `user`
- **Password**: `userpassword123`
