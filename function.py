# Pythonda function bilan tanishish

# print("Assalomu alaykum")
# a = 34
# print(type(a))

# def salom_ber(ism):
#     print(f"Salom {ism} axvollaring yaxshimi")

# salom_ber("bobur")
# salom_ber("Kamolbek")


# def kopaytma(son1,son2):
#     """
#     Ikkita sonni ko'paytma ko'rinishida taqdim qiladigan function
#     """
#     print(f"{son1} * {son2} = {son1*son2}")
    
# kopaytma(9,74)

# Shart operatorlari if else

# son = -34.89

# if son > 0:
#     print("siz kiritgan son musbat")
# else:
#     print("Siz kiritgan son manfiy")


def darajaga_oshirish(a,b):
    """a sonining b inchi darajasini hisoblash funksiyasi"""
    print(f"{a} ** {b} = {a**b}")

def salomber(ism):
    """kiritilgan ismga qoshimcha matn yozib chiqaruvchi function"""
    print(f"Salom {ism.title()} ishlar, o'qishlar qanday ?")

def ishorani_aniqlash(son):
    """Kiritilgan sonni musbat, manfiy yoki nolga teng ekanini aniqlovchi function"""
    if son > 0:
        print("Siz kiritgan son  MUSBAT")
    elif son < 0:
        print("Siz kiritgan son  MANFIY")
    else:
        print("Siz kiritgan son nolga teng")


# def mashina_taklif_qilish(narx):
#     """Mijozning puliga qarab unga yetadigan moshinalar tavfsiya qilish function"""

# def orta_arfimetik(*sonlar):
#     """Siz kiritadigan sonlarning o'rta arfimetikini hisoblash function"""

# def orta_geometrik(*sonlar):
#     """Siz kiritadigan sonlarning o'rta geometrikini hisoblash function"""



# darajaga_oshirish(5,3)
# salomber('oyshajon')
# ishorani_aniqlash(-98)