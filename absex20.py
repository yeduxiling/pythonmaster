def spam():
    # 这里定义的eggs是局部变量，只在函数spam中起作用
    eggs = 31337
    print(eggs)
spam()
# 这里定义的eggs是全局变量，对全局都有效，局部变量和全局变量可以用同一个函数名称，比如eggs
eggs = 8848
print(eggs)
