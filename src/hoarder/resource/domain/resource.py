from dataclasses import dataclass
from datetime import datetime
from enum import Enum

class ResourceType(Enum):
    FILE = "file",
    LINK = "link",

@dataclass
class Resource:
    id: int
    name: str
    creation_date: datetime
    user_id_added_by: int
    tags: list[str]

@dataclass
class FileSystemResource(Resource):
    fs_path: str

@dataclass
class LinkResource(Resource):
    link: str