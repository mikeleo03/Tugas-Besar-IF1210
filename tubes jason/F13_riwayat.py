import variables as var
import F10_SearchInventory as inv

data_inv = 'C:/Users/Asus/OneDrive - Institut Teknologi Bandung/Documents/ITB/TPB ITB 2021/Daspro/tugas/tubes/Tubes IF1210 Daspro/CSV/kepemilikan.csv'
hist = 'C:/Users/Asus/OneDrive - Institut Teknologi Bandung/Documents/ITB/TPB ITB 2021/Daspro/tugas/tubes/Tubes IF1210 Daspro/CSV/riwayat.csv'

arr_data= var.pop_firstline(var.csvtoarray(data_inv))
baris_data= var.length(arr_data)
kolom_data = var.length(arr_data[0])

arr_hist= var.pop_firstline(var.csvtoarray(hist))
baris_hist= var.length(arr_hist)
kolom_hist = var.length(arr_hist[0])

def riwayat(user_id):
    (hist_user, baris_histUser) = inv.my_game(user_id)

    print()
    print("Daftar game:")
    if (baris_histUser==0):
        print("Maaf, kamu tidak ada riwayat pembelian game. Ketik perintah 'beli_game' untuk membeli.")
    else:
        kolom = var.length(hist_user[0])
        for i in range (baris_histUser):
            print (str(i+1) + ".",end=" ")
            for j in range (kolom):
                if (j==kolom-1):
                    print(hist_user[i][j])
                elif (j!=3):
                    print(hist_user[i][j],end=" | ")

riwayat('3')
