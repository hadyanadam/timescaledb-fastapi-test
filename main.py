from sqlalchemy import create_engine, MetaData, Table, String, Integer, DateTime, Float, Column, ForeignKey, text, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_string = "postgres://postgres:Adam2579@localhost:5432/test_timescale"

db = create_engine(db_string)
base = declarative_base()

# class SensorData1HourView(base):
#     __tablename__ = 'sensor_data_1_hour_view'
#     time = Column(DateTime(timezone=True))
#     sensor_id = Column(Integer)
#     avg_cpu = Column('avg_cpu', Float)
#     avg_temp = Column('avg_temp', Float)

Session = sessionmaker(db)
class Sensors(base):
    __tablename__ = 'sensors'

    id = Column(Integer, primary_key=True)
    type = Column(String(50))
    location = Column(String(50))

class SensorData(base):
    __tablename__ = 'sensor_data'

    time = Column(DateTime(timezone=True), primary_key=True)
    sensor_id = Column(Integer, ForeignKey('sensors.id'))
    temperature = Column(Float)
    cpu = Column(Float)

    @classmethod
    def session(cls):
        session = Session()
        se = session.query(cls)
        return se

    @classmethod
    def get_sum(cls):
        results = session.query(cls.sensor_id,
                        func.time_bucket(text("'5 minutes'::interval"), cls.time).label('time'),
                        func.sum(cls.temperature).label('sum_temp'),
                        func.sum(cls.cpu).label('sum_cpu'))\
                            .filter(cls.sensor_id == 1)\
                            .group_by(cls.sensor_id, "time")\
                            .order_by("time").limit(10)
        return results


# meta = MetaData(db)
# sensor_data_table = Table('sensor_data_1_hour_view', meta,
#                           Column('time', DateTime(timezone=True)),
#                           Column('sensor_id', Integer),
#                           Column('avg_cpu', Float),
#                           Column('avg_temp', Float))
base.metadata.create_all(db)

# # sensor_datas = session.query(sensor_data_table).first()
# # print(sensor_datas.time)
# # for s in sensor_datas:
# #     print(s.avg_cpu)


# with db.connect() as conn:
#     select_statement = sensor_data_table.select().limit(10)
#     results = conn.execute(select_statement)
#     # print(results)
#     for r in results:
#         print(r.avg_cpu)

# sql = """
# SELECT 
#   sensor_id,
#   time_bucket('1 hour', time) AS period, 
#   AVG(temperature) AS avg_temp, 
#   AVG(cpu) AS avg_cpu 
# FROM sensor_data fr
# GROUP BY 
#   sensor_id, 
#   time_bucket('1 hour', time)
# ORDER BY 
#   sensor_id, 
#   time_bucket('1 hour', time)
# LIMIT 10;
# """
# create_view()
sql = """
SELECT sensor_id, time_bucket('5 minutes'::interval, sensor_data.time) AS time, SUM(temperature) AS sum_temp, SUM(cpu) AS sum_cpu FROM sensor_data WHERE sensor_id=2 GROUP BY sensor_id, time ORDER BY time LIMIT 10;
"""
# results = session.query(SensorData).\
#     from_statement(
#         text(
#             "SELECT sensor_id, time_bucket('5 minutes'::interval, sensor_data.time) AS time, SUM(temperature) AS temperature, SUM(cpu) AS cpu FROM sensor_data WHERE sensor_id=2 GROUP BY sensor_id, time ORDER BY time LIMIT 10"
#             ))
results = SensorData.session().limit(10).all()
print(results)

# for r in results:
#     print(f'{r.time}\t{r.sensor_id}\t{r.sum_temp}\t{r.sum_cpu}')
# print(results.fetchall())


# for r in res
# ults:
#     print(r)