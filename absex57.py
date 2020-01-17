import random
n = 10
a_list = [random.randrange(1, 100) for i in range(10)]
print(f'a_list comprehends {len(a_list)} random numbers:\n' , a_list)

a_list.sort()
print('the list sorted:\n', a_list)

a_list.sort(reverse = True)
print('the list sorted reversely:\n', a_list)
