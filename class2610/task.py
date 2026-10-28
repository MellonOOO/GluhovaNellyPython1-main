
# task 1
def square(num):
    num = num ** 2
    return num
result = square(9)
print(result)

# task 2
def count(num):
    if num % 2 == 0:
        return True
    return False
result = count(12)
print(result)

# task 3
def area(height, width):
    result = height * width
    return result
result = area(10, 9)
print(result)

# task 4
def triangle_area(height, base):
    result = height * base / 2
    return result
result = triangle_area(21, 3)
print(result)

# task 5
def quadratic_equation(a, b, c):
    D = b ** 2 - 4*a*c
    a = []
    if D > 0:
        x1 = (b * -1 + D ** 0.5) / (2*a)
        x2 = (b * -1 - D ** 0.5) / (2*a)
        a.append(x1)
        a.append(x2)
        return a
    elif D == 0:
        x = b * -1 / (2*a)
        a.append(x)
        return a
    return a
result = quadratic_equation(1, 2, 3)
print(result)

#task 6
def mid(*num):
    s = sum(num)
    n = len(num)
    mid = s/n
    return mid
result = mid(23,4,4, 234, 3, -50)
print(result)

# task 7
def count1(*num):
    a = []
    for i in num:
        if i % 2 ==0:
            a.append(i)
    return a
result = count1(12, 32,3, 23, 2)
print(result)

