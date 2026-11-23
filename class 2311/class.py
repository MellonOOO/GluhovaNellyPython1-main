s ="hello"
sps = "I" + "am a student"
fs = "мне %f.3 лет, меня зовут %s" % (50, "вася") # метки, %d = num, %s = str , %f - дробные числа перед ф можно обозначить количество знаков после запятой

avg =4.33333333333
yar = 2010
movie_name = "begining"
fs = f"мой лубимый фильм - {movie_name}. он вышел в {yar} году"


groceries = [122, 323, 33, 3]
ex = f"итого : {sum(groceries)} рублей"
print(ex)

num = 4625.2213123


formats = f"{{{num:,.1f}, {-num:+}, {0.43:.1%}, {int(num):b}, {752:x}}}"
forms = "Я учусь на {} курс. мой средний бал {:.2f}".format(4, avg)
print(fs)
print(formats)