# Employee Management System

A Flask-based Employee Management Portal built as a hands-on DevOps learning project.

The goal of this project was not only to build a web application but also to learn how applications move through the complete DevOps lifecycle:

Development → Version Control → Containerization → CI/CD → Cloud Deployment

---

## Features

* Add Employees
* View Employees
* Delete Employees
* Dashboard with Employee Count
* Responsive UI
* SQLite Database
* Automatic Database Initialization

---

## Technology Stack

### Frontend

* HTML
* CSS

### Backend

* Python
* Flask

### Database

* SQLite

### DevOps Tools

* Git
* GitHub
* Docker
* GitHub Actions

### Cloud Platform

* Microsoft Azure
* Ubuntu Linux Virtual Machine

---

## Project Architecture

Developer
↓
Git
↓
GitHub Repository
↓
GitHub Actions (CI)
↓
Docker Build
↓
Azure Linux VM
↓
Docker Container
↓
Employee Management Portal

---

## DevOps Concepts Implemented

### Version Control

* Git
* GitHub

### Containerization

* Docker
* Dockerfile

### Continuous Integration (CI)

* GitHub Actions workflow
* Automatic Docker image build on push

### Cloud Deployment

* Azure Linux Virtual Machine
* SSH Connectivity
* Docker Deployment
* Network Security Group Configuration

---

## Running Locally

Clone the repository:

```bash
git clone <your-repository-url>
cd employee-management-system
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

Open:

```text
http://localhost:5000
```

---

## Running With Docker

Build the image:

```bash
docker build -t employee-portal .
```

Run the container:

```bash
docker run -d -p 5000:5000 employee-portal
```

Open:

```text
http://localhost:5000
```

---

## CI Pipeline

The project uses GitHub Actions.

Every push to the main branch automatically:

1. Checks out the repository
2. Builds the Docker image
3. Verifies the application can be built successfully

---

## Azure Deployment

The application has been deployed to:

* Azure Virtual Machine
* Ubuntu Server
* Docker Container

Deployment process:

1. Create Azure VM
2. Connect using SSH
3. Install Docker
4. Clone GitHub Repository
5. Build Docker Image
6. Run Container
7. Configure Network Security Group
8. Access Application via Public IP

---

## Future Improvements

* Edit Employee Functionality
* Docker Composee
* Environment Variables
* Azure Container Registry (ACR)
* Automated CD Pipeline
* Azure Container Apps
* Azure App Service Deployment

---

## Learning Objectives

This project was built to gain practical experience with:

* Application Deployment
* Docker
* GitHub Actions
* Azure Virtual Machines
* Linux Administration
* CI/CD Fundamentals

---

## Author

Muzammil

DevOps & Cloud Learning Project
