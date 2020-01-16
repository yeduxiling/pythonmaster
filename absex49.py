# 取 100以内的质数（大于等于2，且只能被1和本身整除的整数）
for n in range(2,100):

    if n == 2:
        print(n)
        continue
    for i in range(2, n):
        if (n % i) == 0:
            break
    else:
        print(n) 
