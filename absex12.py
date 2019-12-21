# range 函数，range(a, b, c) 在a到b的范围内以步长值c取值，取值中包含a,但不包含b,是[a,b）的关系，如果步长值 c缺省，则默认为1，a/b/c都可以为负数,c的值不可为0

for i in range(2, 17):
    print(i)


for n in range(2, 17, 3):
    print(i)

for m in range(2, 17, -1):
    print(m)

for l in range(2, 10, 0):
    print(l)
