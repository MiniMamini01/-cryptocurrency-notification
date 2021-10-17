

while True:
    print('hello')
    with open('what.txt','r') as a :
        data = a.read().strip()
        if data == 'quit':
            quit()