"""# task 11
s = [int(i) for  i in input(">).split()]
out = list(filter(lambda n: n > 0, s ))
print(out)
# task 12
s = [int(i) for  i in input(">).split()]
out = list(filter(lambda n: n % 3 == 0 or  n % 5 == 0, s ))
print(out)
# task 13
s = [int(i) for  i in input(">").split()]
d = [int(i) for  i in input(">").split()]
out = list(filter(lambda n: n in range(d[0], d[1] +1), s ))
print(out)
range(d[0], d[1])
# task 14
files = input(">").split()
out = list(filter(lambda s: s.split(".")[-1].lower == "py", files))
print(out)
# task 15
dubls = input(">").split(",")
names = [i.split()[0] for i in dubls]
marks = [i.split()[-1] for i in dubls]
jouranal = {}
for i in range(len(names)):
    if int(marks[i]) > 60:
        jouranal[names[i]] = int(marks[i])
print(jouranal)
# task 15.2
dubls = input(">").split(",")
def check(i):
    m = i.split()[-1]
    if int(m) >= 60:
        return True
    return False
out = list(filter(check, dubls))
print(out)
# task 16
s = input(">").lower().split(",")
out = list(filter(lambda i: len(i)>= 2 and i[0] == i[-1] ,s ))
print(out)
# task 17
s = input(">").split(",")
out = list(filter(lambda i:  int(i.split()[0]) >= 300 and i[-1] == "1", s))
print(out)
# task 18
s = input(">").split()
out = list(map(int, s))
print(out)
# task 19
s = input(">").split(",")
out = list(map(lambda i : i.strip().capitalize(), s))
print(out)
# task 20
s = input(">").split()
out = list(map(lambda i: i[0] + i[-1], s ))
print(out)
# task 21
s = map(int, input(">").split())
out = list(map(lambda i: divmod(i, 60), s))
print(out)"""
# task 22







