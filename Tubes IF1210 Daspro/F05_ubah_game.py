import function as func
import variables as var
def UbahGame(M):
    # Spesifikasi program : Menginput perubahan data game yang baru ke dalam matriks (selain id dan stok pada game)
    # KAMUS
    # M : array [1..row] of array [1..col] of string
    # i : integer
    # Found : boolean
    # Id, nama, kategori, tahun_rilis, harga : string
    # ALGORITMA
    row = var.length(M)
    Id = str(input("Masukkan id game : "))
    Found = False
    i = 0
    while i<row and Found==False:
        if Id==M[i][0]:
            Found = True
        else : i+=1
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
        func.wait(1.5)
        func.clearScreen()
        print("Berhasil mengubah game!")
        return M
