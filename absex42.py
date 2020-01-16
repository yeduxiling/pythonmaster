weight_input = float(input("请输入重量："))
unit = input("请输入单位（磅/千克）：")

if unit == "千克" :
    weight_result = weight_input * 2.2046
    print(f"{weight_input}{unit}等于{('%.2f' % weight_result)}磅")
elif unit == "磅":
    weight_result = weight_input / 2.2046
    print(f"{weight_input}{unit}等于{('%.2f' % weight_result)}千克")
else:
    print("你输入的单位不对，无法计算")
