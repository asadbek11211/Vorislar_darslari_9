# string , methods, f"" string

# ism = 'bobur'
# familya = 'murodov'
# otchestva = 'anvarovich'
# FIO = f"Assalomu alaykum {familya} {ism} {otchestva}!"

# print(FIO)
# print(f"Assalomu alaykum {familya.title()} {ism.title()} {otchestva.title()}!")

##### lower() , casefold() String malumotdagi barcha Katta harflarni kichik qiladi
# ism = 'IbadUlla Ahmedov'
# txt = "HeLlo, And Welcome To My World!"

# x = txt.casefold()

# print(x)
# print(ism.lower())

# center() String malumotning o'rtasiga bosh joy joylashtiradi
# txt = "banana"

# x = txt.center(50)

# print(x)

#count() String malumotda nechta ma'lum bir so'z yoki harf borligini hisoblaydi
# txt = "I love apples, apple are my favorite fruit"

# x = txt.count("I")

# print(x)

# endswith() String malumot ma'lum bir so'z yoki harf bilan tugashini tekshiradi
# txt = "Hello, welcome to my world."

# x = txt.endswith(" ")

# print(x)

#expandtabs() String malumotdagi tab belgilarini bosh joy bilan almashtiradi
# txt = "H\te\tl\tl\to"
# ism = 'K\tamolb\tek'
# x =  ism.expandtabs(0)

# print(ism)
# print(x)

# find() String malumotda ma'lum bir so'z yoki harfning indeksini qaytaradi
# txt = "Hello, welcome to my world."

# x = txt.find(".")

# print(x)


ism = input("Ismingizni kiriting: ")
yosh = int(input("Yoshingizni kiriting: "))
manzil = input("Manzilingizni kiriting: ")
maktab = input("Maktabingizni kiriting: ")
qiziqish = input("Qiziqishlaringizni kiriting: ")
jura = input("Yaqin insonlaringizni kiriting : ")

print(f"Hurmatli {ism.title()} ning yoshi {yosh} da, \n Manzili {manzil.title()} da joylashgan \n {maktab} maktabda o'qiydi. \n Uning qiziqishlari {qiziqish.title()} va Eng yaqin insonlari {jura.title()} dan iborat.")

ism = list('anvar','karim')
print(ism)