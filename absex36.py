while True:
    age = str(input("请输入你的年龄："))
    if age.isdecimal():
        break
    print('输入的年龄必须为数字，请再次输入')

while True:
    password = str(input("请输入密码（密码只能是字母或数字）"))
    if password.isalnum():
        break
    print("密码必须是字母或数字，请重新输入")
