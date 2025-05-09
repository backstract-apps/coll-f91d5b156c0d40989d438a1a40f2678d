from sqlalchemy.orm import Session
from sqlalchemy import and_, or_
from typing import *
from fastapi import Request, UploadFile, HTTPException
import models, schemas
import boto3

import jwt

import datetime

from pathlib import Path

async def get_student(db: Session):

    student_all = db.query(models.Student).all()
    student_all = [new_data.to_dict() for new_data in student_all] if student_all else student_all

    res = {
        'student_all': student_all,
    }
    return res

async def get_student_id(db: Session, id: int):

    student_one = db.query(models.Student).filter(models.Student.id == id).first() 
    student_one = student_one.to_dict() if student_one else student_one

    res = {
        'student_one': student_one,
    }
    return res

async def put_student_id(db: Session, id: int, name: str, age: int):

    student_edited_record = db.query(models.Student).filter(models.Student.id == id).first()
    for key, value in {'id': id, 'age': age, 'name': name}.items():
          setattr(student_edited_record, key, value)
    db.commit()
    db.refresh(student_edited_record)
    student_edited_record = student_edited_record.to_dict() 

    res = {
        'student_edited_record': student_edited_record,
    }
    return res

async def delete_student_id(db: Session, id: int):

    student_deleted = None
    record_to_delete = db.query(models.Student).filter(models.Student.id == id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        student_deleted = record_to_delete.to_dict() 

    res = {
        'student_deleted': student_deleted,
    }
    return res

async def post_student(db: Session, raw_data: schemas.PostStudent):
    id:int = raw_data.id
    name:str = raw_data.name
    age:int = raw_data.age


    record_to_be_added = {'id': id, 'age': age, 'name': name}
    new_student = models.Student(**record_to_be_added)
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    student_inserted_record = new_student.to_dict()


    # asdnbmnbmNZDBvfz
    file_upload: str = "user_file"

    res = {
        'student_inserted_record': age,
        'sadfgf': name,
        'dfgchvb': full_name,
    }
    return res

