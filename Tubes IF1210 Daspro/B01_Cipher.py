import var

def isNumber(x):
    # Spesifikasi program : Mengecek apakah suatu elemen array merupakan angka
    # KAMUS
    # x : string
    # i : integer
    # Num : boolean
    # ALGORITMA
    Num = False
    i = 0
    while Num==False and i<10:
        if x==str(i):
            Num = True
        else : i+=1
    #{Num=True or i>=10}
    return Num

def isChr(x):
    # Spesifikasi program : Mengecek apakah suatu elemen array merupakan character
    # KAMUS
    # x : string
    # ord(x): integer
    # Chr : boolean
    # ALGORITMA
    Char = False
    if ord(x)>122 or ord(x)<65 or (ord(x)<97 and ord(x)>90):
        Char = True
    return Char

def isCap(x):
    # Spesifikasi program : Mengecek apakah suatu elemen array merupakan huruf kapital
    # KAMUS
    # x : string
    # ord(x): integer
    # Cap : boolean
    # ALGORITMA
    Cap = False
    if 65<=ord(x)<=90:
        Cap = True
    return Cap

def cipher(P):
    # Spesifikasi program : Merupakan subprogram utama yang akan mengkonversi password menggunakan fungsi cipher
    # KAMUS
    # i, asci, tempNum, asci: integer
    # isNumber(P[i]), isChr(P[i]), isCap(P[i]) : boolean
    # e, P: string
    # ALGORITMA
    n = var.length(P)
    e = ""
    for i in range(n):
        if isNumber(P[i]):                              # Kalau elemen password berupa angka
            tempNum = int(P[i])
            if tempNum>7: tempNum -= 3  
            else: tempNum +=3
            e += str(tempNum)
        else:
            if isChr(P[i]):                             # Kalau elemen passoword bukan huruf
                e += P[i]
            else:                                       # Kalau elemen password berupa huruf
                asci = ord(P[i])
                if isCap(P[i]):                         # Kapital
                    if 65<=asci<70: asci+=15
                    elif 70<=asci<=80: asci+=5
                    else:
                        if asci>84: asci-=1
                        else: asci+=1
                else:                           
                    if 97<=asci<=100: asci+=20
                    elif 100<asci<=110: asci+=10
                    else:
                        if asci>118: asci-=1
                        else: asci+=1
                e+=chr(asci)
    return e