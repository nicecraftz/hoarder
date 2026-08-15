from os import path
from pathlib import Path
from ...core import config

STORAGE_DIR = config.DATA_FOLDER

def is_valid_file(file_path: Path):
    return path.exists(file_path) and path.isfile(file_path)

def is_safe_path(file_path: Path):
    return file_path.is_relative_to(STORAGE_DIR)

def get_file(name: str) -> Path | bool:
    file_path = Path(path.join(STORAGE_DIR, name))
    
    if is_valid_file(file_path) and is_safe_path(file_path):
        return file_path.absolute()
     
    return False 
