import string

"""tup = (2, 3)
print(tup)
print(tup[1])
print(tup.index(2))"""
word = "hello"
l = word[0]
print(word)
print(l)
word += "!"
print(word)
print(word.index("l"))
char = "A"
mystery_char = chr(737)# что за буква под номером
print(mystery_char)
num = ord(char)# какой это символ по порядку
print(num)

#char = input()
n = 10
num = ord(char)
for i in range(n):
    num += 1
    print(num, chr(num))

print(string.ascii_letters)
print(string.hexdigits)
print(string.octdigits)
char = "а"
n = 31
num = ord(char)
s = chr(num)
for i in range(n):
    num += 1
    s += chr(num)
    #print( chr(num))
ruletters = s
print(ruletters)
