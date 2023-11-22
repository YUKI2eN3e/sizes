import math
from os import path, walk


def convert_size(size_bytes):
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return "%s %s" % (s, size_name[i])


def get_dir_size(dir: str) -> int:
    total: int = 0
    for dirpath, dirname, filenames in walk(dir):
        for filename in filenames:
            filepath = path.join(dirpath, filename)
            try:
                # if path.exists(filepath) and not path.islink(filepath):
                if not path.islink(filepath):
                    total += path.getsize(filepath)
            except Exception:
                # print(f"{Colours.LIGHT_PURPLE}{Colours.UNDERLINE}{e}{Colours.RESET}")
                pass
    return total


def get_file_size(file: str) -> int:
    """Get the size of the file (-1 if link).

    Args:
        file (str): The file path.

    Returns:
        int: The file size if not a link, otherwise -1
    """
    if not path.islink(file):
        return path.getsize(file)
    return -1
