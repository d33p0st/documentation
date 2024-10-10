#!/usr/bin/env python3

from typing import Union, Tuple, List
import requests
import sys
import os

PYTHON_PROJECTS = [
    'modstore',
    'friday-d33pster',
    'portlive',
    'mr-menu',
    'test-ransomware',
    'looger',
    'wrapper-bar',
    'furypie',
    'detecteff-python',
    'argpi',
    'deny-me',
    'ende',
    'pasta-man',
    'target-ports',
    'serversock',
    's3ssion',
    'dynalistTk'
]

RUST_PROJECTS = [
    'argrust',
    'detecteff',
    'gcl',
    'rustypath',
    'termutils',
    'xmenu'
]

class AutoChangeBadge:
    def __init__(self, pyprojects: List[str] = PYTHON_PROJECTS, rsprojects: List[str] = RUST_PROJECTS) -> None:
        self.api = 'https://api.pepy.tech/api/v2/projects/{}'
        self.pyprojects = pyprojects
        self.rsprojects = rsprojects
        self.found = None

    @property
    def find(self) -> Union[Tuple[str, int, str], None]:
        top = None
        downloads = 0
        link = None

        if os.getenv('PEPY_API'):
            headers = {'X-Api-Key': os.getenv('PEPY_API')}
            print('api. OK.')
        else:
            print('api not found. NOT OK.')
            sys.exit(1)
        
        counter = 0
        # check python projects
        print("Started Check for Python Projects. OK.")
        for p in self.pyprojects:
            response_raw = requests.get(self.api.format(p), headers=headers)
            if response_raw.status_code == 200:
                response = response_raw.json()
                if response['total_downloads'] > downloads:
                    top = p
                    downloads = response['total_downloads']
                    link = f'https://pypi.org/project/{p}'
            print(f'checked {p}. OK.')
            counter += 1
        
        # check rust projects
        print("Started Check for Rust Projects. OK.")
        for p in self.rsprojects:
            url = f"https://crates.io/api/v1/crates/{p}"
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()
                if data["crate"]["downloads"] > downloads:
                    top = p
                    downloads = data["crate"]["downloads"]
                    link = f'https://crates.io/crates/{p}'
            
            print(f'checked {p}. OK.')
            counter += 1
        
        print(f'checked {counter} projects. OK.')
        
        if top:
            self.found = True
            return (top.replace('-', '_'), downloads, link)
        else:
            return top
    
    def update(self, file: str = 'index.markdown') -> None:
        badge_url1 = 'https://img.shields.io/badge/Top%20Downloaded%20Project%20-%20{}%20-%20Blue?link={}'
        badge_url2 = 'https://img.shields.io/badge/Top%20Project%20Download%20Count%20-%20{}%20-%20Blue?link={}'

        print(f'Checking...')

        status = self.find
        
        print('OK.')

        if status:
            print(f'Trying to update {file}...')
            with open(file, 'r+') as ref:
                contents = ref.read().split('\n')
            
            for i in range(contents.__len__()):
                if contents[i].__contains__('<!-- top badge -->'):
                    temp = contents[:i+1] # until the comments line
                    temp.append(f'![Top Project]({badge_url1.format(status[0], status[2])})\n![Top Project Download Count]({badge_url2.format(status[1], status[2])})')
                    while contents[i+1].__contains__('![Top Project]') or contents[i+1].__contains__('![Top Project Download Count]'):
                        i += 1
                    temp.extend(contents[i+1:])
                    contents = temp
                    break
            
            with open(file, 'w+') as ref:
                ref.write('\n'.join(contents))
            
            print('Updated index.markdown with the top project badges. status Ok.')
            sys.exit(0)
        else:
            print('No Projects Found. status NOT OK.')
            sys.exit(1)

if __name__ == '__main__':
    AutoChangeBadge().update()