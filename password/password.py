#! python3
# This program compares the user input to a secret password and provides a response
# Written for Python 3.7.0
# Ben Don
# Modified: 8.3.18

passwordFile = open('SecretPasswordFile.txt')
secretPassword = passwordFile.read()
print('Enter your password.')
typedPassword = input()
if typedPassword == secretPassword:
    print('Access granted')
elif typedPassword == '12345':
    print('That password is one that an idiot puts on their luggage.')
else:
    print('Access denied')
