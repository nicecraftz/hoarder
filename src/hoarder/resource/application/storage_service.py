import os
import re
import tempfile
from pathlib import Path
from uuid import uuid4

from hoarder.core.config import DATA_FOLDER
from hoarder.core.exception import ProblemException

BASE = Path(DATA_FOLDER).resolve()
SAFE_EXT = re.compile(r"^\.[A-Za-z0-9]{1,10}$")


def _safe_extension(original_name: str) -> str:
    ext = Path(original_name).suffix.lower()
    if not ext:
        return ".bin"
    if not SAFE_EXT.match(ext):
        raise ProblemException(
            status=400,
            title="Invalid File Extension",
            detail=f"The extension {ext!r} is not accepted.",
        )
    return ext


def create_file(data: bytes, original_name: str) -> str:
    key = uuid4().hex + _safe_extension(original_name)
    path = (BASE / key).resolve()

    if not path.is_relative_to(BASE):
        raise ProblemException(
            status=500,
            title="Invalid Storage Path",
            detail="Refusing to write outside the data folder.",
        )

    fd, tmp_name = tempfile.mkstemp(dir=BASE, suffix=".part")
    try:
        with os.fdopen(fd, "wb") as tmp:
            tmp.write(data)
            tmp.flush()
            os.fsync(tmp.fileno())
        os.replace(tmp_name, path)
    except BaseException:
        Path(tmp_name).unlink(missing_ok=True)
        raise

    return key
