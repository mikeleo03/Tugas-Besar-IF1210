import variables as var
import argparse
import os
import F16_Save as F16


parser = argparse.ArgumentParser()
parser.add_argument("nama_folder", help="loading semua file csv yang digunakan dalam program ini")
args = parser.parse_args()

def cari_folder(nama_folder):
    cond = False
    for (path, directories, files) in os.walk(os.getcwd()):
        for dir in directories:
            if dir == nama_folder:
                cond = True
                lokasi = os.path.join(path, dir)
    
    if cond == False:
        lokasi = ""
    
    return lokasi
        #print('Folder "' + str(args.nama_folder) + '" tidak ditemukan.')

def load():
    if cari_folder(args.nama_folder) == "":
        print('Folder "' + str(args.nama_folder) + '" tidak ditemukan.')
    else:
        print("Loading…")
        print("Selamat datang di antarmuka “Binomo”")
        load_data()

def load_data():
    
    for (path2, directories2, files2) in os.walk(cari_folder(args.nama_folder)):
        for file in files2:
            if file == "game.csv":
                arr_game= var.pop_firstline(var.csvtoarray(os.path.join(path2, file)))
                baris_game= var.length(arr_game) 
                kolom_game = var.length(arr_game[0])
            if file == "kepemilikan.csv":
                arr_kepemilikan= var.pop_firstline(var.csvtoarray(os.path.join(path2, file)))
                baris_kepemilikan= var.length(arr_kepemilikan) 
                kolom_kepemilikan = var.length(arr_kepemilikan[0])
            if file == "riwayat.csv":
                arr_riwayat= var.pop_firstline(var.csvtoarray(os.path.join(path2, file)))
                baris_riwayat= var.length(arr_riwayat) 
                kolom_riwayat= var.length(arr_riwayat[0])
            if file == "user.csv":
                arr_user= var.pop_firstline(var.csvtoarray(os.path.join(path2, file)))
                baris_user= var.length(arr_user) 
                kolom_user = var.length(arr_user[0])
        
    return arr_game, arr_kepemilikan, arr_riwayat, arr_user
