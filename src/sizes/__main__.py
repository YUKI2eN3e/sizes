from os import listdir, path, walk
from typing import List

from sizes.cli import get_args
from sizes.dir import Dir
from sizes.file import File
from sizes.utils import get_dir_size, get_file_size


def run() -> None:
    args = get_args()
    dirs: List[Dir] = []
    files: List[File] = []
    if args.directory:
        start_dir = "."
        for dir_name in [
            path.join(start_dir, dir_name)
            for dir_name in listdir(start_dir)
            if path.isdir(path.join(start_dir, dir_name))
        ]:
            dirs.append(Dir(size=get_dir_size(dir_name), name=dir_name))
    if args.file:
        for filepath in next(walk("."), (None, None, []))[2]:
            try:
                if not path.islink(filepath):
                    files.append(File(size=get_file_size(filepath), name=filepath))
            except Exception:
                pass
    items: List[File | Dir] = []
    if len(dirs) > 0:
        items.extend(dirs)
    if len(files) > 0:
        items.extend(files)
    if args.ordered:
        items.sort(reverse=True)
    for item in items:
        print(item)


if __name__ == "__main__":
    run()
