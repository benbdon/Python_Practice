#! python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.

import pyperclip, re

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))? # may have area code
    (\s|-|\.)? # may have a separator
    (\d{3}) # must have first 3 digits
    (\s|-|\.) #must have a seperator
    (\d{4}) #must have last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))? # may have an extension
    )''', re.X) # X stands for VERBOSE which allows you to break the Regex into multiple lines

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+ # username
    @ # @ symbol
    [a-zA-Z0-9.-]+ #domain name
    (\.[a-zA-Z]{2,4}) #dot-something what's a 4 dot-something?
    )''', re.X)

text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1],groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
