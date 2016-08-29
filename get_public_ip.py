#!/usr/bin/python3
#Get the public ip address of this computer from a web service
#2016-08-28

import requests

r = requests.get('http://bot.whatismyipaddress.com')
ip = r.text
print(str(ip))
