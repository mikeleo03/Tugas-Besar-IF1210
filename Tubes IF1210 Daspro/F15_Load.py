# Program Load
# Spesifikasi program : Program yang akan dijalankan pertama untuk memulai program dan loading data CSV ke array

# KAMUS
# args : argumen dalam pemanggilan file python
# cari_folder, load_data, load : function

# ALGORITMA

# import fungsi, prosedur, dan variabel buatan dari file lain
import variables as var
import argparse
import os
import F16_Save as F16

# menerima argumen dalam pemanggilan file python di terminal
parser = argparse.ArgumentParser()
parser.add_argument("nama_folder", help="loading semua file csv yang digunakan dalam program ini")
args = parser.parse_args()

def cari_folder(nama_folder):
    # Spesifikasi program : Mencari lokasi folder

	# KAMUS LOKAL
	# cond : boolean
    # path, directories, files : string
    # dir, lokasi : string
    # nama_folder : string

	# ALGORITMA
    cond = False
    for (path, directories, files) in os.walk(os.getcwd()): # melakukan pengulangan untuk mendapatkan lokasi folder
        for dir in directories:
            if dir == nama_folder:
                cond = True
                lokasi = os.path.join(path, dir)
    
    if cond == False:
        lokasi = ""
    
    return lokasi

def load():
    # Spesifikasi program : Menuliskan ke layar proses loading

	# KAMUS LOKAL
	# 

	# ALGORITMA
    if cari_folder(args.nama_folder) == "":
        print('Folder "' + str(args.nama_folder) + '" tidak ditemukan.')
    else:
        print("Loading…")
        print("Selamat datang di antarmuka “Binomo”")
        load_data()

def load_data():
    # Spesifikasi program : Menyimpan data csv sebagai array

	# KAMUS LOKAL
	# path2, directories2, files2 : string
    # file : string
    # arr_game, arr_kepemilikan, arr_riwayat, arr_user : array of array of string
    # baris_game, baris_kepemilikan, baris_riwayat, baris_user : integer
    # kolom_game, kolom_kepemilikan, kolom_riwayat, kolom_user : integer

	# ALGORITMA
    
    for (path2, directories2, files2) in os.walk(cari_folder(args.nama_folder)):
        for file in files2:
            if file == "game.csv": # menyimpan file csv game ke dalam array game
                arr_game= var.pop_firstline(var.csvtoarray(os.path.join(path2, file)))
                baris_game= var.length(arr_game) 
                kolom_game = var.length(arr_game[0])
            if file == "kepemilikan.csv": # menyimpan file csv kepemilikan ke dalam array kepemilikan
                arr_kepemilikan= var.pop_firstline(var.csvtoarray(os.path.join(path2, file)))
                baris_kepemilikan= var.length(arr_kepemilikan) 
                kolom_kepemilikan = var.length(arr_kepemilikan[0])
            if file == "riwayat.csv": # menyimpan file csv riwayat ke dalam array riwayat
                arr_riwayat= var.pop_firstline(var.csvtoarray(os.path.join(path2, file)))
                baris_riwayat= var.length(arr_riwayat) 
                kolom_riwayat= var.length(arr_riwayat[0])
            if file == "user.csv": # menyimpan file csv user ke dalam array user
                arr_user= var.pop_firstline(var.csvtoarray(os.path.join(path2, file)))
                baris_user= var.length(arr_user) 
                kolom_user = var.length(arr_user[0])
        
    return arr_game, arr_kepemilikan, arr_riwayat, arr_user
