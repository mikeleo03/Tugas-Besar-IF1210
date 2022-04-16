import function as fun
def makeId(row):
    # Spesifikasi program : Membuat id game secara otomatis ketika ingin menambahkan game baru
    # KAMUS
    # id : string
    # row : integer
    # ALGORITMA
    id = ""
    row-=1
    if row<10:
        id = "GAME00"+str(row)
    elif 10<=row<100:
        id = "GAME0"+str(row)
    else:                           #{row>100}
        id = "GAME"+str(row)
    return id

def addG(M,row):
    # Spesifikasi program : Menginput data game baru ke matriks
    # KAMUS
    # M : array [1..row] of array [1..col] of string
    # Id, nama, kategori, tahun_rilis, harga. stok : string
    # newGame : array [1..row] of array [1..6] of string
    # newM : array [1..(row+1)] of array [1..col] of string
    # ALGORITMA
    nama = str(input("Masukkan nama game : "))
    kategori = str(input("Masukkan kategori game : "))
    tahun_rilis = str(input("Masukkan tahun rilis game : "))
    harga = str(input("Masukkan harga game : "))
    stok = str(input("Masukkan jumlah stok game : "))
    while nama=='' or kategori=='' or tahun_rilis=='' or harga=='' or stok=='':
        print("Mohon agar memasukkan semua informasi mengenai game agar dapat disimpan di BNMO")
        nama = str(input("Masukkan nama game : "))
        kategori = str(input("Masukkan kategori game : "))
        tahun_rilis = str(input("Masukkan tahun rilis game : "))
        harga = str(input("Masukkan harga game : "))
        stok = str(input("Masukkan jumlah stok game : "))
    Id = makeId(row)
    newGame = [[Id,nama,kategori,tahun_rilis,harga,stok]]
    newM = M+newGame
    print("Penambahan game sukses")
    return newM

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
row+=1
NList = addG(GList,row)
fun.wait(1.5)
fun.clearScreen()
fun.writeCSV("game.csv",NList,col,row)