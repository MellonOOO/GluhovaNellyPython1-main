"""try:
    num = int(input("> введите число от 1 до 100"))
    while num not in range (1 , 100):
        num = int(input("> введите число от 1 до 100"))
except ValueError as error:
    print(type(error))
except NameError as error:

    num = -1
except TypeError:
    num = int(input("> введите число от 1 до 100"))
else:
    print(" no error")
finally:
    print("ввод завершен")
print(num)"""
def avg(* numbers):
    s = 0
    c = 0
    for i in numbers:
        s =+ i
        s += 1
    return s/c