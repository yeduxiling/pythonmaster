import random
r = random.randrange(1, 1000)
# 引入随机数r,r的范围为1 - 10000

if r % 2 == 0:
    print(r, 'is even.')
else:
    print(r, 'is odd.')
