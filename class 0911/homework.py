import string
# task 1
sim = input()
print(ord(sim))
# task 2
first_sim = input()
second_sim = input()
if ord(first_sim) > ord(second_sim):
    print(ord(first_sim)-ord(second_sim))
else:
    print(ord(second_sim)-ord(first_sim))

# task 3
stroka = input()
fin_str = ""
k = int(input())
for i in stroka:
    if i != " ":
        sim = chr(ord(i) + k)
        if ord(sim) >= 122 - k:
            sim = chr(97+k + -((122 -ord(i))))
            fin_str += sim
        else:
            fin_str += sim
    else:
        fin_str += " "
print(fin_str)
# task 4
stroka = input()
eng_let = string.ascii_letters
count_eng_let = 0
for i in eng_let:
    if i in stroka:
        count_eng_let += 1
dig = string.digits
count_dig = 0
for i in dig:
    if i in stroka:
        count_dig += 1
pun = string.punctuation
count_pun = 0
for i in pun:
    if i in stroka:
        count_pun += 1
el_count = len(stroka) - count_pun - count_dig - count_eng_let

