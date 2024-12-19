from typing import Any, Coroutine, Dict, Optional
from fastapi_pagination import Page
from sqlalchemy.ext.asyncio import AsyncSession
from .base import CRUDBase
from app.schemas.sensor_data import SensorData, SensorDataCreate
from app.models.sensor_data import SensorData

class CRUDSensorData(CRUDBase[SensorData, SensorDataCreate]):
    
    async def get(self, db: AsyncSession, id: str) -> SensorData:
        return await super().get(db, id)
    
    async def create(self, db: AsyncSession, defaults: Dict[str, Any] | None, **kwargs: Any) ->  SensorData:
        return await super().create(db, defaults, **kwargs)
    
    async def get_multi(self, db: AsyncSession, *, skip: int = 0, limit: int = 20) -> Page[SensorData]:
        print(f"limit {limit}")
        return await super().get_multi(db, skip=skip, limit=limit)
        
sensor_data = CRUDSensorData(SensorData)
