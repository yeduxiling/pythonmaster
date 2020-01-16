# 这个程序要实现的功能是获取剪贴板中的文本，将文本的每一行前加上*号，然后将文本复制回剪贴板
import pyperclip
text = pyperclip.paste()
# 将文本赋值为剪贴板中的字符串内容
lines = text.split('\n')
#将复制的整个字符串使用split方法以\n 为间隔进行分割，输出的是一个列表，每一行是一个值。
for i in range(0, len(lines)):
    lines[i] = '*' + lines[i] + '*'
# 将每一行前面加上 *号，注意此时的lines 是列表不是字符串，最终要输出的还是字符串
text = '\n'.join(lines)
print(text)

pyperclip.copy(text)
