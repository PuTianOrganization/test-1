import string
import re

lowerCase = string.ascii_lowercase
upperCase = string.ascii_uppercase
digits = string.digits
punctuation = string.punctuation
level = ["弱强度", "中低强度", "中高强度", "高强度"]

# 输入
password = input("密码: ")
# 判断
safeLevel = -1
if len(password) < 6:
    print("密码长度不符合要求")
else:
    for char in password:
        if char == "":
            safeLevel = -1
            break
        if char in lowerCase:
            safeLevel += 1
            lowerCase = ""
        if char in upperCase:
            safeLevel += 1
            upperCase = ""
        if char in digits:
            safeLevel += 1
            digits = ""
        if char in punctuation:
            safeLevel += 1
            punctuation = ""
    if safeLevel > -1:
        print("安全强度等级: " + level[safeLevel])
    else:
        print("含有非法字符")

