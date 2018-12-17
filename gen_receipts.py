#!/bin/python

import random
import json
import os

count = os.getenv("FILE_COUNT") or 100
words = [word.strip() for word in open('/usr/share/dict/words').readlines()]

for identifier in range(1, count + 1):
    amount = random.uniform(1.0, 1000.0)
    

