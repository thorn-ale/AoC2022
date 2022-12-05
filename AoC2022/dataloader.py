from pathlib import Path
import requests
from datetime import datetime
import sys


def fetch_input(day: int | None = None, year: int | None = None) -> str:
    if not day:
        day = datetime.now().day

    if not year:
        year = datetime.now().year

    session_cookie = open(Path(__file__).parent.joinpath('../SESSION.txt'), 'r').read().strip()
    #thanks to Betaveros <https://github.com/betaveros/> for the tip !
    resp = requests.get(f'https://adventofcode.com/{year}/day/{day}/input', headers={
        'Cookie': f'session={session_cookie}'
    })
    if resp.status_code != 200:
        print(f'unable to load {day}/12/{year} input, please create it manually')
        sys.exit(1)
    return resp.text

def get_input_data(day: int) -> str:
    input_file = Path(__file__).parent.joinpath(f'../input/day{day}.txt')
    if not input_file.exists():
        data = fetch_input(day)
        with open(input_file, 'w', encoding='utf-8') as o:
            o.write(data)
        return data
    with open(input_file, 'r', encoding='utf-8') as buf:
        return buf.read()

