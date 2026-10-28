# task 7
p = 0 # положительные
m = 0 # отрицательные
o = 0 # нулевые
num = [24, 43, 53, 66, 6, -3 ,-45, 0, 0, -595]
for i in num:
    if i < 0 :
        m +=1
    elif i == 0:
        o +=1
    else:
        p +=1
print(p, m, o)
# task8
count = []
num = [24, 43, 53, 66, 6, -3 ,-45, 0, 0, -596]
for i in num:
    if i%2 == 0:
        count.append(i)
print(count)
# task9
polo = []
num = [24, 43, 53, 66, 6, -3 ,-45, 0, 0, -596]
l = len(num)
for i in range(l):
    if i >= 0 :
        polo.append(i)
    else:
        polo.append(0)
print(polo)
# task10
en = []
n = 0
sum = 0
num = [24, 43, 53, 66, 6, -3 ,-45, 0, 0, -59]
for i in num:
    n +=1
    sum += i
midle = sum/n
for i in num:
    if i > midle:
        en.append(i)
print(en)

