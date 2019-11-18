print("Mary had a little lamb.")

#在打印的字符串中如果有可替换的内容，则使用{}加后面用.format()的方式来进行引用
fleece = "Its fleece was white as {}"
color = "shit"

print(fleece.format(color))
print("Its fleece was white as {}. ".format('snow'))
print("And everywhere that Mary went.")
print("." * 10) # what'd that do?

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end. try removing it to see what happens
# 在打印字符串的最后加上,end=''代表不换行
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')
print(end7 + end8 + end9 + end10 + end11 + end12)
