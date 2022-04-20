import sys
print('My name is')
for i in range(5):
    print('Jimmy Five Times  ('+ str(i) +') ')

while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + '.')
