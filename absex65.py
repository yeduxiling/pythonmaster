f = open('/tmp/test-file.txt', 'w')
f.write('first line\nsecond line\nthird line\n')
f.close()

f = open('/tmp/test-file.txt', 'r')
s = f.readline().strip()
print(s)
s = f.readline().strip()
print(s)
f.close()
