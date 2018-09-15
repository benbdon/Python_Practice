# prettyCharacterCount.py

import pprint

message = 'It was a bright, cold day in April and the clocks were striking thirteen.'
count = {}

for char in message:
    count.setdefault(char,0) # saves a couple lines of code, but the name is misleading/confusing
    count[char] = count[char] + 1

pprint.pprint(count)
