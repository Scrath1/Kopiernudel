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


config = get_config()
source_dir = config["src"]
dest_dir = config["dst"]

list_of_files = glob.glob(dest_dir + r"\*")  # * means all if need specific format then *.csv
latest_file = ""
if len(list_of_files) != 0:
    latest_file = max(list_of_files, key=os.path.getctime)

while True:
    if latest_file == "" or get_savegame_hash(latest_file) != get_savegame_hash(source_dir):
        time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        target_filename = r"HonourMode" + time
        shutil.copytree(source_dir, os.path.join(dest_dir, target_filename))
        print(f"{time}: Created Backup")
    sleep(60)
