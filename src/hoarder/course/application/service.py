from sqlmodel import Session, select
from hoarder.core.db import get_session
from hoarder.course.domain.course import UniversityCourse

async def get_all_courses() -> list[UniversityCourse]:
    session: Session = get_session()
    session.exec(select(UniversityCourse)).all()
