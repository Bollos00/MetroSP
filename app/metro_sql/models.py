from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy_utils import UUIDType
import uuid
from sqlalchemy.sql import func

from .metro_sql_db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(UUIDType(), primary_key=True, index=True, default=uuid.uuid4)
    password = Column(String)
    last_activity = Column(DateTime(timezone=True), server_default=func.now())


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
    
    from_date_time = Column(DateTime(timezone=True))
    to_date_time = Column(DateTime(timezone=True), ForeignKey("nodes.date_time"))
    
    owner_id = Column(UUIDType(), ForeignKey("users.id"))
    # owner = relationship("User", back_populates="node_links")