def is_prime():
    n = int(input("请输入一个自然数："))
    if n == 1:
        print(f"{n}是素数。")
    if n > 1:
        for i in range(2, n):
            if n / i != 0:
                print(f"{n}是素数。")
            else:
                print(f"{n}不是素数。")

is_prime()
