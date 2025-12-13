# A va B sonlari berilgan Ularning qiymatini almashtirib rezultat oling

# a = int(input("A sonini kiriting: "))
# b = int(input("B sonini kiriting: "))

# print(" A sonining qiymati A = ", b)
# print(" B sonining qiymati B =  ", a)


oquvchilar = []

for oquvchi in range(4):
    print(f"{oquvchi+1} - o'quvchini kiriting")
    oquvchi = {
        
        'ism':input('Ism kiriting :' ),
        'yoshi': input('yoshini kiriting : ')
    }
    oquvchilar.append(oquvchi)
print(oquvchilar)