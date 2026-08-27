from sqlmodel import Session, select, insert, delete, update
from hoarder.course.domain.course import UniversityCourse, CourseCreate, CourseUpdate

def get_all_courses(session: Session) -> list[UniversityCourse]:
    return session.exec(select(UniversityCourse)).all()

def create_course(session: Session, p: CourseCreate):
    course = UniversityCourse.model_validate(p)
    session.add(course)
    session.commit()
    session.refresh(course)
    return course

def delete_course(session: Session, id: int):
    statement = delete(UniversityCourse).where(UniversityCourse.id == id)
    session.exec(statement)
    session.commit()

def update_course(session: Session, id: int, update_payload: CourseUpdate):
    statement = select(UniversityCourse).where(UniversityCourse.id == id)
    course : UniversityCourse = session.exec(statement).first()
    if course:
        course.name = update_payload.name
        course.description = update_payload.description
        course.semester = update_payload.semester
