#w1 = [int(i) for i in input().split()]
#w2 = [int(i) for i in input().split()]

w2 ={"молоко":20,"мороженное":10,"сырок":7,"сыр":12}
w1 ={"творог": 3,"сырок":17,"ряженка":4,"сыр":8}
out = w1.copy()
for i in w2:
    if i not in out:
        out[i] = w2[i] + out.get(i, 0)

print(out)