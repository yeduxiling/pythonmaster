import random

n = 10

a_list = [random.randrange(1, 100) for i in range(n)]
print(a_list)

b_list = [x for x in a_list if x % 2 == 0]
print(b_list)
