from pydantic import BaseModel

import datetime

import uuid

from typing import Any, Dict, List, Tuple

class Student(BaseModel):
    id: int
    name: str
    age: int


class ReadStudent(BaseModel):
    id: int
    name: str
    age: int
    class Config:
        from_attributes = True




class PostStudent(BaseModel):
    id: int
    name: str
    age: int

    class Config:
        from_attributes = True

