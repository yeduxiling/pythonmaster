def chai(list):
    m = len(list)
    for n in range(len(list)):
        out = ", ".join(list[n - 1])
        out_put = out + 'and ' + list[m - 1]
    print(out_put)

list = ["古力穷哈", "迪丽热妈", "丑笔畅", "陈立农"]
chai(list)
