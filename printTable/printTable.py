# printTable.py - this will take a list of strings
# and format them into columns

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(stringList):
    colWidth = [0] * len(stringList)
    for i in range(len(tableData)):
        length = 0
        for string in tableData[i]:
            if len(string) > length:
                length = len(string)
        colWidth[i] = length

    for i in range(len(stringList[0])):
        for j in range(len(stringList)):
            print(tableData[j][i].rjust(colWidth[j]), end=' ')
        print()
                              
    
printTable(tableData)
