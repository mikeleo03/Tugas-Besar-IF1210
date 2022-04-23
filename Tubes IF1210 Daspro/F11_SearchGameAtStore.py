# Program SearchGameAtStore
# Spesifikasi program : Program yang akan dijalankan jika pengguna memilih "search_game_at_store" dan akan mencari game di toko

# KAMUS
# game : csv
# arr_game : array of game
# baris_game, kolom_game : integer

# ALGORITMA
# import fungsi, prosedur, dan variabel buatan dari file lain
import function as func
import variables as var

def search_game_at_store (arr_game):
    # Spesifikasi program : menghasilkan array dari filter game di toko

    # KAMUS LOKAL
    # baris_game, parameter, baris_search, kolom_search : integer
    # id, nama, harga, kategori, tahun : string (string karena menyesuaikan dengan tipe data array)
    # arr_search : array of string

    # ALGORITMA
    func.clearScreen()
    func.wait(1)
    print("=========== Search Game At Store ===========")
    id = str(input("Masukkan ID Game: "))
    nama = str(input("Masukkan Nama Game: "))
    harga = str(input("Masukkan Harga Game: "))
    kategori = str(input("Masukkan Kategori Game: "))
    tahun = str(input("Masukkan Tahun Rilis Game: "))

    # deklarasi
    baris_game = var.length(arr_game) # banyak baris dari array game sebelum di filter dan dikurangi 1 karena baris pertamanya hanya berupa kategori
    baris_search = 0 # banyak baris dari filter
    parameter = 0 # jumlah parameter input dari user

    # filter sesuai input user
    if (id==""): # jika kosong maka array filter sama dengan array game
        arr_search = (arr_game) # menghapus baris pertama array game karena hanya berisi tulisan kategori
        baris_search = baris_game
    elif not(id==""):
        (arr_search,baris_search) = var.array_search(arr_game, baris_game,0,id)
        parameter+=1

    if not(nama==""):
        # menyimpan array filter dan barisnya di arr_search1 dan baris_search1 karena var arr_search digunakan dalam fungsi berikutnya
        (arr_search1,baris_search1) = var.array_search(arr_search, baris_search,1,nama)
        arr_search = arr_search1
        baris_search = baris_search1
        parameter+=1

    if not(kategori==""):
        arr_search1,baris_search1= var.array_search(arr_search, baris_search,2,kategori)
        arr_search = arr_search1
        baris_search = baris_search1
        parameter+=1

    if not(tahun==""):
        arr_search1,baris_search1 = var.array_search(arr_search, baris_search,3,tahun)
        arr_search = arr_search1
        baris_search = baris_search1
        parameter+=1
    
    if not(harga==""):
        arr_search1,baris_search1 = var.array_search(arr_search, baris_search,4,harga)
        arr_search = arr_search1
        baris_search = baris_search1
        parameter+=1
    
    print()
    print("Daftar Game pada toko yang memenuhi kriteria: ")
    if (parameter>0) and (baris_search==0): # user memasukkan lebih dari 1 parameter dan tidak ada sesuai
        print("Tidak ada game pada toko yang memenuhi kriteria")
    else: 
        kolom_search = var.length(arr_search[0]) # menghitung panjang kolom dari array filter
        panjang_kolom = var.array_max_kolom(arr_search)

        # menampilkan hasil array filter dan merapikan
        for i in range (baris_search):
            print (str(i+1) + ".",end=" ")
            for j in range (kolom_search):
                max_length = panjang_kolom[j]
                length_kolom = var.length(arr_search[i][j])
                if (j==kolom_search-1):
                    print(arr_search[i][j])
                else:
                    print(str(arr_search[i][j]) + " "*(max_length-length_kolom) ,end=" | ")
    print()
    func.goBackEnter()
