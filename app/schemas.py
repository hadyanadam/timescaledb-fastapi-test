from pydantic import BaseModel
from typing import List
from datetime import datetime

class SensorId(BaseModel):
    id: int

class SensorBase(BaseModel):
    type: str
    location: str

class SensorCreate(SensorBase):
    pass

class SensorRetrieve(SensorBase, SensorId):

    class Config:
        orm_mode=True

class SensorDataBase(BaseModel):
    time: datetime
    sensor_id: int
    temperature: float
    cpu: float

class SensorDataRetrieve(SensorDataBase):
    class Config:
        orm_mode=True

class SensorDataCreate(SensorDataBase):
    pass