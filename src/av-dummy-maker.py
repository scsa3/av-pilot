import argparse
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument('dir', nargs='?', default=Path('./dummy/'))
parser.add_argument('--prefix', help='dummy file prefix', default='ebod')
args = parser.parse_args()


def main() -> None:
    base_path = args.dir
    base_path.mkdir(parents=True, exist_ok=True)

    base_file_name = args.prefix + '-{:0>3d}.mp4'
    base_file_string = base_file_name
    for i in range(1, 11):
        file_string = base_file_string.format(i)
        path = base_path / Path(file_string)
        print(path.resolve())
        path.touch()


if __name__ == '__main__':
    main()
