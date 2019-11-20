name = input('请输入用户名> ')
password = input('请输入密码> ')

if name == 'Mary':
    print('Hello Mary')
    if password == 'swordfish':
        print('Access granted')
    else:
        print('wrong password')
