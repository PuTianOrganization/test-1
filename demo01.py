end = 300
# 所有数标记为素数
arr = [1 for i in range(end)]
# 删除0和1
arr[0] = arr[1] = 0
# 循环删除元素为1的下标对应的倍数
for i in range(2, end):
    if arr[i] == 1:
        for j in range(i + 1, end):
            if j % i == 0:
                arr[j] = 0
# 结果
ans = [i for i in range(end) if arr[i] == 1]
print(str(end) + "内素数: ")
print(ans)

