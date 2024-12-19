# Sensor_Data_API
This application handles ingestion and serving of sensor data.

- Clone the project to your local repository.
- To run the project follow the steps below.

## Environment variables
Create a .env in the project root directory from .env.example file 
The .env should have the following sample variables and values.

You can change the values as you see fit. Please use the values in the subsequent database setup and migration step
## Building the project
Assuming you have docker installed, run the command below:
```yaml
docker-compose -f docker-compose.yml up -d
```

The command will build the images and start the docker images instances (containers).

# Database Setup & Migrations Guide

The following instructions for setting up the PostgreSQL database and running migrations using Alembic.

### Commands

Run the below commands in the Postgres docker container

```bash
docker ps
```
```bash
docker exec it <CONTAINER ID> /bin/bash
```

1. **Connect to PostgreSQL**  
To connect to PostgreSQL using the `psql` command line tool:
    ```bash
    psql -U username
    ```

2. **Create a New Database**  
To create a new database, run the following SQL command:
    ```sql
    CREATE DATABASE database;
    ```

3. **Set a Password for the User**  
To change the password of the PostgreSQL user, run:
    ```sql
    ALTER ROLE username WITH PASSWORD 'password';
    ```

4. **Grant All Privileges**  
Grant all privileges on the newly created database to the user:
    ```sql
    GRANT ALL PRIVILEGES ON DATABASE database TO username;
    ```

### Migrations

Run the below commands in the application (sensor_api) container

1. **Run Alembic Migrations**  
To apply migrations and bring your database schema up to date, run the following Alembic command:
    ```bash
    alembic upgrade head
    ```

This command will create the necessary tables.

### Notes

- Replace `username`, `password`, and `database` with your actual PostgreSQL credentials and database name.
- Ensure that the PostgreSQL server is running and accessible before executing these commands.

To access the API, open your browser and paste the following URL:
```
http://localhost:8000/docs
```
