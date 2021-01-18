from sqlalchemy import Column, DateTime, ForeignKey, String, Integer, Float, create_engine
from sqlalchemy.ext.declarative import declarative_base
from .config import DATABASE_URI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(DATABASE_URI)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Sensors(Base):
    __tablename__ = 'sensors'

    id = Column(Integer, primary_key=True)
    type = Column(String(50))
    location = Column(String(50))

class SensorData(Base):
    __tablename__ = 'sensor_data'

    time = Column(DateTime(timezone=True), primary_key=True)
    sensor_id = Column(Integer, ForeignKey('sensors.id'), nullable=False)
    temperature = Column(Float)
    cpu = Column(Float)

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(20), nullable=False)
    password = Column(String(15), nullable=False)

