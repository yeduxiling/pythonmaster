# 猜数小游戏，
#规则：提示请输入1-10之间的数字，看看你多少次能够猜对。每次的目标数字随机生成，然后提示用户输入，如果输入的数字比目标数字大，则提示，大了，如果比目标数字小，则提示小了，如果相等，则提示，真厉害你猜对了！你用了多少次猜出了这个数字！
import random, sys
num = random.randint(1, 10)
i = 0
print("1-10之间猜一个数字，看看你能用多少次猜中！")
while True:
    i += 1
    answer = int(input("请输入你的答案："))
    if num > answer:
        print("你输入的数值小了，再大一些！")
    elif num < answer:
        print("你输入的数值大了，再小一些！")
    else:
        print(f"哇，你好厉害，猜对了！你一共用了{i}次猜对的！")
        sys.exit()
