import hashlib
import os
import shutil
import time
import yaml


def get_config(config_file: str = "config.yml"):
    with open(config_file, 'r') as f:
        return yaml.safe_load(f)


def get_filename_from_path(path: str) -> str:
    return os.path.basename(os.path.normpath(path))


def append_to_file_or_dir(src: str, app: str):
    if os.path.isdir(src):
        return src + app
    else:  # respect the file extension when appending
        split = os.path.splitext(src)
        return split[0] + app + split[1]


def sleep_with_timer(t: float):
    """Doesn't seem to work when running in IDE without debug mode"""
    while t > 0:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r", flush=True)
        time.sleep(1)
        t -= 1


def copy(src: str, dst: str):
    if os.path.isdir(src):
        shutil.copytree(src, dst)
    else:
        shutil.copy(src, dst)


def determine_copy_func(path: str):
    """Returns the correct copy function based on whether the path leads to a file or a directory"""
    if os.path.isdir(path):
        return shutil.copytree
    else:
        return shutil.copy


def get_hash(path: str) -> str:
    if os.path.isdir(path):
        return hash_dir(path)
    else:
        return sha1_of_file(path)


# source: https://stackoverflow.com/questions/36204248/creating-unique-hash-for-directory-in-python
def sha1_of_file(filepath):
    sha = hashlib.sha1()
    with open(filepath, 'rb') as f:
        while True:
            block = f.read(2**10)  # Magic number: one-megabyte blocks.
            if not block: break
            sha.update(block)
        return sha.hexdigest()


# source: https://stackoverflow.com/questions/36204248/creating-unique-hash-for-directory-in-python
def hash_dir(dir_path):
    hashes = []
    for path, dirs, files in os.walk(dir_path):
        for file in sorted(files):  # we sort to guarantee that files will always go in the same order
            hashes.append(sha1_of_file(os.path.join(path, file)))
        for dir in sorted(dirs):  # we sort to guarantee that dirs will always go in the same order
            hashes.append(hash_dir(os.path.join(path, dir)))
        break  # we only need one iteration - to get files and dirs in current directory
    return str(hash(''.join(hashes)))
