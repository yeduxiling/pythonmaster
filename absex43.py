"""
如果输入的成绩在90分以上（含90分）输出A；80分-90分（不含90分）输出B；70分-80分
（不含80分）输出C；60分-70分（不含70分）输出D；60分以下输出E。
"""

score = float(input("请输入分数(0-100分)："))
if score<0 or score >100:
    score = float(input('本次考试分数在0-100之间，你输入的分数超过范围，请重新输入！\n'))
else:
    if score >= 90:
        grade = 'A'
    elif score >= 80 and score < 90:
        grade = 'B'
    elif score >=70 and score < 80:
        grade = 'C'
    elif score >= 60 and score <70:
        grade = 'D'
    else:
        grade = 'E'
    print(f'本次考试得分{score}分，评分等级为：{grade}')
