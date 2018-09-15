# Chap 2 Flow Control: greetings.py

raw_input = input('Give me some input\n')
spam = int(raw_input)

if spam == 1:
    print('Hello')
elif spam == 2:
    print('Howdy')
else:
    print('Greetings!')
