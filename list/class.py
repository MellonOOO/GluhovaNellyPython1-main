l = [1, 2, 3, 4, 5]
print(l)
l[0] = 6
if 1 in l :
    print("Yes")
else:
    print("No")
out = 1
for i in l :
    out *= i
    print(out)
l.append(6) # add
print(l)
l.remove(4) # remove
print(l)
l[0]=6
print(l)
del l[0] # удаление по индексу
print(len("fir-fir-fir"))
l.insert(1, "hi")
l.insert(1, "hello")
print(l)
c = l.index(6, 1)# первое появление
print(c)
l.pop(1)
print(l)