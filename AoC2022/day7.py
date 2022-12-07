from dataloader import get_input_data
from typing import Optional
import re

class Tokens:
    prev_dir_token = '$ cd ..'
    cd_token = '$ cd '
    ls_token = '$ ls '
    dir_token = 'dir '
    file_token = r'\d+ '


class File:
    def __init__(self, name: str, size: int, parent: 'Dir') -> None:
        self.name = name
        self.size = size
        self.parent = parent


class Dir:
    def __init__(self, name: str, parent: Optional['Dir'] = None) -> None:
        self.name = name
        self.dirs: dict[str: Dir] = {}
        self.files: list[File] = []
        self.parent = parent

    def is_root(self) -> bool:
        return self.parent == None

    def add_file(self, file: 'File') -> None:
        self.files.append(file)

    def add_dir(self, new_dir: 'Dir') -> 'Dir':
        self.dirs[new_dir.name] = new_dir
        return new_dir

    def get_direct_children_size(self):
        if len(self.files) == 0:
            return 0
        return sum([f.size for f in self.files])
        
    def get_dir_sizes(self) -> int:
        res = self.get_direct_children_size()
        for d in self.dirs.values():
            res += d.get_dir_sizes()
        return res

    def get_size_dict(self) -> dict['Dir', int]:
        res = {}
        res[self] = self.get_dir_sizes()
        for d in self.dirs.values():
            temp = d.get_size_dict()
            for k, v in temp.items():
                res[k] = v
        return res

        
def parse_dir(line: str, parent: Dir) -> Dir:
    return Dir(line[len(Tokens.cd_token):], parent)


def parse_file(line: str, parent: Dir) -> File:
    size = int(re.findall(Tokens.file_token, line)[0])
    name = line.split(' ')[1]
    return File(name, size, parent)


def parse(data):
    root = Dir('/')
    current_dir = root
    for line in data.split('\n')[1:]:
        line = line.strip()
        if Tokens.prev_dir_token in line:
            current_dir = current_dir.parent
        elif Tokens.cd_token in line:
            current_dir = current_dir.add_dir(parse_dir(line, current_dir))
        elif re.match(Tokens.file_token, line):
            current_dir.add_file(parse_file(line, current_dir))
        else:
            continue
    space_used = root.get_dir_sizes()
    sd = root.get_size_dict()
    print(sum([x for x in sd.values() if x <= 100000]))
    print(min([x for x in sd.values() if 70000000 - space_used + x > 30000000]))


def main():
    data = get_input_data(7)
    parse(data)


if __name__ == '__main__':
    main()

