# Program Riwayat
# Spesifikasi program : Program yang akan dijalankan jika pengguna memilih "riwayat" dan akan menampilkan riwayat

# KAMUS
# data_inv, hist : csv
# baris_data, kolom_data, baris_hist, kolom_hist : integer

# ALGORITMA
# import fungsi, prosedur, dan variabel buatan dari file lain
import function as func
import variables as var
import F10_SearchInventory as inv

data_inv = 'kepemilikan.csv'
hist = 'riwayat.csv'
# deklarasi csv menjadi array
arr_data= var.pop_firstline(var.csvtoarray(data_inv))
baris_data= var.length(arr_data)
kolom_data = var.length(arr_data[0])

arr_hist= var.pop_firstline(var.csvtoarray(hist))
baris_hist= var.length(arr_hist)
kolom_hist = var.length(arr_hist[0])

def my_history(username):
    # Spesifikasi program : menghasilkan array dari riwayat pembelian game user

    # KAMUS LOKAL
    # baris_inv, baris : integer
    # user_id : string
    # arr, arr_filter : array of string

    # ALGORITMA
    user_id = var.user_id(username)
    baris_data = var.length(arr_data) #baris dari array kepemilikan
    arr = ['' for i in range(baris_data)] # deklarasi array kosong
    baris=0
    for i in range (baris_data):
        if arr_data[i][1] == user_id:
            (arr,baris) = var.array_search(arr_hist,baris_hist,3, user_id) #memfilter array riwayat sesuai user_id
            
    arr_filter =['' for i in range(baris)] # deklarasi array lagi agar tidak ada array yg kosong
    for j in range (baris):
        arr_filter[j]=arr[j]
    return(arr_filter,baris)

def riwayat(username):
    # Spesifikasi program : menghasilkan riwayat pembelian game user

    # KAMUS LOKAL
    # hist_user : array of string
    # kolom_histUser, baris_histUser : integer

    # ALGORITMA
    func.clearScreen()
    func.wait(1)
    print("=========== Riwayat ===========")
    
    (hist_user, baris_histUser) = my_history(username) # memanggil fungsi mygame untuk filter game sesuai user_id

    print()
    print("Daftar game:")
    if (baris_histUser==0): # jika tidak memeliki game
        print("Maaf, kamu tidak ada riwayat pembelian game. Ketik perintah 'beli_game' untuk membeli.")
    else:
        kolom_histUser = var.length(hist_user[0])
        panjang_kolom = var.array_max_kolom(hist_user)

        for i in range (baris_histUser):
            print (str(i+1) + ".",end=" ")
            for j in range (kolom_histUser):
                max_length = panjang_kolom[j]
                length_kolom = var.length(hist_user[i][j])

                if (j==kolom_histUser-1):
                    print(hist_user[i][j])
                elif (j!=3):
                    print(hist_user[i][j]+ " "*(max_length-length_kolom),end=" | ")
    print()
    func.goBackEnter()