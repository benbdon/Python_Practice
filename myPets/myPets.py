myPets = ['Zophie', 'Pooka', 'Fat-Tail']
name = input('Enter a pet name:\r\n')
if name not in myPets:
    print('I do not have a pet named ' + name)
else:
    print(name + ' is my pet.')
