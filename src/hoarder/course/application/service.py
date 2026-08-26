from sqlmodel import Session, select, insert, delete
from hoarder.course.domain.course import UniversityCourse, CourseCreate

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