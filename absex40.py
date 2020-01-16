#输入圆的半径，计算圆的周长和面积
import math

r = float(input('请输入圆的半径（cm）:'))

c = 2 * math.pi * r
c_1 = '%.2f' % c

area = math.pi * (r **2)
area_1 = '%.2f' % area

print(f'半径为{r}cm的圆，其周长为{c_1}cm，面积为{area_1}cm²')
