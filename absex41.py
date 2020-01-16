# 判断输入年份是否为闰年,
# 根据闰年的定义，普通闰年为：年份为4的倍数，且不是100的倍数。世纪闰年为400的倍数为闰年。
"""
def is_leap(year):
    if year % 4 == 0 and year % 100 != 0:
        print(f"{year}年是闰年。")
    elif year % 400 == 0:
        print(f"{year}年是闰年。")
    else:
        print(f"{year}年不是闰年。")

year = int(input("请输入您要查询的年份："))
is_leap(year)
"""

# 简化版，一句判断
def is_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year}年是闰年。")
    else:
        print(f"{year}年不是闰年。")

year = int(input("请输入您要查询的年份："))
is_leap(year)
