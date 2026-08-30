from sqlmodel import SQLModel, Field, Text


class StudyBase(SQLModel):
    name: str = Field(nullable=False)
    description: str = Field(nullable=False, sa_column=Text)
    years: int = Field(nullable=False, gt=0, lt=5)

class Study(StudyBase, table = True):
    __tablename__ = "study_paths"
    id: int | None = Field(primary_key=True, default=None)