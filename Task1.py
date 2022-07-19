# Вычислить число pi c заданной точностью d Пример:
# - при d = 0.001, π = 3.141    10^{-1} ≤ d ≤10^{-10}

import math
n=float(input('Введите желаемую точность (например 0.001): '))
count=0
while n%1!=0: 
    n*=10
    count+=1
print(round(math.pi,count))

