import shutil
import hashlib
from datetime import datetime
import glob
import os
import yaml
from time import sleep


def get_savegame_hash(path: str) -> str:
    with open(os.path.join(latest_file, r"HonourMode.lsv"), "rb") as f:
        b = f.read()  # read entire file as bytes
        return hashlib.sha256(b).hexdigest()


def get_config(config_file: str = "config.yml"):
    with open(config_file, 'r') as f:
        return yaml.safe_load(f)


def get_filename_from_path(path: str) -> str:
    return os.path.basename(os.path.normpath(path))


if __name__ == "__main__":
    config = get_config()
    src = config["src"]
    dst = config["dst"]
    interval = config["interval"]
    src_filename = get_filename_from_path(src)

    while True:
        list_of_files = glob.glob(dst + r"\*")
        latest_file = ""
        if len(list_of_files) != 0:
            latest_file = max(list_of_files, key=os.path.getctime)

        if latest_file == "" or get_savegame_hash(latest_file) != get_savegame_hash(src):
            time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            target_filename = src_filename + time
            shutil.copytree(src, os.path.join(dst, target_filename))
            print(f"{time}: Created Backup")
        sleep(interval)
