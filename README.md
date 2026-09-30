<div align="center">

# 🏥 Hospital Management System

### A Modern, Role-Based Web Application for Efficient Hospital Operations

<br/>

[![Project Status](https://img.shields.io/badge/Status-In%20Development-yellow?style=for-the-badge)](https://github.com/sumitrawat2417/hospital-management-system)
[![Framework](https://img.shields.io/badge/Flask-Python-blue?style=for-the-badge&logo=flask)](https://flask.palletsprojects.com/)
[![Database](https://img.shields.io/badge/SQLite-Database-lightgrey?style=for-the-badge&logo=sqlite)](https://www.sqlite.org/index.html)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5-purple?style=for-the-badge&logo=bootstrap)](https://getbootstrap.com/)
[![License](https://img.shields.io/badge/License-Academic-green?style=for-the-badge)](LICENSE)

<br/>

> Built as part of the **IIT Madras BS Degree in Data Science** — Modern Application Development 1 (MAD 1) Project

</div>

---

## 📋 Table of Contents

- [About the Project](#-about-the-project)
- [The Problem We Solve](#-the-problem-we-solve)
- [System Roles & Features](#-system-roles--features)
  - [Admin (Hospital Staff)](#️-admin-hospital-staff)
  - [Doctor](#-doctor)
  - [Patient](#-patient)
- [Technology Stack](#-technology-stack)
- [Database Schema](#-database-schema)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the App](#running-the-app)
- [API Endpoints](#-api-endpoints)
- [Key Constraints & Business Logic](#-key-constraints--business-logic)
- [Evaluation & Submission](#-evaluation--submission)
- [Author](#-author)

---

## 🌟 About the Project

The **Hospital Management System (HMS)** is a full-stack web application built with **Python (Flask)** on the backend and **HTML, CSS, Bootstrap + Jinja2** on the frontend. It uses **SQLite** as the database, making it completely self-contained and runnable on any local machine without any external database setup.

The application provides a clean, intuitive interface for three distinct user types — **Admins**, **Doctors**, and **Patients** — each with their own dedicated dashboard, access controls, and set of functionalities. All user interactions are managed through role-based authentication, ensuring data privacy and security.

This project was designed and developed from scratch as part of the **MAD 1 (Modern Application Development 1)** coursework at IIT Madras, demonstrating the practical application of web application development concepts including MVC architecture, RESTful API design, relational database modeling, and session-based authentication.

---

## 🩺 The Problem We Solve

Hospitals are complex environments that deal with enormous amounts of data every single day. Many facilities — especially smaller clinics and hospitals — still rely on:

- 📒 **Manual paper registers** for patient records
- 📞 **Phone calls** for appointment scheduling
- 🗂️ **Disconnected spreadsheets** for doctor schedules

This leads to a cascade of problems:

| Problem | Impact |
|---------|--------|
| Double-booked appointments | Frustrated patients & doctors |
| Lost patient records | Incorrect or delayed diagnosis |
| No centralized patient history | Poor quality of care |
| Manual admin overhead | Wasted staff time and resources |
| No real-time status updates | Lack of transparency for all parties |

The HMS directly addresses all of these by providing a **centralized, real-time, role-aware digital platform** for all hospital operations.

---

## 👥 System Roles & Features

The system is built around three distinct user roles. Each role has a dedicated login experience and dashboard.

### 🛡️ Admin (Hospital Staff)

The Admin is the **superuser** of the system. There is **no public registration for Admins** — the Admin account is created programmatically when the database is first initialized, ensuring full system control.

| Feature | Description |
|---------|-------------|
| 📊 **Dashboard** | Real-time stats — total doctors, patients, and appointments |
| 👨‍⚕️ **Manage Doctors** | Add new doctors, update their profiles (name, specialization, contact), and remove/blacklist them |
| 🤒 **Manage Patients** | View all registered patients, and remove/blacklist any problematic user |
| 📅 **Appointment Overview** | View all upcoming and completed appointments across the entire hospital |
| 🔍 **Search** | Search for any patient or doctor by name or specialization |

---

### 👨‍⚕️ Doctor

Doctors are added to the system by the Admin. They have their own secure login and a focused dashboard for their daily clinical work.

| Feature | Description |
|---------|-------------|
| 📅 **Personal Dashboard** | See upcoming appointments for the day and the full week at a glance |
| 👥 **Patient List** | View all patients currently assigned to them |
| ✅ **Manage Appointments** | Mark individual appointments as *Completed* or *Cancelled* |
| 🗓️ **Set Availability** | Define available time slots for the next 7 days — controls when patients can book |
| 📝 **Update Medical Records** | For completed appointments, add a detailed diagnosis, treatment plan, doctor notes, and prescriptions |
| 📜 **Patient History** | View the complete medical history of any assigned patient for informed consultation |

---

### 🤒 Patient

Patients can **self-register** on the platform. This is the public-facing side of the application designed to be simple and user-friendly.

| Feature | Description |
|---------|-------------|
| 📝 **Register & Login** | Create a personal account securely and log in |
| ✏️ **Edit Profile** | Update personal details like name, contact info, and age |
| 🔍 **Search Doctors** | Search for doctors by their name or medical specialization (e.g., "Cardiologist") |
| 📅 **Book Appointment** | View a doctor's real-time available slots for the next 7 days and book one |
| ❌ **Cancel Appointment** | Cancel an upcoming appointment directly from the dashboard |
| 📜 **Appointment History** | View all past appointments along with the doctor's diagnosis, prescriptions, and notes |
| 🩺 **Treatment Records** | Full visibility into their own medical history and treatment details |

---

## 🛠️ Technology Stack

This project strictly follows the mandatory tech stack defined in the project guidelines.

### Core (Mandatory)

| Layer | Technology | Reason |
|-------|-----------|--------|
| **Backend** | [Flask](https://flask.palletsprojects.com/) (Python) | Lightweight, flexible Python web framework |
| **Database** | [SQLite](https://www.sqlite.org/) | Serverless, file-based DB — runs anywhere |
| **ORM** | [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/) | Clean Python-to-DB model interface |
| **Templating** | [Jinja2](https://jinja.palletsprojects.com/) | Powerful templating integrated with Flask |
| **Frontend** | HTML5, CSS3, [Bootstrap 5](https://getbootstrap.com/) | Responsive, mobile-first UI framework |

### Additional (Optional / Recommended)

| Technology | Purpose |
|-----------|---------|
| `Flask-Login` | Session management & user authentication |
| `Werkzeug` | Secure password hashing |
| `Chart.js` | Visual charts/graphs on Admin dashboard |
| `Flask-RESTful` | Building structured REST API endpoints |

---

## 🗄️ Database Schema

The application uses 6 core database tables with clear relationships:

```
┌──────────┐       ┌──────────────┐       ┌───────────────┐
│  Users   │──────▶│   Doctors    │──────▶│ Appointments  │
│──────────│       │──────────────│       │───────────────│
│ id (PK)  │       │ id (PK)      │       │ id (PK)       │
│ username │       │ user_id (FK) │       │ patient_id(FK)│
│ email    │       │ dept_id (FK) │       │ doctor_id(FK) │
│ password │       │ name         │       │ date          │
│ role     │       │ specializ.   │       │ time          │
└──────────┘       │ experience   │       │ status        │
     │             └──────────────┘       └───────────────┘
     │                                          │
     ▼                                          ▼
┌──────────┐       ┌──────────────┐       ┌───────────────┐
│ Patients │       │ Departments  │       │  Treatments   │
│──────────│       │──────────────│       │───────────────│
│ id (PK)  │       │ id (PK)      │       │ id (PK)       │
│ user_id  │       │ name         │       │ appt_id (FK)  │
│ age      │       │ description  │       │ diagnosis     │
│ blood_grp│       │ doctor_count │       │ prescription  │
│ phone    │       └──────────────┘       │ notes         │
└──────────┘                              └───────────────┘
```

> **Note:** The `status` field in Appointments can be one of: `Booked`, `Completed`, or `Cancelled`.

---

## 📁 Project Structure

```
hospital-management-system/
│
├── app.py                   # App entry point — Flask app factory & config
├── models.py                # SQLAlchemy database models (all tables)
├── controllers.py           # Route handlers & business logic
│
├── templates/               # Jinja2 HTML templates
│   ├── base.html            # Base layout (navbar, footer)
│   ├── auth/
│   │   ├── login.html       # Login page (shared for all roles)
│   │   └── register.html    # Patient registration page
│   ├── admin/
│   │   ├── dashboard.html   # Admin overview dashboard
│   │   ├── doctors.html     # Doctor management page
│   │   └── patients.html    # Patient management page
│   ├── doctor/
│   │   ├── dashboard.html   # Doctor's personal dashboard
│   │   ├── appointments.html
│   │   └── patient_history.html
│   └── patient/
│       ├── dashboard.html   # Patient's personal dashboard
│       ├── search.html      # Doctor search results
│       └── book.html        # Appointment booking form
│
├── static/                  # Static assets
│   ├── css/
│   │   └── style.css        # Custom CSS styles
│   └── js/
│       └── main.js          # Custom JavaScript
│
├── requirements.txt         # All Python dependencies
└── README.md                # This file
```

---

## 🚀 Getting Started

Follow these steps to get the project running on your local machine.

### Prerequisites

Make sure you have the following installed:

- **Python 3.8+**
- **pip** (Python package manager)
- **Git**

### Installation

**1. Clone the repository:**
```bash
git clone https://github.com/sumitrawat2417/hospital-management-system.git
cd hospital-management-system
```

**2. Create and activate a virtual environment:**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

**3. Install all dependencies:**
```bash
pip install -r requirements.txt
```

### Running the App

**4. Initialize the database and start the server:**
```bash
python app.py
```

> ✅ This will automatically create the SQLite database file and seed the default **Admin** account.

**5. Open the app in your browser:**
```
http://127.0.0.1:5000/
```

**Default Admin Credentials:**
```
Username: admin
Password: admin123
```

---

## 🔌 API Endpoints

The application exposes a set of RESTful API endpoints for core resources *(to be updated as development progresses)*:

| Method | Endpoint | Role | Description |
|--------|----------|------|-------------|
| `GET` | `/api/doctors` | Admin, Patient | Get list of all doctors |
| `POST` | `/api/doctors` | Admin | Add a new doctor |
| `PUT` | `/api/doctors/<id>` | Admin | Update doctor profile |
| `DELETE` | `/api/doctors/<id>` | Admin | Remove a doctor |
| `GET` | `/api/appointments` | Admin | Get all appointments |
| `POST` | `/api/appointments` | Patient | Book a new appointment |
| `PUT` | `/api/appointments/<id>` | Doctor, Patient | Update appointment status |

---

## ⚙️ Key Constraints & Business Logic

These are the critical rules enforced within the application:

- 🚫 **No Double Booking:** The system checks for conflicts before confirming any appointment. A doctor cannot have two appointments at the same date and time.
- 🔒 **Admin Cannot Register:** The Admin account is seeded directly into the database at startup. There is no public-facing Admin registration to prevent unauthorized access.
- 📅 **7-Day Availability Window:** Doctors can only set their availability for the next 7 days. Patients can only book within this window.
- 🔄 **Status Flow:** Appointment status can only flow in one direction — `Booked → Completed` or `Booked → Cancelled`. A completed or cancelled appointment cannot be reverted.
- 🗄️ **Programmatic DB Creation:** The database schema and initial data are created entirely via code (SQLAlchemy models). No manual database setup is required.

---

## 📊 Evaluation & Submission

This project will be evaluated based on:

- ✅ Functional correctness of all three user flows (Admin, Doctor, Patient)
- ✅ Code quality and originality (plagiarism checks are performed)
- ✅ Database design (normalized ER diagram)
- ✅ Project Report (max 5 pages) including ER diagram, API docs, and AI declaration
- ✅ Video Presentation (5–10 min screencast) uploaded to Google Drive

---

## 👤 Author

**Sumit Rawat**
- 🎓 IIT Madras BS Degree in Data Science & Applications
- 💻 GitHub: [@sumitrawat2417](https://github.com/sumitrawat2417)

---

<div align="center">

⭐ **If you found this helpful, please consider starring the repository!** ⭐

*Made with ❤️ for the IIT Madras MAD 1 Project*

</div>
