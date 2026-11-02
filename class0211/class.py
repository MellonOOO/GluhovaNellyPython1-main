
#tu = (4, 5, 6)# картеж - tuple

""""for i in range(3):
    print(names[i], marks[i], sep=",", end=",")"""""

bad_table =[["вас", 4],["мас", 5],["бас", 3]]

table = {"вас": 5, "мас": 4, "бас":3}
print(table["вас"])
#ключом может быть int , str, float-be , tuple
# не может list, tuple, object
#print(table[None])
#if "кас" not  in table:
#    table["кас"] = 4
print(table.get("кас", 0))
print(table.get("вас", 0))
table["вас"] = 3
print(table)
#del table["мас"]
# метот pop
#print(table.pop("вас", 0 ))
print(table)
for i in table:
    print("студент",i)
    print("оценка", table[i])
a = list(table.keys())
b = list(table.values())
c = table.items()
print(c)

