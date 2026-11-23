import math
"""def get_num():
    while True:
        n = int(input("введите число от 1 до 99\n"))
        while n not  in range:
            n = int(input("введите число от 1 до 99\n"))
n =input("введите число от 1 до 99\n")"""











def sqrt(n:float, acc:int=5) -> float:
    if n < 0:
        raise ValueError("корень только для положительных")
    for i in range(0, int(n)+ 1):
        if i ** 2 >n :
            up = i
            low = i -1
            break
    k = math.ceil(math.log2(10**acc)) +2
    for i in range(k):
        mid = (up+low)/2
        if mid ** 2 >= n :
            up = mid
        else:
            low = mid
    return (mid*10**(acc+1))/ 10**(acc+1)

print(sqrt(300))
