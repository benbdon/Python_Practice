# characterPictureGrid.py - invert and print grid

def rotateAndPrint(grid):
    for y in range(len(grid[0])):
        string = ''
        for x in range(len(grid)):
            string += grid[x][y]
        print(string)

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

rotateAndPrint(grid)        
