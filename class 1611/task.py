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
range(d[0], d[1])"""
# task 14
files = input(">").split()
def sas(s):
    exp = s.split(".")[-1]
    return exp.lover() == "py"
out = list(filter(sas, files))
print(out)
