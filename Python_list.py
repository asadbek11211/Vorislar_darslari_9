"""
    21.10.2025
    Python List Operations
"""

# ism = 'Bobur'
# uy_manzil = "toshkent shahar, chilonzor tumani"

# print(ism.capitalize())
# print(ism.upper())
# print(uy_manzil.capitalize())
# print(uy_manzil.title())


# # Pythonda List(royhatlar) bilan ishlash

# hayvonlar = ["mushuk", "hokiz", "ot", "sigr", "kuchuk"]
# oila = ["ota", 25, "ona", 22, "aka", 7, "uka", 5]
# mashinaalr = ["spark", "nexia", "gentra", "tracker"]

# hayvonlar = ["mushuk", "hokiz", "ot", "sigr", "kuchuk"]
# #  index       0         1       2      3       4 

# print(hayvonlar)  # mushuk
# qiymat = hayvonlar[3]
# print(qiymat)

# mashinaalr = ["spark", "nexia", "gentra", "tracker"]

# print(mashinaalr[0])
# print(mashinaalr[-1])
# print(mashinaalr[1].title())
# print(mashinaalr[-2].upper())

# IT_oquvchilar = []

# IT_oquvchilar.append("Ibrohim")
# IT_oquvchilar.append("Anvar")
# IT_oquvchilar.append("Jasur")
# IT_oquvchilar.append("Doston")
# print(IT_oquvchilar)

# IT_oquvchilar.insert(2, "SARVAR")
# IT_oquvchilar.insert(0, "KAMOLTOY")
# print(IT_oquvchilar)

"""
25.10.2025 ro'yhatlar davomi

"""

# moshinalar = ["mers","gentra","tico","malibu2","traker","BMW","aodi"]
# moshinalar.sort(reverse=True)
# print(moshinalar)

# print(sorted(moshinalar))
# print(sorted(moshinalar, reverse=True))

sonlar = [12, 34, 56, 78, 98, 13, -9, -89]
print(f"Asl korinishi : {sonlar}")
print(f"Tartiblangan korinishi : {sorted(sonlar)}")
print(f"Teskari Tartiblangan korinishi : {sorted(sonlar, reverse=True)}")

print(len(sonlar))

toq_sonlar = list(range(1,11,2))
print(toq_sonlar)