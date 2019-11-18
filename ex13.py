# 引用python中sys模块中的argv 函数，argv函数是指在运行文件时，可以对程序传递参数
from sys import argv


# read the WYSS section for how to run this
script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
