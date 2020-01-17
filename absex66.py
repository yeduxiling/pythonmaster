f = open('/tmp/test-file.txt', 'w')
f.write('first line\nsecond line\nthird line\n')
f.close()

f = open('/tmp/test-file.txt', 'r')
s = f.readlines()
print(s)
f.close()
