import argparse
import re
from pathlib import Path
from typing import List

parser = argparse.ArgumentParser()
parser.add_argument('target_directory', metavar='target-directory')
parser.add_argument('-v', '--verbose', help='increase output verbosity', action='store_true')
args = parser.parse_args()


def main() -> None:
    directory_path = get_path()
    paths = collect_video_paths(directory_path)
    paths = paths_filter(paths)
    print_paths(paths)


def get_path() -> Path:
    path = args.target_directory
    return Path(path)


def collect_video_paths(path: Path) -> List[Path]:
    files_gen = path.glob('**/*.*')
    return [file for file in files_gen]


def paths_filter(paths: List[Path]) -> List[Path]:
    new_paths: List[Path] = list()
    for path in paths:
        if is_porn(path):
            new_paths.append(path)
    return sorted(new_paths)


def is_porn(path: Path) -> bool:
    name = path.name
    name = name.lower()
    is_code_in = re.search(r'[a-z]{3,4}-?[0-9]{3}', name)
    extension = path.suffix
    extension = extension.lower()
    is_video = re.match(r'\.(avi|mp4)', extension)
    return bool(is_video) and bool(is_code_in)


def print_paths(files: List[Path]) -> None:
    print_function = print_absolute_path if args.verbose else print_relate_path
    for file in files:
        print_function(file)


def print_relate_path(path: Path):
    print(path)


def print_absolute_path(path: Path):
    print(path.resolve())


if __name__ == '__main__':
    main()
