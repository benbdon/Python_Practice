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
    )''', re.VERBOSE)

# TODO: Create email regex.

# TODO: Find matches in clipboard text.

# TODO: Copy results to the clipboard.
