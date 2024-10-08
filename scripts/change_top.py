#!/usr/bin/env python3

from typing import Union, Tuple
import requests
import sys
import os

PROJECTS = [
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

class AutoChangeBadge:
    def __init__(self, projects: list[str] = PROJECTS) -> None:
        self.api = 'https://api.pepy.tech/api/v2/projects/{}'
        self.projects = projects
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
        for p in self.projects:
            response_raw = requests.get(self.api.format(p), headers=headers)
            if response_raw.status_code == 200:
                response = response_raw.json()
                if response['total_downloads'] > downloads:
                    top = response['id']
                    downloads = response['total_downloads']
                    link = f'https://pypi.org/project/{p}'
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