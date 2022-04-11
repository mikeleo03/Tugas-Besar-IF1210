import variables as var
import function as func
import argparse
import os
import F03_Login as F03

parser = argparse.ArgumentParser()
parser.add_argument("nama_folder", help="loading semua file csv yang digunakan dalam program ini")
args = parser.parse_args()

cond = False
for (path, directories, files) in os.walk(os.getcwd()):
    for dir in directories:
        if dir == args.nama_folder:
            cond = True
            print("Loading…")
            func.wait(1.5)
            print("# Panggil prosedur load data")
            print("Selamat datang di antarmuka “Binomo”")
            for (path2, directories2, files2) in os.walk(os.path.join(path, dir)):
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
            benar = True
            while benar:
                print("Meminta perintah berikutnya")
                ketik = input()
                if (ketik == "login"):
                    print("# Masuk ke laman Login")
                    func.wait(3)
                    F03.login()
                else:
                    print("\nperintah tidak valid, silahkan input ulang")
                    benar = True
                    
if cond == False:
    print('Folder "' + str(args.nama_folder) + '" tidak ditemukan.')