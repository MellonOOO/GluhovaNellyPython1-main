# # 1
# name = input()
# print(name.capitalize())
# #
# # #2
# word = input()
# print(word.upper())
#
# #3
# u = input()
# print(u.strip())
#
# #4
# i = input()
# print(i.replace(" ", "_"))
#
# #5
# A = input()
# print(A.lower().count("a"))

#6
line = input()
word1 = input()

if word1 in line:
    print("Слово есть")
else:
    print("Слова нет")
#7

file = input()
if file.endswith(".txt"):
    print("Файл есть")
else:
    print("Нету такого расширения")

#8

vol = "аяеёюэщтуы"
vol = vol + vol.upper()
c = 0
s = input()
for i in s:
    if i in vol:
        c += 1
print(f"{c} гласных")

#9
import string
c = 0
s = input()
for i in s:
    if i in string.digits:
        c += 1
print(f"{c} цифр")

#10
s = input()
s = s.split()
print(len(s))

#11

name1 = input()
lon = ""
for word in name1.split():
    if len(word) > len(lon):
        lon = word
print(lon)

#12

name2 = input()
lon1 = ""
for word in name2:
    lon1 = word + lon1
print(lon1)
print(name2[::-1])

#13























a = [i**2 for i in range(10) if i % 3 != 0]
print(a)
b = [int(i) for  i in input().split()]
print(b)
x, y = [int(i) for i in input().split()]
print(x)
print(y)

















