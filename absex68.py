a_list = ['first line\n', 'second line\n', 'third line\n']
f = open('/tmp/test-file.txt', 'w')
f.writelines(a_list)
f.close()

f = open('/tmp/test-file.txt', 'r')
for line in f.readlines():
    print(line)
f.close()
