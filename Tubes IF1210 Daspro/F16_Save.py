# Program Save
# Spesifikasi program : Program yang akan dijalankan jika pengguna ingin menyimpan data yang telah berubah

# KAMUS
# arrtocsv, save : procedure

# ALGORITMA

# import fungsi, prosedur, dan variabel buatan dari file lain
import os
import F15_Load as F15
import variables as var

def arrtocsv(array, nama_folder):
    # Spesifikasi program : Mengubah array menjadi file csv yang tersimpan dalam suatu folder

	# KAMUS LOKAL
	# f : fungsi untuk memodifikasi suatu file
    # array : array of array of string
    # nama_folder : string
    # i, j : integer

	# ALGORITMA
    f = open(nama_folder, "w")
    if nama_folder[-8:] == "user.csv": # Mengubah array user menjadi file csv user
        f.write("id;username;nama;password;role;saldo\n")
        for i in range(var.length(array)):
            for j in range(6):
                if j != 5:
                    f.write(array[i][j] + ";")
                else:
                    f.write(array[i][j] + "\n")

    elif nama_folder[-8:] == "game.csv": # Mengubah array game menjadi file csv game
        f.write("id;nama;kategori;tahun_rilis;harga;stok\n")
        for i in range(var.length(array)):
            for j in range(6):
                if j != 5:
                    f.write(array[i][j] + ";")
                else:
                    f.write(array[i][j] + "\n")
        
    elif nama_folder[-11:] == "riwayat.csv": # Mengubah array riwayat menjadi file csv riwayat
        f.write("game_id;nama;harga;user_id;tahun_beli\n")
        for i in range(var.length(array)):
            for j in range(5):
                if j != 4:
                    f.write(array[i][j] + ";")
                else:
                    f.write(array[i][j] + "\n")
        
    elif nama_folder[-15:] == "kepemilikan.csv": # Mengubah array kepemilikan menjadi file csv kepemilikan
        f.write("game_id;user_id\n")
        for i in range(var.length(array)):
            for j in range(2):
                if j != 1:
                    f.write(array[i][j] + ";")
                else:
                    f.write(array[i][j] + "\n")
    f.close()

def save(arr_game, arr_kepemilikan, arr_riwayat, arr_user):
    # Spesifikasi program : Menyimpan file csv ke dalam suatu folder

	# KAMUS LOKAL
	# arr_game, arr_kepemilikan, arr_riwayat, arr_user : array of array of string
    # nama_folder, lokasi : string
    # arrtocsv : procedure

	# ALGORITMA
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