import random
n = 3
a_list = [random.randrange(65, 91) for i in range(n)]
b_list = [chr(random.randrange(65,91) )for i in range(n)]
print(a_list)
c_list = a_list + b_list + a_list * 2
print(c_list)

# 在c_list末尾增加一个元素
c_list.append('100')
print(c_list)

# 清空序列
print()
print(a_list)
a_list.clear()
print(a_list)

print()
# 复制一个列表
d_list = c_list.copy()
print(d_list)
del d_list[6:8]
print(d_list)
print(c_list)  # 从c_list进行了复制，但是删除操作不会影响c_list原本的赋值

print()
# 展示复制 .copy（）方法与赋值 = 的不同
e_list = d_list
print(d_list)
print(e_list)
del e_list[6:8]
print(d_list)
print(e_list)  #由于赋值采用的是引用的方式，因此在del e_list 的值的同时，d_list引用的列表值也被del 列表值改变

# 在末尾追加一个列表
print()
print(a_list)
a_list.extend(c_list) #相当于a_list + c_list
print(a_list)

# 在索引的某个位置插入一个元素
print()
print(a_list)
a_list.insert(1, 'example') # 在索引值为1的位置插入字符串 'example'
a_list.insert(3, 'elephant') # 在索引值为3的位置插入字符串 'elephant'
print(a_list)

# 排序

#  a_list.sort() 会报错，因为列表中的元素由 str 和 int组成

print()
print(a_list)
a_list.reverse()
print(a_list)
x = a_list.reverse()
print(x)  #reverse()只是对当前序列进行操作，不返回逆序的列表,所以需要打印才能显示，返回值是None
