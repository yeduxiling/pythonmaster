#.format代表把括号中带的参数，分别插入到原位置对应的可插入空间上。format被称为格式化函数
在变量中引用函数的格式为变量名.函数(输入值)

formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
      "Try your",
      "Own text here",
      "Maybe a poem",
      "Or a song about fear"
))
