from datetime import datetime
import glob
from util import *


if __name__ == "__main__":
    config = get_config()
    src, dst, interval = "", "", ""
    try:
        src = config["src"]
        dst = config["dst"]
        interval = config["interval"]
    except KeyError:
        print(f"Invalid configuration file. Missing one or more yaml keys.")
        exit(1)

    src_filename = get_filename_from_path(src)
    copy_func = determine_copy_func(src)

    while True:
        list_of_files = glob.glob(dst + r"\*")
        latest_file = ""
        if len(list_of_files) != 0:
            latest_file = max(list_of_files, key=os.path.getctime)

        if latest_file == "" or get_hash(latest_file) != get_hash(src):
            time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            target_filename = append_to_file_or_dir(src_filename, '-' + time)
            copy(src, os.path.join(dst, target_filename))
            print(f"{time}: Created Backup")

        sleep_with_timer(interval)
