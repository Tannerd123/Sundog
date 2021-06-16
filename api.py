# api.py - Made by Tanner Eldridge
# ESoftware Inc.
# 
# 
# API - Methods
# 
#  REST API
# Application progrmaming Interface
# Representational State  Transfer 
#
#

import requests
import json



response = requests.get(
  'https://api.stackexchange.com/2.2/answers?order=desc&sort=activity&site=stackoverflow')

for data in response.json()['items']:
  print(data['title'])