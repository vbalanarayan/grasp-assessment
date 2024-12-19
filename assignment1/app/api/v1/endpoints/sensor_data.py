# Import necessary modules and components
from typing import Annotated
from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi_pagination import Page, paginate
from app.models.sensor_data import SensorData
from app.schemas.sensor_data import SensorData as SensorDataSchema, SensorDataCreate, SearchParams
from app.api.deps import get_db
from app import crud
from datetime import datetime
from typing import List
from sqlalchemy.future import select

# Create an APIRouter instance
router = APIRouter()

@router.post("/", response_model=SensorDataSchema, status_code=status.HTTP_201_CREATED)
async def create_sensor_data(
    db: Annotated[AsyncSession, Depends(get_db)],
    sensor_data_in: SensorDataCreate
):
    # Create a new sensor data record
    decoded_data = sensor_data_in.decode_data()

    # Update the sensor_data_in object with the decoded fields
    sensor_data_in.v0 = decoded_data.get("v0", sensor_data_in.v0)
    sensor_data_in.v11 = decoded_data.get("v11", sensor_data_in.v11)
    sensor_data_in.v18 = decoded_data.get("v18", sensor_data_in.v18)
    sensor_data_in.time = datetime.fromisoformat(decoded_data.get("Time", sensor_data_in.time))
    sensor_data_in_dict = sensor_data_in.dict(exclude={'data'})
    sensor_data_tuple = await crud.sensor_data.create(db=db, defaults=sensor_data_in_dict)
    sensor_data, created = sensor_data_tuple
    return SensorDataSchema.from_orm(sensor_data)

@router.get("/{id}", response_model=SensorDataSchema, status_code=status.HTTP_200_OK)
async def get_sensor_data(
    id: str,
    db: Annotated[AsyncSession, Depends(get_db)]
):
    # Get a sensor data record by ID
    sensor_data = await crud.sensor_data.get(db=db, id=id)
    if not sensor_data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sensor data not found")
    return sensor_data

@router.post("/search", response_model=List[SensorDataSchema], status_code=status.HTTP_200_OK)
async def search_sensor_data(
    db: Annotated[AsyncSession, Depends(get_db)],
    search_params: SearchParams
):
    # Extract the start_time and end_time from the request body
    start_time = search_params.start_time
    end_time = search_params.end_time
    limit = search_params.limit
    offset = search_params.offset

    # Query the sensor_data table for records between start_time and end_time with pagination
    stmt = select(SensorData).filter(
        SensorData.publish_time >= start_time,
        SensorData.publish_time <= end_time
    ).limit(limit).offset(offset)
    
    # Execute the query
    result = await db.execute(stmt)
    sensor_data_records = result.scalars().all()

    if not sensor_data_records:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No sensor data records found within the given time range"
        )

    return sensor_data_records
