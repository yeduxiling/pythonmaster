"""
游戏规则：
1.机器人投骰子，玩家来猜，2个骰子，玩家猜大小，2个骰子之和大于7为大，小于7为小，等于7为平局；
2.玩家和机器人庄家都有10个硬币，玩家猜对一局得1硬币，猜错输1硬币，平局不扣硬币，机器人反之；
3.玩家或者机器人硬币为0，则游戏结束；
4.用户可以在猜数的过程中退出游戏。
"""

from random import randrange
coin_user, coin_bot = 10, 10
rounds_of_game = 0

def bet(dice, wager):
    if dice == 7:
        print(f"The dice is {dice};\nDRAW!\n")
        return 0
    elif dice < 7:
        if wager == 's':
            print(f"The dice is {dice};\nYou WIN!\n")
            return 1
        else:
            print(f"The dice is {dice};\nYou LOST!\n")
            return -1
    elif dice > 7:
        if wager == 's':
            print(f"The dice is {dice};\nYou LOST!\n")
            return -1
        else:
            print(f"The dice is {dice};\nYou WIN!\n")
            return 1

while True: #开始执行循环
    print(f"Your coin: {coin_user}\t Bot's coin:{coin_bot}")
    dice = randrange(2, 13)
    wager = input("What's your bet? (‘s’ means dice<7 ; 'b' means dice>7;'q' means quit )")
    if wager == 'q':
        break
    elif wager in "bs":   #如果玩家的答案中包含b或者s,再进行判断
        result = bet(dice, wager)
        # coin_user += result 表示玩家的硬币在游戏结束后加上对应的结果
        coin_user += result
        coin_bot -= result
        rounds_of_game += 1
    if coin_user == 0: #顺着前面的条件判断往下走，如果触发了该条件，则运行
        print("Woops, you'ver LOST ALL, and game over!")
        break
    elif coin_bot == 0:
        print("Woops, the robot's LOST ALL, and game over!")
        break
print(f"You've played {rounds_of_game} rounds.\n")
print(f"You have {coin_user}coins now. the robot has {coin_bot}coins now.\nBye!")
