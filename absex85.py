"""用户输入一个数，程序判断它是不是素数（质数）"""
"""素数的定义为，大于1的自然数中，只能被1和本身整除的数"""

n = int(input("请输入一个自然数："))
def is_prime(m):
    for i in range(2, n):
        if n % i != 0:
            return True
        else:
            return False

if is_prime(n) and n != 1 and n !=2:
    print(f"{n}是一个质数。")
else:
    print(f"{n}不是一个质数")
