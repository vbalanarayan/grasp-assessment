# Import the APIRouter class from FastAPI
from fastapi import APIRouter

# Import the 'sensor_data' router from the 'app.api.v1.endpoints' module
from app.api.v1.endpoints import sensor_data

# Create an instance of the APIRouter
router = APIRouter()

# Include the 'sensor_data' router as a sub-router under the '/sensor_data' prefix
router.include_router(sensor_data.router, prefix="/sensor_data", tags=["Sensor Data"])
