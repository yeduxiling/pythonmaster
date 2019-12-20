"""
使用input()函数获取输入的字符串
使用int()将输入的字符串转化为整数
使用input()输出带占位符的字符串
"""
a = int(input('a = '))
b = int(input('b = '))

print(f"{a} + {b} = {a + b} ")
print('%d - %d = %d'% (a, b, a - b))
print('%d * %d = %d'% (a, b, a * b))
print('%d / %d = %d'% (a, b, a / b))
print('%d // %d  = %d'% (a, b, a // b))
print('%d %% %d = %d'% (a, b, a % b))
print('%d ** %d = %d'% (a, b, a ** b))
