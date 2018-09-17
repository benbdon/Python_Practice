#!python3
# strongPassword.py = this program will check if a provided password is strong
import re

def isLongEnough(pw):
    if (len(pw) < 8):
        return False
    else:
        return True

def hasUpper(pw):
    upperRegex = re.compile(r'[A-Z]')
    if(upperRegex.search(pw) == None):
        return False
    else:
        return True

def hasLower(pw):
    lowerRegex = re.compile(r'[a-z]')
    if(lowerRegex.search(pw) == None):
        return False
    else:
        return True

def hasNumber(pw):
    numRegex = re.compile(r'\d')
    if(numRegex.search(pw) == None):
        return False
    else:
        return True
                            
pw = input('What\'s the password?\n')
print(isLongEnough(pw) or hasUpper(pw) or hasLower(pw) or hasNumber(pw))
