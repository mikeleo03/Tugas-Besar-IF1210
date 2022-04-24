# Program Riwayat
# Spesifikasi program : Program yang akan dijalankan jika pengguna memilih "riwayat" dan akan menampilkan riwayat

# KAMUS
# arr_kepemilikan : array of kepemilikan
# arr_riwayat : array of riwayat
# arr_user : array of user
# username: string

# ALGORITMA
# import fungsi, prosedur, dan variabel buatan dari file lain
import function as func
import variables as var

def my_history(username, arr_kepemilikan, arr_riwayat, arr_user):
    # Spesifikasi program : menghasilkan array dari riwayat pembelian game user

    # KAMUS LOKAL
    # baris_data, baris_hist, baris : integer
    # user_id : string
    # arr, arr_filter : array of string
    # i,j : integer
    
    # ALGORITMA
    user_id = var.user_id(username, arr_user)
    
    baris_data = var.length(arr_kepemilikan) # baris dari array kepemilikan
    baris_hist = var.length(arr_riwayat) # baris dari array riwayat
    
    arr = ['' for i in range(baris_data)] # deklarasi array kosong
    baris=0
    for i in range (baris_data):
        if arr_kepemilikan[i][1] == user_id:
            (arr,baris) = var.array_search(arr_riwayat,baris_hist,3, user_id) #memfilter array riwayat sesuai user_id
            
    arr_filter =['' for i in range(baris)] # deklarasi array lagi agar tidak ada array yg kosong
    for j in range (baris):
        arr_filter[j]=arr[j]
    return(arr_filter,baris)

def riwayat(username,arr_kepemilikan, arr_riwayat, arr_user):
    # Spesifikasi program : menghasilkan riwayat pembelian game user

    # KAMUS LOKAL
    # hist_user : array of string
    # kolom_histUser, baris_histUser : integer

    # ALGORITMA
    func.clearScreen()
    func.wait(1)
    print("=========== Riwayat ===========")
    
    (hist_user, baris_histUser) = my_history(username,arr_kepemilikan, arr_riwayat, arr_user) # memanggil fungsi mygame untuk filter game sesuai user_id

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
