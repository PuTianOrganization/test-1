attrs = ["筋骨", "敏捷", "气势", "反应", "技巧", "内力"]
tables = [['萧峰', 20, 17, 20, 20, 18, 19],
          ['杨过', 18, 19, 17, 20, 18, 18],
          ['令狐冲', 12, 17, 14, 20, 19, 13],
          ['张无忌', 20, 17, 15, 14, 20, 20],
          ['郭靖', 19, 18, 19, 18, 19, 20]]
# 总得分
totalScore = []
for i in range(len(tables)):
    total = 0
    for j in range(len(attrs)):
        total += tables[i][j + 1]
    totalScore.append(total)
mapper = list(zip([tables[i][0] for i in range(len(tables))], totalScore))
print("总得分: ", end="")
print(mapper)
# 平均分
avgScore = []
for i in range(len(attrs)):
    total = 0
    for j in range(len(tables)):
        total += tables[j][i + 1]
    avgScore.append(round(total / len(attrs), 2))
print("平均分: ", end="")
print(list(zip(attrs, avgScore)))
# 总分最高
maxScore = max([mapper[i][1] for i in range(len(mapper))])
for i in range(len(mapper)):
    if mapper[i][1] == maxScore:
        print("总分最高: " + mapper[i][0])



