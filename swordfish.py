while True:
    print('who are you')
    name = input()
    if name != 'god':
        continue
    print('hello god. What is the password')
    password = input()
    if password == 'swordfish':
        break
print ('Access granted')
