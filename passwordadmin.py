#账号管理器程序，通过主控密码管理管理区，通过账号调取对应的密码
import sys, pyperclip
password = {'orcafang@163.com':'753q951w789e123r', 'qq653933809':'7412q9632w',
           'wx15092107662':'753q951w789e123r', 'appid':'753Q951w789e123R'}

import sys
if len(sys.argv) < 2:
    print("缺少信息，运行这个程序需要输入文件名和需要查询的账户信息，如'orcafang@163.com'")
    sys.exit()

account = sys.argv[1] #获取要查询的账户的信息，并将其赋值为account
if account in password:
    pyperclip.copy(password[account])
    print(f"{account}账户的密码已经复制到剪贴板，请直接粘贴使用")
else:
    print(f"{account}账户不存在，请确认后再输入")
