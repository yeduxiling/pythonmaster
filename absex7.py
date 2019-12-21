# while True 起手，使用 while True if break 定式，表示只有当if语句成立时才中断循环，否则循环持续
while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue
    print('Hello,Joe. What is the password?(It is a fish.)')
    password = input()
    if password == 'swordfish':
    break
print('Access granted.')
