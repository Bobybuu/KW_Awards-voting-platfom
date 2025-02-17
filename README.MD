# README.md file for for voting platform project  
# Django Project Setup

This is a Django project using PostgreSQL as the database.

## Requirements

- Python 3.x
- Django 3.x
- PostgreSQL

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Bobybuu/KW_Awards-voting-platfom.git
    cd KW_Awards-voting-platfom/backend
    ```

2. **Create a virtual environment:**

    ```bash
    python --version 
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up PostgreSQL:**

### Install PostgreSQL

#### On Windows

- Download the installer from the PostgreSQL Downloads page.
- Run the installer and follow the setup wizard.
- Set a password for the PostgreSQL superuser (default user is `postgres`).
- Choose the port number (default is 5432).

#### On macOS

1. Install Homebrew
2. Update Homebrew:

    ```bash
    brew update
    ```

3. Install PostgreSQL:

    ```bash
    brew install postgresql
    ```

4. Start PostgreSQL:

    ```bash
    brew services start postgresql
    ```

#### On Linux

1. Update the package list:

    ```bash
    sudo apt update
    ```

2. Install PostgreSQL and its contrib package:

    ```bash
    sudo apt install postgresql postgresql-contrib
    ```

3. Start PostgreSQL:

    ```bash
    sudo systemctl start postgresql
    ```

4. Enable PostgreSQL to start on boot:

    ```bash
    sudo systemctl enable postgresql
    ```

### Create a Database and a User for the Project

1. Switch to the PostgreSQL user:

    ```bash
    sudo -i -u postgres
    ```

2. Access the PostgreSQL prompt:

    ```bash
    psql
    ```

3. Create a database and a user for the project:

    ```sql
    CREATE DATABASE yourdbname; -- Create the database
    CREATE USER yourdbuser WITH PASSWORD 'yourpassword'; -- Create the user
    ALTER ROLE yourdbuser SET client_encoding TO 'utf8'; -- Set the encoding
    ALTER ROLE yourdbuser SET default_transaction_isolation TO 'read committed'; -- Set the transaction isolation level
    ALTER ROLE yourdbuser SET timezone TO 'UTC'; -- Set the timezone
    GRANT ALL PRIVILEGES ON DATABASE yourdbname TO yourdbuser; -- Grant privileges to the user on the database
    \l -- List all your databases
    \c yourdbname -- Connect to your database
    CREATE EXTENSION IF NOT EXISTS "uuid-ossp"; -- Create the uuid-ossp extension
    \du -- List all your users and their privileges
    ```

4. Exit the PostgreSQL prompt:

    ```sql
    \q
    ```

5. **Configure the database in :**

    Edit your  file to include the following:

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.getenv('votingplatform'),
            'USER': os.getenv('test'),
            'PASSWORD': os.getenv('giddy254'),
            'HOST': os.getenv('localhost'),
            'PORT': os.getenv('5432'),
        }
    }
    ```

6. **Apply migrations:**

    ```bash
    python manage.py migrate
    ```

7. **Create a superuser:**

    ```bash
    python manage.py createsuperuser
    ```

8. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

## Usage

- Access the admin site at `http://127.0.0.1:8000/admin/`

## Working with Git Branches

1. **Create a new branch:**

    ```bash
    git checkout -b your-branch-name
    ```

    ```bash
    git branch --set-upstream-to=origin/main <branch-name>  # If tracking main
    ```

2. **update from main after branch checkout**

   ```bash
   git pull origin main

   ```

3. **Make your changes and commit them:**

    ```bash
    git add .
    git commit -m "Your commit message"
    ```

4. **Push your branch to the remote repository:**

    ```bash
    git push origin your-branch-name
    ```

5. **Create a pull request:**

    Go to the repository on GitHub and create a pull request from your branch.

6. **Merge the pull request:**

    Once your pull request is reviewed and approved, it can be merged into the main branch.
