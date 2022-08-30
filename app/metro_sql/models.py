from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Enum
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
    last_activity = Column(DateTime(timezone=True), server_default=func.now())


# Route planner
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
    end_date_time = Column(DateTime(timezone=True), ForeignKey("nodes.date_time"))
    displacement_time_s = Column(Integer)

# Beacons
# class Station(Base):
#     __tablename__ = "stations"
    
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String)
#     beacon_id_major = Column(Integer)
#     subenvironments = Column(Integer)
#     lines = Column(Enum(MetroLine))
    
# class Train(Base):
#     __tablename__ = "trains"
    
#     id = Column(Integer, primary_key=True, index=True)
#     fleet = Column(String) # Frota
#     beacon_id_major_begin = Column(Integer)
#     beacon_id_major_end = Column(Integer)
    