x = int(input('请输入一个整数：'))
y = int(input('请输入另一个整数:'))


if x > y:
    x, y = y, x
for factor in range(x, 0, -1):
    if x % factor == 0 and y % factor == 0:
        print(f"{x}和{y}的最大公约数是：{factor}")
        print(f"{x}和{y}的最小公倍数是：", (x * y )/ factor)
    break
