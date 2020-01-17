dinner_list = ['迪丽热妈', '古力穷哈', '丘比畅', '陈立农']
for n in range(0, len(dinner_list)):
    print("欢迎来参加我的晚宴," + dinner_list[n] )

print()
print('很遗憾' + dinner_list[2] + '无法参加晚宴了')
dinner_list[2] = '蒙丹'
print(dinner_list[2] + '老师' +'将出席晚宴')

print()
for n in range(0, len(dinner_list)):
    print("欢迎来参加我的晚宴," + dinner_list[n] )

print()
print()
for n in range(0, len(dinner_list)):
    print("欢迎来参加我的晚宴," + dinner_list[n] + ' ,我找到了一个更大的餐桌，可以邀请更多人参加')

dinner_list.insert(0, '陈·阿扎尔')
dinner_list.insert(2, '周丽娜')
dinner_list.append('朱军')

print()
for n in range(0, len(dinner_list)):
    print("欢迎来参加我的晚宴," + dinner_list[n] )

print()
for n in range(0, len(dinner_list)):
    print("欢迎来参加我的晚宴," + dinner_list[2] )

print()
for n in range(0, len(dinner_list)):
    print("欢迎来参加我的晚宴," + dinner_list[4] )

bye_bye = dinner_list.pop(0)
print()
print('很抱歉，因为桌子没到，你不能参加我的晚宴了' + bye_bye)

bye_bye = dinner_list.pop(1)
print('很抱歉，因为桌子没到，你不能参加我的晚宴了' + bye_bye)

bye_bye = dinner_list.pop(3)
print('很抱歉，因为桌子没到，你不能参加我的晚宴了' + bye_bye)

bye_bye = dinner_list.pop(2)
print('很抱歉，因为桌子没到，你不能参加我的晚宴了' + bye_bye)

bye_bye = dinner_list.pop(0)
print('很抱歉，因为桌子没到，你不能参加我的晚宴了' + bye_bye)

print()
for n in range(0, len(dinner_list)):
    print("欢迎来参加我的晚宴," + dinner_list[n] )

print()
del dinner_list[0:2]
print(dinner_list)
