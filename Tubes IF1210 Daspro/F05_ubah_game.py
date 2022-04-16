import function as fun
def ubahG(cSv,M,col,row):
    # Spesifikasi program : Menginput perubahan data game yang baru ke dalam matriks (selain id dan stok pada game)
    # KAMUS
    # cSv : csv
    # M : array [1..row] of array [1..col] of string
    # i : integer
    # Found : boolean
    # Id, nama, kategori, tahun_rilis, harga : string
    # newGame : array [1] of array [1..6] of string
    # newM : array [1..(row+1)] of array [1..col] of string
    # ALGORITMA
    Id = str(input("Masukkan id game : "))
    Found = False
    for i in range (1,row):
        if Id==M[i][0]:
            Found = True
            break
    if Found:
        nama = str(input("Masukkan nama game : "))
        if nama!='':
            M[i][1] = nama
        kategori = str(input("Masukkan kategori game : "))
        if kategori!='':
            M[i][2] = kategori
        tahun_rilis = str(input("Masukkan tahun rilis game : "))
        if tahun_rilis!='':
            M[i][3] = tahun_rilis
        harga = str(input("Masukkan harga game : "))
        if harga!='':
            M[i][4] = harga
        fun.wait(1.5)
        fun.clearScreen()
        print("Berhasil mengubah game!")
        fun.writeCSV(cSv,M,col,row)
        

# Spesifikasi program : Mengubah data pada game (selain ID dan Stok)
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
ubahG("game.csv",GList,col,row)