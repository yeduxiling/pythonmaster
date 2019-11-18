# 使用 变量名 = 值 的方式来定义变量，变量的值可以是数值，可以是字符串，也可以是其他变量的运算结果
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


print("There are", cars,"cars available.")
print("There are only", drivers,"drivers available.")
print("There will be", cars_not_driven,"empty cars today.")
print("We can transport", carpool_capacity,"people today.")
print("We have", passengers,"to carpool today.")
print("We need to put about", average_passengers_per_car,"in each car.")
print(cars / space_in_a_car)

#在打印的字符串中如果出现了变量，则在字符串前用f代表打印的字符串中会引用格式化变量
print(f"There are {cars} cars available.")
print(f"There are only {drivers} drivers available.")
print(f"There will be {cars_not_driven} empty cars today.")
print(f"We can transport {carpool_capacity} people today.")
print(f"We have {passengers} to carpool today.")
print(f"We need to put about {average_passengers_per_car} in each car.")
print(cars / space_in_a_car)
