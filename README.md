# Mandry App

Mandry App is a Django-based web application that provides a platform for travelers to share and discover new adventures. This repository contains the source code and Docker configurations necessary to get the app up and running.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Docker
- Docker Compose

### Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yurakuzo/mandry-app.git
   cd mandry-app
   ```

2. **Environment Variables:**
   - Create a `.env` file in the project root directory.
   - Copy the contents of `.env.sample` to your `.env` file and update the values accordingly.

   ```plaintext
   # .env.sample
   SECRET_KEY=your-secret-key
   DEBUG=True
   ALLOWED_HOSTS=127.0.0.1 localhost 0.0.0.0
   APP_PORT=5000
   POSTGRES_HOST=db
   POSTGRES_PORT=5432
   POSTGRES_DB=proj_db
   POSTGRES_USER=proj_usr
   POSTGRES_PASSWORD=postgres
   ```

3. **Build and Run with Docker Compose:**
   ```bash
   docker-compose up --build
   ```

   This command will build the Docker images and start the containers for the Django app, PostgreSQL database, and Nginx.

4. **Access the Application:**
   - Open your web browser and navigate to `http://localhost`.

5. **Create a Superuser:**
   - In order to access the Django admin interface, you'll need to create a superuser account.
   - The `entrypoint.sh` script creates a default superuser with username `admin` and password `admin`.
   - You can log in to the Django admin interface at `http://localhost/admin` using these credentials.

## Features

- **User Authentication:**
  - Users can sign up, log in, log out, and change their password.
  - After signing up, users are logged in automatically.

- **User Profiles:**
  - Logged in users can view their profile.

- **Main Page:**
  - A main page is available at the root URL (`/`).

## Directory Structure

- `mandry/`: Main Django project directory.
- `traveller/`: Django app for handling user authentication and profiles.
- `templates/`: HTML templates for the various views.
- `static/`: Static files such as CSS.
- `docker-compose.yml`: Docker Compose configuration file for orchestrating the containers.
- `Dockerfile`: Dockerfile for building the Django app image.
- `nginx/`: Directory containing Nginx configuration files.
- `.github/`: Directory containing GitHub Actions CI/CD workflow configurations.

## CI/CD

The project is configured with a basic GitHub Actions workflow for continuous integration and deployment. The workflow is defined in `.github/workflows/github-ci.yml`.

## Code Quality Check

We use flake8 to ensure the code adheres to PEP 8 style guide and to check for syntax errors.

**Install flake8:**

```bash
pip install flake8
```

**Run flake8:**
```bash
flake8 .
```

This command will check the code in the current directory and output any errors or warnings
