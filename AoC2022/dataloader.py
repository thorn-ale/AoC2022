from pathlib import Path
import requests
from datetime import datetime
import sys
import os


def fetch_input(day: int | None = None, year: int | None = None) -> str:
    if not day:
        day = datetime.now().day

    if not year:
        year = datetime.now().year

    if not 'AOCSESSION' in os.environ.keys():
        session_file = Path(__file__).parent.joinpath('../SESSION.txt')
        if session_file.exists():
            session_cookie = open(session_file, 'r').read().strip()
        else:
            print(f'neither the env variable AOCSESSION nor the file [project_root]/SESSION.txt exists. Please create either one of them or fetch your input manually.')
            sys.exit(1)
    else:
        session_cookie = os.environ.get('AOCSESSION')

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

