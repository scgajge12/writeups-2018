#!/usr/bin/python

import requests
import re

headers = {'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}

r = requests.get('http://2018shell1.picoctf.com:53383/flag', headers=headers)
source = r.text

print re.findall(r'(picoCTF\{.+\})', source)[0]
