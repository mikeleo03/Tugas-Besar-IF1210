import function as fun
def ubahS(cSv,M,col,row):
    # Spesifikasi program : Menambahkan game pada list
    # KAMUS
    # M : array [1..row] of array [1..col] of string
    # col, row, s, result : integer
    # Val,Found : boolean
    # ALGORITMA
    Id = str(input("Masukkan id game : "))
    Val = True
    Found = False
    for i in range (1,row):
        if Id==M[i][0]:
            Found = True
            break
    if Found:
        s = int(input("Masukkan jumlah : "))
        result = int(M[i][5]) + s
        if s>0:
            print("Stok game",M[i][1],"berhasil ditambah. stok sekarang : "+str(result))
            M[i][5] = str(result)
        else:
            if result>=0:
                print("Stok game",M[i][1],"berhasil dikurangi. stok sekarang : "+str(result))
                M[i][5] = str(result)
            else:
                print("Stok game",M[i][1],"gagal dikurangi. stok sekarang : ",M[i][5],"(<"+str(s)+")")
                Val = False
    else: 
        print("Tidak ada game dengan ID tersebut")
        Val = False
    # Jika stok berhasil diubah
    if Val:
        fun.writeCSV(cSv,M,col,row)


# Spesifikasi program : Menambahkan game pada list
# KAMUS
# file : csv
# GList : array [1..row] of array [1..col] of string
# NList : array [1..(row+1)] of array [1..col] of string
# ALGORITMA
file = open("game.csv",'r')
# Definisi baris dan kolom (didefinisikan sebelumnya)
col = 6
row = fun.count_row("game.csv")
GList = fun.OpenCSV(file,col,row) # Menginput csv ke dalam array
ubahS("game.csv",GList,col,row)