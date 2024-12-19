# Sensor_Data_API
This application handles ingestion and serving of sensor data.

- Clone the project to your local repository.
- To run the project follow the steps below.

## Environment variables
Create a .env in the project root directory from .env.example file 
The .env should have the following sample variables and values.
```
POSTGRES_HOST=products_db
POSTGRES_USER=username
POSTGRES_PASSWORD=password
POSTGRES_DATABASE=database
POSTGRES_PORT=5432
ASYNC_DATABASE_URI=postgresql+asyncpg://username:password@products_db:5432/database
PROJECT_NAME=Product Listings
```
You can change the values as you see fit.
## Building the project
Assuming you have docker installed, run the command below:
```yaml
docker-compose -f docker-compose.yml up -d
```

The command will build the images and start the docker images instances (containers).

To access the API, open your browser and paste the following URL:
```
http://localhost:8000/docs
```
