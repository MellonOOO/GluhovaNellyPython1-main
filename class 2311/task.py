# task 1
"""name = input("введите имя >")
age = input("введите возраст >")
print(f"меня {name} зовут , мне {age} лет")
# task 2
name = input("введите имя >")
city = input("введите город >")
thing = input("введите предмет >")
print(
    f"\n Имя : {name}\n Город : {city}\n Любимый предмет : {thing}"
)
# task 3
num1 = int(input("введите 1 число >"))
num2 = int (input("введите 2 число >"))
print(f"Сумма :{num1+ num2}, разность :{num1-num2}, произведение : {num1*num2}, частное : {num1/num2}")
# task 4
name_cost = list(input("введите название товара и его цену>").split())
print(f"Товар : {name_cost[0]}, Цена : {name_cost[1]}")
# task 5
from itertools import count
mar = list(map(int,input("введите оценки>").split()))
print(f"{(sum(mar)/len(mar)):.2f}")
# task 6
temp = float(input("введите темпратуру>"))
print(f"{temp} = {temp*9/5 + 32}")
# task 7
name_cost_count = list(input("введите название товара , его количество и цену>").split())
print(f"{name_cost_count[0]}: {name_cost_count[1]} x {name_cost_count[2]} = {int(name_cost_count[1])*int(name_cost_count[2])}")
# task 8"""
a, b = float(input(">")), float(input(">"))
print(f" исходная цена {a}\n скидка {a/100*b:.2f}\n итого {a- (a/100*b)}")
# task



