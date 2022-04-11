# Program Riwayat
# Spesifikasi program : Program yang akan dijalankan jika pengguna memilih "riwayat" dan akan menampilkan riwayat

# KAMUS
# data_inv, hist : csv
# baris_data, kolom_data, baris_hist, kolom_hist : integer

# ALGORITMA
# import fungsi, prosedur, dan variabel buatan dari file lain
import function as func
import variables as var
import F10_SearchMyGame as inv

data_inv = 'C:/Users/Asus/OneDrive - Institut Teknologi Bandung/Documents/ITB/TPB ITB 2021/Daspro/tugas/tubes/Tubes IF1210 Daspro/CSV/kepemilikan.csv'
hist = 'C:/Users/Asus/OneDrive - Institut Teknologi Bandung/Documents/ITB/TPB ITB 2021/Daspro/tugas/tubes/Tubes IF1210 Daspro/CSV/riwayat.csv'
# deklarasi csv menjadi array
arr_data= var.pop_firstline(var.csvtoarray(data_inv))
baris_data= var.length(arr_data)
kolom_data = var.length(arr_data[0])

arr_hist= var.pop_firstline(var.csvtoarray(hist))
baris_hist= var.length(arr_hist)
kolom_hist = var.length(arr_hist[0])

def riwayat(username):
    # Spesifikasi program : menghasilkan riwayat pembelian game user

    # KAMUS LOKAL
    # hist_user : array of string
    # kolom_histUser, baris_histUser : integer

    # ALGORITMA
    func.clearScreen()
    func.wait(1)
    print("=========== Riwayat ===========")
    (hist_user, baris_histUser) = inv.my_game(username) # memanggil fungsi mygame untuk filter game sesuai user_id

    print()
    print("Daftar game:")
    if (baris_histUser==0): # jika tidak memeliki game
        print("Maaf, kamu tidak ada riwayat pembelian game. Ketik perintah 'beli_game' untuk membeli.")
    else:
        kolom_histUser = var.length(hist_user[0])
        for i in range (baris_histUser):
            print (str(i+1) + ".",end=" ")
            for j in range (kolom_histUser):
                if (j==kolom_histUser-1):
                    print(hist_user[i][j])
                elif (j!=3):
                    print(hist_user[i][j],end=" | ")
    print()
    func.goBackEnter()
