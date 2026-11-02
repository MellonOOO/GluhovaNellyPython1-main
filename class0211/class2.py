
marks = [int(i) for i in input().split()]

out = {}
for i in marks:
    if i in out:
        out[i]+=1
    else:
        out[i]=1
print(out)
print(out[5])