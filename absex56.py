import random
n = 3

#生成3个随机数，构建一个列表
a_list = [random.randrange(65, 91) for i in range(n)]
b_list = [chr(random.randrange(65, 91)) for i in range(n)]
print(a_list)
print(b_list)

c_list = a_list + b_list + a_list * 2
print(c_list)

a_list *= 3
print(a_list)

# 内建函数操作：len()/max()/min()
print(len(c_list))
print(max(b_list))  # 在内建函数内部进行异常处理，以比较字符和数字
print(min(b_list))

print('X' not in b_list)
