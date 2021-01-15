from . import models, schemas
from typing import List, Optional
from .dependencies import get_db_session
from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from datetime import datetime

api = APIRouter()
@api.get('/')
def home(db: Session = Depends(get_db_session)):
    return {"text" : "hello world"}

@api.post('/create')
def create(sensors: schemas.SensorCreate, db: Session = Depends(get_db_session)):
    sensor = models.Sensors(**sensors.dict())
    db.add(sensor)
    db.commit()
    return {'response':'success'}

@api.get('/retrieve/{id}', response_model=schemas.SensorRetrieve)
def retrieve(id: int, db: Session= Depends(get_db_session)):
    sensor = db.query(models.Sensors).filter_by(id=id).first()
    return sensor

@api.post('/data/create')
def data_create(sensor_data:List[schemas.SensorDataRetrieve], db: Session= Depends(get_db_session)):
    for data in sensor_data:
        create_data = models.SensorData(**data.dict())
        db.add(create_data)
    db.commit()
    return {"response" : f"{len(sensor_data)} created"}

@api.get('/data/retrieve/{id}', response_model=List[schemas.SensorDataRetrieve])
def data_retrieve(
    id: int, date_start:Optional[datetime] = False, date_end: Optional[datetime] = False,
    db: Session= Depends(get_db_session)
):
    response = db.query(models.SensorData)\
        .filter(models.SensorData.sensor_id == id)
    if date_start and date_end:
        response = response\
            .filter(models.SensorData.time >= date_start)\
            .filter(models.SensorData.time <= date_end)
    return response.all()