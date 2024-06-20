#!/usr/bin/env python3
from argparse import ArgumentParser
from re import search
from subprocess import run

class VersionTagger:

    def __init__(self, file_path):
        self.file_path = file_path
        self.current_version: List[int] = [int(v) for v in self.get_current_version().split('.')]

    def get_current_version(self) -> None:
        with open(self.file_path, 'r') as file:
            for line in file:
                if line.startswith('    VERSION ='):
                    return search(r'\d+\.\d+\.\d+', line).group()

    def version_short(self) -> str:
        version = self.current_version.copy()
        if version[2] == 0:
            del version[2]
        v = '.'.join([str(i) for i in version])
        return f"v{v}"

    def exec(self, commit: bool, push: bool) -> None:
        # try:
        self.add()
        if commit:
            self.commit()
        self.tag()
        if push:
            self.push()
        # except Exception as e:
        #    print(e)

    def add(self) -> None:
        cmd = f'git add {self.file_path}'
        # TODO: 2024-06-20, setup.py needs to be added, too!
        run(cmd, shell=True)

    def commit(self) -> None:
        version = [str(i) for i in self.current_version]
        msg = f"updated version in {self.file_path} to {'.'.join(version)}"
        cmd = f'git commit -m "{msg}"'
        run(cmd, shell=True)

    def tag(self) -> None:
        cmd = f'git tag --force {self.version_short()}'
        run(cmd, shell=True)

    def push(self) -> None:
        cmd = 'git push --tags origin master'
        run(cmd, shell=True)


def main():
    parser = ArgumentParser(description='Increment version in controller.py')
    parser.add_argument('--no-commit', dest='commit', action='store_false', default=True, help='Do not commit')
    parser.add_argument('--no-push', dest='push', action='store_false', default=True, help='Do not commit')
    
    args = parser.parse_args()
    
    tagger = VersionTagger('src/xmrsigner/controller.py')
    tagger.exec(args.commit, args.push)

if __name__ == '__main__':
    main()
