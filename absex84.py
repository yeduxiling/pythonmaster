n = int(input('请输入一个数：'))

def is_positive(n):
    if n > 0:
        return True
    else:
        return False

if is_positive(n):
    print(f"{n}是个正数")
else:
    print(f"{n}不是正数")
