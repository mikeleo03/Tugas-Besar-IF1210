import function as func
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

def TambahGame(M):
    # Spesifikasi program : Menginput data game baru ke matriks
    # KAMUS
    # M : array [1..row] of array [1..col] of string
    # Id, nama, kategori, tahun_rilis, harga. stok : string
    # newGame : array [1..row] of array [1..6] of string
    # newM : array [1..(row+1)] of array [1..col] of string
    # ALGORITMA
    col = 6
    row = func.count_row('game.csv')                    
    nama = str(input("Masukkan nama game : "))
    kategori = str(input("Masukkan kategori game : "))
    tahun_rilis = str(input("Masukkan tahun rilis game : "))
    harga = str(input("Masukkan harga game : "))
    stok = str(input("Masukkan stok awal : "))
    while nama=='' or kategori=='' or tahun_rilis=='' or harga=='' or stok=='':
        print("Mohon agar memasukkan semua informasi mengenai game agar dapat disimpan di BNMO")
        nama = str(input("Masukkan nama game : "))
        kategori = str(input("Masukkan kategori game : "))
        tahun_rilis = str(input("Masukkan tahun rilis game : "))
        harga = str(input("Masukkan harga game : "))
        stok = str(input("Masukkan stok awal : "))
    row+=1
    Id = makeId(row)
    newGame = [[Id,nama,kategori,tahun_rilis,harga,stok]]
    newM = M+newGame
    print("Penambahan game sukses")
    func.wait(1.5)
    func.clearScreen()
    func.writeCSV("game.csv",newM,col,row)
    return newM

