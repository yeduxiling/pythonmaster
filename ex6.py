# 设定变量 types_of_people 的值为10
types_of_people = 10

# 设定变量x的值，引用格式化字符 types_of_people
x = f"There are {types_of_people} types of people."

# 设定变量binary 的值为 binary
binary = "binary"
# 设定变量do_not 的值为 don't
do_not = "don't"
# 设定变量y 的值为字符串嵌套引用格式化字符 {binary} 和 {do_not}
y = f"Those who know {binary} and those who {do_not}."

# 打印x
print(x)
# 打印y
print(y)

# 打印字符串，并引用格式化字符 {x}
print(f"I said: {x}")
# 打印字符串，并引用格式化字符 {y}
print(f"I also said: '{y}' ")

# 设定变量 hilarious 值为字符串
hilarious = 10
# 设定变量 joke_evaluation 值为字符串，并且可引用其他变量 类似于函数？
joke_evaluation = "Isn't that joke so funny?! {}"

# 打印变量joke_evaluation ,并引用变量hilarious
print(joke_evaluation.format(hilarious))

# 设定变量w值为字符串
w = "This is the left side of..."
# 设定变量e值为字符串
e = "a string with a right side."
# 打印w和e的拼接
print(w + e)
