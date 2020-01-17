import re
with open('regex-target-text-sample.txt', 'r') as f:
    str = f.read()
pttn = r'beg[aui]ns?'
print(re.findall(pttn, str))
