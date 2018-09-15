# isPhoneNumber.py

def isPhoneNumber(text):
    if len(text) != 12: # can't have a length of anything other than 12
        return False
    
    for i in range(0, 3): # first 3 characters must be digits
        if not text[i].isdecimal():
            return False
        
    if text[3] != '-': # followed by a hyphen
            return False

    for i in range(4, 7): # followed by 3 digits
        if not text[i].isdecimal():
            return False
        
    if text[7] != '-': # followed by a hyphen
            return False

    for i in range(8, 12): # followed by 4 digits
        if  not text[i].isdecimal():
            return False
    return True


message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'

for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
print('Done')
