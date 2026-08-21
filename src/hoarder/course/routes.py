from fastapi import APIRouter
import hoarder.course.application.service as service
from hoarder.course.domain.course import CoursePublic 

course = APIRouter(prefix="/course", tags=["university_course"])

@course.get("/", response_model=list[CoursePublic])
async def get_all_courses():
    return service.get_all_courses()
