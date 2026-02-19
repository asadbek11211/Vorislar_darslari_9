# # """
# #     9-sinf
# #     25.10.2025
# #     Ro'yhatlar bilan ishlash. Methodlar va function lar bilan ishlash
# #     methods(.sort())
# #     function(sum(), min(), max(), sorted(), list(),range())
# #     Ro'yhatlardan nusxa olish
# #     Tuple() o'zgarmas ro'yhat
# # """

# # # davlatlar = ["Uzbekiston","Brazilya","Ispaniya","Vatikan","Qazaqistan","Turkiya"]
# # # moshinalar = list(('BMW','audi','tico','damas','depal s07','depal sl03','onix'))
# # # sonlar = list((2,1,7,3,-9))

# # # print(sonlar)
# # # print(davlatlar)
# # # print(moshinalar)

# # # moshinalar.sort()
# # # print(moshinalar)

# # # sonlar.sort(reverse=True)
# # # print(sonlar)

# # # sonlar1 = list(range(0,21))
# # # print(sonlar1)

# # # sonlar2 = list(range(-80,523,3))
# # # #print(sonlar2)
# # # print(len(sonlar2))

# # #sonlar3 = [89,-98,63,-2,-96,98,32,120,157,369,895,1235,2558,-75]
# # # minn = min(sonlar3)
# # # maxx= max(sonlar3)

# # # print(sum(sonlar3))

# # # davlatlar = ["Uzbekiston","Brazilya","Ispaniya","Vatikan","Qazaqistan","Turkiya"]

# # # country = davlatlar[:]

# # # print("davlatlar nomli royhat :",davlatlar)
# # # print("country nomli royhat :", country)

# # # country.insert(0,"Singapur")
# # # print(country)

# # # print(davlatlar)
# # # print(country)

# # # toqson = list(range(1,21,2))
# # # print("Asl lo'rinishi :", toqson)
# # # print("1 dan 7 gacha :", toqson[0:4])
# # # print(toqson[:])

# # # Tuple o'zgarmas ro'yhat

# # ismlar = ["elbek","ixtiyor"]                     # oddiy royhat
# # familyalar = ("karimboyev", "abdullayev","Toxtoboyev")         # Ozgarmas royhat (tuple)

# # print("Oddiy royhat :",ismlar)
# # print("Ozgarmas royhat (tuple) :",familyalar)

# # ismlar.append("sardor")
# # print(ismlar)

# # # familyalar.append("toshboyev")      # xatolik beradi, tuple ga yangi element qo'shib bo'lmaydi
# # # print(familyalar)

# # o_familyalar = list(familyalar)  

# # print(o_familyalar)    # tuple ni list ga aylantirib olamiz
# # o_familyalar.append("toshboyev")  
# # print(o_familyalar)   # endi yangi element qo'sh

# # familyalar = tuple(o_familyalar)   # list ni yana tuple ga aylantirib olamiz
# # print(familyalar)









# #1 O'zingizga ma'lum davlatlarning ro'yxatini tuzing va ro'yxatni konsolga chiqaring
# davlatlar = ["O'zbekiston", "AQSh", "Rossiya", "Xitoy", "Hindiston"]
# print(davlatlar)

# #2 Ro'yxatning uzunligini konsolga chiqaring

# print(f"Ro'yxatdagi davlatlar soni : {len(davlatlar)} ga teng")

# #3 sorted() funktsiyasi yordamida ro'yxatni tartiblangan holda konsolga chiqaring

# print(f"Davlatlarning tartiblangan ko'rinishi : {sorted(davlatlar)}")

# #4 sorted() yordamida ro'yxatni teskari tartibda konsolga chiqaring
# print(f"Davlatlarning teskari tartiblangan ko'rinishi : {sorted(davlatlar, reverse = True)}")

# #5 Asl ro'yxatni qaytadan konsolga chiqaring
# print(davlatlar)

# #6 reverse() metodi yordamida ro'yxatni ortidan boshlab chiqaring
# davlatlar.reverse()
# print(davlatlar)

# #7 sort() metodi yordamida ro'yxatni avval alifbo bo'yicha, keyin esa alifboga teskari tartibda konsolga chiqaring.
# davlatlar.sort()
# print(f"Alifbo boyicha tartiblangan royxat : {davlatlar}")

# davlatlar.sort(reverse=True)
# print(f"Alifboga teskari tarzda tartiblangan royxat : {davlatlar}")

# # 8 120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing
# juft_sonlar = list(range(120, 1201, 2))
# print(juft_sonlar)

# # 9 Ro'yxatdagi sonlar yig'indisini hisoblang va konsolga chiqaring



import function 

function.darajaga_oshirish(5,3)
function.salomber('mohinur')
function.ishorani_aniqlash(0)