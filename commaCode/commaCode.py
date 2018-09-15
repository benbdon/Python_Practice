# commaCode.py - takes a list value as an argument and returns a string with all the items separated by a comma and a space, with and inserted before the last item.

def getInput(): #assuming you want user-defined input
    strList = []
    print('Please provide a list of strings. Type enter again when complete.')
    while True:
        item = input()
        if item == '':
            break
        strList.append(item)
    return strList

def listToString(strList):    
    string = ''    
    for i in strList:
        if i == strList[0]: #if it's the first element, just add it to string
            string = i
        elif i == strList[-1]: #if it's the last element, use ", and" before it
            string = string + ', and ' + i
        else: #otherwise, just add a ", " before it
            string = string + ', ' + i
    print(string)

someList = ['apples', 'bananas', 'tofu', 'cats']
#someList = getInput()
listToString(someList)
