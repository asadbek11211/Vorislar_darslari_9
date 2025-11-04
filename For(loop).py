

# ismlar = ['Ali', 'Vali', 'Hasan', 'Husan', 'Olim']
# for ism in ismlar:
#     print(f"Salom {ism}, ishlaring yaxshimi?")

# for son in list(range(1,11)):
#     print(f"{son} ning kvadrati {son**2} ga teng")

# print("a soni b sonidan kichik bolsin(a < b)")
# a = int(input("a ga butun son kiriting: "))
# b = int(input("b ga butun son kiriting: "))
# sonlar = []
# for son in range(a, b+1):
#     sonlar.append(son)
# print(f"{a} dan {b} gacha bolgan sonlar: {sonlar}")
# print(f"{a} dan {b} gacha {len(sonlar)} ta son bor")


# print("a soni b sonidan kichik bolsin(a < b)")
# a = int(input("a ga butun son kiriting: "))
# b = int(input("b ga butun son kiriting: "))
# sonlar = []
# for son in range(a-1, b):
#     sonlar.append(son)
# print(f"{a} dan {b} gacha bolgan sonlar: {sorted(sonlar, reverse=True)}")
# print(f"{a} dan {b} gacha {len(sonlar)} ta son bor")

# sonlar = []
# yigindi = []
# n = int(input("n ga butun son kiriting: "))
# for son in range(1,n+1):
#     korinish = f"1/{son}"
#     sonlar.append(korinish)
#     yigindi.append(1/son)
# print(f"formula {sonlar} \n yigindi: {sum(yigindi)}")

# son = list(range(2,3))
# print(son)

# n = int(input("n ga butun son kiriting: "))
# royhat = []
# for son in range(1, n+1):
#      for daraja in range(son,son+1):
#          korinish = f"{son}^{daraja}"
#          royhat.append(korinish)
#          yigindi = son**daraja
# print(f"formula: {royhat} \n yigindi: {yigindi}")

#1-masala
# print("n > 0")
# k = int(input("k nonini kiriting : "))
# n = int(input("n nonini kiriting : "))

# for son in range(1,n+1):
#     print(f"{son}-sikl : {k}")

#2-masala

a = int(input("a nonini kiriting : "))
b = int(input("b nonini kiriting : "))
sonlar = list(range(a,b+1))
for son in sonlar:
    print(son)
print(len(sonlar))










