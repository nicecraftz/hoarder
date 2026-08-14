from dataclasses import dataclass
from datetime import datetime
from enum import Enum

class Role(Enum):
    USER = "user",
    VIEWER = "viewer",
    TRUSTED = "trusted",
    MODERATOR = "moderator",
    ADMIN = "admin"

@dataclass
class User:
    id: int
    username: str
    password_hash: str
    created_at: datetime
    verified: bool
    role: Role