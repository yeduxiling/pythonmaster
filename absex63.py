import os

f = open('/tmp/test-file.txt','w')
print(f.name)
f.close() # 需要先关闭文件，才能删除文件
if os.path.exists(f.name):
    os.remove(f.name)
    print(f'{f.name} deleted')
else:
    print(f'{f.name} dose not exist')
