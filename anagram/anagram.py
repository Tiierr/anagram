#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import requests
import json
from bs4 import BeautifulSoup

class Anagram:
    url = "http://wordsmith.org/anagram/anagram.cgi?anagram={0}&language=english&t=0&d=&include=&exclude=&n=&m=&source=adv&a=n&l=n&q=n&k=0"

    def __init__(self, argv):
        self.argv = ' '.join(argv)
        if len(argv) == 1:
            self.url = self.url.format(argv[0])
            self.transfer()
        elif len(argv) > 1:
            content = '+'.join(argv)
            self.url = self.url.format(content)
            self.transfer()
        else:
            print('INPUT ERROR!')

    def transfer(self):
        anagrams = self.parse()
        for i, anagram in enumerate(anagrams):
            print(str(i + 1)+'. ' + anagram)
        # print(json.dumps({self.argv : anagrams}))

    def parse(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text,'lxml')
        contents = soup.findAll('p')[-3]
        contents = str(contents).split('<br/>')[1:-1]
        for i, content in enumerate(contents):
            if content.startswith('\n'):
                content = content[1:]
                contents[i] = content

        return contents

def main():
    Anagram(sys.argv[1:])

if __name__ == '__main__':
    main()
