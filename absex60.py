import random
n = 3

a_list = [random.randrange(65, 91) for i in range(n)]
print(a_list)

# 插入
print()
a_list.insert(1, 'example') # 在索引值为1的位置插入元素 example

#删除
print()
print(a_list)
a_list.remove('example') # 删除example元素；如果有多个example元素，则只删除第一个
print(a_list)

# pop()用于删除并返回被删除的值

print()
print(a_list)
p = a_list.pop(2) # 删除索引值为2的元素，并将返回值赋予p
print(a_list)
print(p)

# pop()与del 或者remove（）的区别
print()
a_list.insert(2, 'example')
a_list.insert(2, 'example')
print(a_list)
del a_list[2]
print(a_list)

print()
print(a_list.remove('example')) # a_list.remove()这个Method的返回值是None
print(a_list)
