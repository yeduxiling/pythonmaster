import random, sys
num = random.randint(1, 100000)
i = 0
print("猜猜电脑现在想的数是多少(1-100000之间的整数)，看你多少次能猜对！")
while True:
    ans = int(input("请输入你猜的数："))
    i += 1
    if num > ans:
        print("你猜的数有点小了，再大些！")
    elif num < ans:
        print("你猜的数有点大了，再小些！")
    else:
        print(f"恭喜你猜对了！你一共用了{i}次猜对的。")
        sys.exit()
