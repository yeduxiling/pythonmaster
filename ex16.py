from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print(f"If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print ("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line1: ")
line2 = input("line2: ")
line3 = input("line3: ")

print("I'm going to write these to the file.")

target.write(f"\n{line1} \n{line2} \n{line3}")

target = open(filename, 'r')
print(f"这是文档现在的内容：{target.read()}")

print("Add finally,we close it")
target.close()
