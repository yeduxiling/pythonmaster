import random
n = 3
a_list = [random.randrange(65,91) for i in range(n)]
b_list = [chr(random.randrange(65, 91)) for i in range(n)]
print(a_list)
c_list = a_list + b_list + a_list * 2
print(c_list)

print()
print(c_list[3])
print(c_list[:])
print(c_list[5:])
print(c_list[:3])
print(c_list[2:6])

print()
del c_list[3]
print(c_list)
del c_list[5:8]
print(c_list)

print()
c_list[1:5:2] = ['a', 2]

print(c_list)
