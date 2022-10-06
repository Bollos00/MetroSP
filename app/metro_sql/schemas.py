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

class NodeCreate(NodeBase):
    pass

class Node(NodeBase):
    id: int
    owner_id: uuid.UUID

    class Config:
        orm_mode = True
