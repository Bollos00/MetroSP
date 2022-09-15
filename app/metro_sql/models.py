from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Enum, Float
from sqlalchemy.orm import relationship
from sqlalchemy_utils import UUIDType
import uuid
from sqlalchemy.sql import func

from .metro_sql_db import Base
from .enums import MetroFleet, MetroLine, MetroWay

class User(Base):
    __tablename__ = "users"

    id = Column(UUIDType(), primary_key=True, index=True, default=uuid.uuid4)
    password = Column(String)
    last_activity = Column(DateTime(timezone=True), server_default=func.now(),
                           onupdate=func.utc_timestamp())


class Node(Base):
    __tablename__ = "nodes"

    id = Column(Integer, primary_key=True, index=True)
    
    node_id = Column(Integer)
    date_time = Column(DateTime(timezone=True))

    owner_id = Column(UUIDType(), ForeignKey("users.id"))
    # owner = relationship("User", back_populates="nodes")
    
    
class NodeLink(Base):
    __tablename__ = "node_links"

    id = Column(Integer, primary_key=True, index=True)
    
    node_link_id = Column(Integer)
    
    start_date_time = Column(DateTime(timezone=True))
    end_date_time = Column(DateTime(timezone=True))
    displacement_time_s = Column(Integer)


class IndoorNavBeacon(Base):
    __tablename__ = "indoor_nav_beacons"
    
    id = Column(Integer, primary_key=True, index=True)
    
    station_id = Column(Integer, ForeignKey("stations.id"))
    subenvironment = Column(Integer)
    beacon_id_minor = Column(Integer)
    
    x = Column(Float, default=0)
    y = Column(Float, default=0)
    z = Column(Float, default=0)
    

class Station(Base):
    __tablename__ = "stations"
    
    id = Column(Integer, primary_key=True, index=True)
    beacon_id_major = Column(Integer, index=True, autoincrement=True)
    name = Column(String, index=True)
    subenvironments = Column(Integer, default=0)
    lines = Column(Integer, default=MetroLine.L_INVALID)
 
    
class Train(Base):
    __tablename__ = "trains"
    
    id = Column(Integer, primary_key=True, index=True)
    fleet = Column(Enum(MetroFleet)) # Frota
    beacon_id_major_begin = Column(Integer)
    beacon_id_major_end = Column(Integer)
    lines = Column(Integer, default=MetroLine.L_INVALID)
    cars = Column(Integer)
    doors = Column(Integer)


class ValidUUID(Base):
    __tablename__ = "valid_uuids"
    uuid = Column(UUIDType(), primary_key=True)