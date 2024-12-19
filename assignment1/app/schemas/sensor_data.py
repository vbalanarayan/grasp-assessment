import base64
import json
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class SensorDataBase(BaseModel):
    message_id: str = Field(..., description="Message id")
    publish_time: datetime = Field(..., description="Publish time in ISO8601 format")
    v0: str = Field(..., description="Sensor value 0")
    v11: str = Field(..., description="Sensor value 11")
    v18: str = Field(..., description="Sensor value 18")
    time: datetime = Field(..., description="Time in ISO8601 format")

class SensorDataCreate(SensorDataBase):
    message_id: str
    publish_time: datetime
    v0: str = None
    v11: str = None
    v18: str = None
    time: datetime = None
    data: str  # base64 encoded field

    def decode_data(self):
        # Decode base64 to bytes, then convert to UTF-8 string
        decoded_bytes = base64.b64decode(self.data)
        decoded_str = decoded_bytes.decode('utf-8')

        # Parse the decoded string into a dictionary
        try:
            decoded_dict = json.loads(decoded_str)
            return decoded_dict
        except Exception as e:
            raise ValueError(f"Failed to decode 'data' field: {e}")

class SensorData(SensorDataBase):
    id: str

    class Config:
        from_attributes = True  # Enables compatibility with SQLAlchemy models

class SearchParams(BaseModel):
    start_time: datetime
    end_time: datetime
    limit: Optional[int] = 10
    offset: Optional[int] = 0 

    class Config:
        from_attributes = True  # Enables compatibility with SQLAlchemy model
