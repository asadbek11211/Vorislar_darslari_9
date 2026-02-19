def salom_ber(ism):
    print(f"Salom {ism} axvollaring yaxshimi. O'qishlarchi ?")

def kopaytma(son1,son2):
    """
    Ikkita sonni ko'paytma ko'rinishida taqdim qiladigan function
    """
    print(f"{son1} * {son2} = {son1*son2}")

def ishorani_aniqlash(son):
    if son > 0:
        print("Siz kiritgan son musbat")
    elif son < 0:
        print("Siz kiritgan son manfiy")
    else:
        print("Siz kiritgan son nolga teng")