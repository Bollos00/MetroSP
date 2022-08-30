from pydantic import BaseModel
import datetime
import uuid


class UserBase(BaseModel):
    id: uuid.UUID

class UserCreate(UserBase):
    password: str

class UserAuth(UserCreate):
    pass

class User(UserBase):
    last_activity: datetime.datetime = datetime.datetime(year=1, month=1, day=1)

    class Config:
        orm_mode = True


class NodeBase(BaseModel):
    node_id: int
    date_time: datetime.datetime
    owner_id: uuid.UUID


class NodeCreate(NodeBase):
    pass

class Node(NodeBase):
    id: int

    class Config:
        orm_mode = True


class NodeLinkBase(BaseModel):
    node_link_id: int
    start_date_time: datetime.datetime
    end_date_time: datetime.datetime

class NodeLinkCreate(NodeLinkBase):
    pass

class NodeLink(NodeLinkBase):
    id: int
    displacement_time_s: int
    
    class Config:
        orm_mode = True