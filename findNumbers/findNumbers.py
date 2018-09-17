#!python3
# findNumbers.py - this will print all the properly formatted numbers

import re
numRegex = re.compile(r'(?<!,)\b\d{1,3}(?:,\d{3})*\b(?!,)')
matches = []
print(numRegex.findall('42 1,234 6,368,745 12,34,567 1234'))
