# collatz.py - responds to even and odd numbers

def collatz(n):
    if n % 2 == 0: # If even
        print( n // 2)
        return n // 2
    elif n % 2 == 1: #If odd
        print( 3 * n + 1)
        return 3 * n + 1

try:
    n = int(input('Enter a positive integer:\r\n'))
    while n != 1:
        n = collatz(n)

except ValueError:
    print('Invalid input, must be an integer')
