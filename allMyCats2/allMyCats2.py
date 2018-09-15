#allMyCats2.py

catNames = []
while True:
    print()
    name = input('Enter the name of cat ' + str(len(catNames) + 1) +
                 ' (Or enter nothing to stop.):\r\n')
    if name == '':
        break
    catNames = catNames + [name] # list concatenation
print('The cat names are:')
for name in catNames:
    print('  ' + name)
