from q1 import *
import random
m = int(input())
n = int(input())
a = [[0]*m]*n
for i in range(len(a)):
    for j in range(len(a[1])):
        a[i][j] = random.randint(0, 10)
print(a)
print("sum :", sum(a))
print("max: ", max(a))
print("mean : ", mean(a))
print("median : ", median(a))
k = mode(a)
print("mode : ", k)
print("standard deviation : ", std_deviation(a))
print("frequency distribution : ", freq_distr(a))
