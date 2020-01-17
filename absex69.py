import os

with open('/tmp/test-file.txt', 'w') as f:
    f.write('first line\nsecond line\nthird line\n')

with open('/tmp/test-file.txt', 'r') as f:
    for line in f.readlines():
        print(line)

if os.path.exists(f.name):
    os.remove(f.name)
    print(f'{f.name} deleted')
else:
    print(f'{f.name} does not exist.')
