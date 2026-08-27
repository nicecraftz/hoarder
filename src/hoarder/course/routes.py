from fastapi import APIRouter, Depends, Response
from sqlmodel import Session

import hoarder.course.application.service as service
from hoarder.course.domain.course import CoursePublic, CourseCreate, CourseUpdate
from hoarder.core.db import get_session

course = APIRouter(prefix="/course", tags=["university_course"])

@course.get("/", response_model=list[CoursePublic])
async def get_all_courses(session: Session = Depends(get_session)):
    return service.get_all_courses(session)

@course.post("/", response_model=CoursePublic)
async def create_course(create_payload: CourseCreate, session: Session = Depends(get_session)):
    return service.create_course(session, create_payload)

@course.patch("/{id}")
async def update_course(id: int, update_payload: CourseUpdate, session: Session = Depends(get_session)):
    return service.update_course(session, id, update_payload)

@course.delete("/{id}")
async def delete_course(id: int, session: Session = Depends(get_session)):
    service.delete_course(session, id)
    return Response(status_code=200)
