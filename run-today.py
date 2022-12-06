from datetime import datetime
from pathlib import Path
import subprocess
import sys


def main(args):
    day = datetime.now().day if len(args) == 1 else int(args[1])
    project_dir = Path(__file__).parent
    subprocess.run(['python', str(project_dir.joinpath(f'AoC2022/day{day}.py'))])


if __name__ == '__main__':
    main(sys.argv)