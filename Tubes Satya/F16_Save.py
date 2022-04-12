import os
import F15_Load as F15
import variables as var


def arrtocsv(array, nama_folder):
    f = open(nama_folder, "w")
    if nama_folder[-8:] == "user.csv":
        f.write("id;username;nama;password;role;saldo\n")
        for i in range(var.length(array)):
            for j in range(6):
                if j != 5:
                    f.write(array[i][j] + ";")
                else:
                    f.write(array[i][j] + "\n")

    elif nama_folder[-8:] == "game.csv":
        f.write("id;nama;kategori;tahun_rilis;harga;stok\n")
        for i in range(var.length(array)):
            for j in range(6):
                if j != 5:
                    f.write(array[i][j] + ";")
                else:
                    f.write(array[i][j] + "\n")
        
    elif nama_folder[-11:] == "riwayat.csv":
        f.write("game_id;nama;harga;user_id;tahun_beli\n")
        for i in range(var.length(array)):
            for j in range(5):
                if j != 4:
                    f.write(array[i][j] + ";")
                else:
                    f.write(array[i][j] + "\n")
        
    elif nama_folder[-15:] == "kepemilikan.csv":
        f.write("game_id;user_id\n")
        for i in range(var.length(array)):
            for j in range(2):
                if j != 1:
                    f.write(array[i][j] + ";")
                else:
                    f.write(array[i][j] + "\n")
    f.close()

def save(arr_game, arr_kepemilikan, arr_riwayat, arr_user):
    nama_folder = input("Masukkan nama folder penyimpanan: ")
    lokasi = F15.cari_folder(nama_folder)
    if lokasi == "":
        os.mkdir(os.path.join(os.getcwd(), nama_folder))
        lokasi = os.path.join(os.getcwd(), nama_folder)

    
    arrtocsv(arr_game, lokasi + str(chr(92)) + "game.csv")
    arrtocsv(arr_kepemilikan, lokasi + str(chr(92)) + "kepemilikan.csv")
    arrtocsv(arr_riwayat, lokasi + str(chr(92)) + "riwayat.csv")
    arrtocsv(arr_user, lokasi + str(chr(92)) + "user.csv")
    
#arrtocsv