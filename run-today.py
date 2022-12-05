from datetime import datetime
import subprocess
import sys


def main(args):
    day = datetime.now().day if len(args) == 1 else int(args[1])
    subprocess.run(['python', f'./AoC2022/day{day}.py'])


if __name__ == '__main__':
    main(sys.argv)