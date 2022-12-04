from pathlib import Path


def get_input_data(day: int) -> str:
    with open(Path(__file__).parent.joinpath(f'../input/day{day}.txt'), 'r', encoding='utf-8') as buf:
        return buf.read()