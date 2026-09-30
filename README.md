# 🏥 Hospital Management System (HMS)

![Project Status](https://img.shields.io/badge/Status-In%20Development-yellow)
![Framework](https://img.shields.io/badge/Framework-Flask-blue)
![Database](https://img.shields.io/badge/Database-SQLite-lightgrey)

A comprehensive, role-based Hospital Management System web application built with Python (Flask) and SQLite. This project is being developed as part of the IIT Madras BS Degree program (MAD 1 Project).

## 📖 About the Project

Hospitals require efficient systems to manage patients, doctors, appointments, and medical treatments. Many facilities still rely on manual registers or fragmented software, leading to scheduling conflicts, data loss, and inefficient tracking of patient history.

This **Hospital Management System (HMS)** solves these problems by providing a unified, web-based platform that allows different users to interact with the system based on their specific roles, ensuring smooth operations and reliable data management.

## ✨ Core Features & Roles

The system is designed around three primary user roles:

### 🛡️ Admin (Hospital Staff)
* **Centralized Dashboard**: View overall hospital statistics (total doctors, patients, appointments).
* **Doctor Management**: Add, update, and manage doctor profiles and specializations.
* **Patient Management**: Monitor registered patients and manage system access.
* **Appointment Overview**: View all upcoming and past hospital appointments.
* *(Note: Admin accounts are securely pre-configured during system initialization.)*

### 👨‍⚕️ Doctor
* **Personalized Dashboard**: View assigned patients and daily/weekly schedules.
* **Availability Management**: Set available time slots for the upcoming 7 days.
* **Consultation Management**: Mark appointments as 'Completed' or 'Cancelled'.
* **Medical Records**: Access patient history and update treatment details, including diagnoses, notes, and prescriptions.

### 🤒 Patient
* **Self-Service Portal**: Register, log in, and manage personal profiles securely.
* **Find a Doctor**: Search for doctors by name or medical specialization.
* **Seamless Booking**: View a doctor's availability and book appointments. The system automatically prevents scheduling conflicts.
* **Medical History**: Access a complete history of past appointments, treatments, and prescriptions.

## 🛠️ Technology Stack

This project strictly adheres to the following core technologies to ensure a lightweight and robust architecture:

* **Backend Engine:** Flask (Python)
* **Database:** SQLite (with SQLAlchemy)
* **Frontend Design:** HTML5, CSS3, Bootstrap 5
* **Templating:** Jinja2

## 🚀 Local Setup & Installation

*(Instructions for setting up the virtual environment, initializing the database, and running the Flask server will be updated here as development progresses.)*

## 📜 License & Credits

Developed by Sumit Rawat for the IITM BS Degree program.
