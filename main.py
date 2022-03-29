import shutil
from datetime import datetime
import glob
from util import *


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

        if latest_file == "" or hash_dir(latest_file) != hash_dir(src):
            time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            target_filename = src_filename + time
            shutil.copytree(src, os.path.join(dst, target_filename))
            print(f"{time}: Created Backup")

        sleep_with_timer(interval)
