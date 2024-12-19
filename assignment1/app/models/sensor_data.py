from sqlalchemy import Column, Integer, String, DateTime
from .base import Base_

class SensorData(Base_):
    __tablename__ = "sensor_data"

    message_id = Column(String, nullable=False)  # Message ID as a string
    publish_time = Column(DateTime(timezone=True), nullable=False, index=True)  # Publish time as ISO8601
    v0 = Column(String, nullable=False)  # Sensor value 0 as a string
    v11 = Column(String, nullable=False)  # Sensor value 11 as a string
    v18 = Column(String, nullable=False)  # Sensor value 18 as a string
    time = Column(DateTime, nullable=False)  # ISO8601 timestamp for the `time` column
