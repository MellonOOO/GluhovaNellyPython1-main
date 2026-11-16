"""r = range(10, 100, 3)
for i in r :
    print(i)
l = list(r) # = l = [ i for i in r ]
print(l)"""
nums = [-3, 2, -5, 0 , 10, -20]
sts = ["дом", "семья", "фарсаж"]
def cond(n:int) -> bool:
    return  n <= 5 and n % 2  == 0

print(cond(0))
cond = lambda  n: n <= 5 and n % 2  == 0
print(cond(3))
foo = cond
print(foo)
def action(s: str):
    return len(s)
out = filter(cond, nums)
for i in out:
    print(i)
# lambda - функция без имени
out = filter(lambda n: n <= 5 and  n % 2 == 0, nums)
out_map = list(map(lambda s: s.strip(), sts))
print(sts , list(out_map))
print(nums,  list(out))
# фильтр работает только 1 раз
