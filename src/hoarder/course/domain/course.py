from dataclasses import dataclass

@dataclass
class UniversityCourse:
    id: int
    name: str
    year: int
    semester: 1 | 2
    resource_ids: list[int]