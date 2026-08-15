from .core import config
import os

def ensure_data_folder():
    try:
        if not os.path.exists(config.DATA_FOLDER):
            os.mkdir(config.DATA_FOLDER)
    except Exception as e:
        print(f"An error occurred: {e}")


ensure_data_folder()