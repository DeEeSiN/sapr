from task5 import task

str1 = '["1", ["2","3"],"4", ["5", "6", "7"], "8", "9", "10"]'
str2 = '[["1","2"], ["3","4","5"], "6", "7", "9", ["8","10"]]'
res = [["8", "9"]]
r = task(str1, str2)

print(r == res)