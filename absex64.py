f = open('/tmp/test-file.txt', 'w')
f.write('first line\nsecond line\nthird line\n')
f.close()

f = open('/tmp/test-file.txt', 'r')
s = f.read()
print(s)
f.close()
