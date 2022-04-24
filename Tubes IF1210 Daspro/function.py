# Program function
# Spesifikasi program : Kumpulan fungsi dan prosedur yang akan dipanggil pada program lain 

# ALGORITMA
# import module os, sys, dan time
import os
import sys
import time

import F02_Register as F02
import F04_tambah_game as F04
import F05_ubah_game as F05
import F06_ubah_stok as F06
import F07_list_game_toko as F07
import F08_BuyGame as F08
import F09_ListGame as F09
import F10_SearchInventory as F10
import F11_SearchGameAtStore as F11
import F12_TopUp as F12
import F13_Riwayat as F13
import F14_Help as F14
import F16_Save as F16
import F17_Exit as F17

import B02_MagicShell as B02
import B03_TicTacToe as B03

def goBackEnter():
	# Spesifikasi program : Membuat user kembali ke tampilan sebelumnya
	# KAMUS LOKAL
	# x : dictionary
	# ALGORITMA
    x = input("Tekan enter untuk kembali")
    return 0

def wait(i):
	# Spesifikasi program : Menahan waktu dengan jumlah detik sesuai dengan argumen
	# KAMUS LOKAL
	# i : float
	# ALGORITMA  
	time.sleep(i)

def clearScreen():
	# Spesifikasi program : Menghapus semua output yang sudah di-print
	# ALGORITMA  
	os.system('cls') #change to 'clear' when using macOS or linux

def clearLast():
	# Spesifikasi program : Menghapus output yang di-print terakhir
	# ALGORITMA  
	sys.stdout.write('\x1b[1A')
	sys.stdout.write('\x1b[2K')

def funcuser(username,iduser,arr_game,arr_kepemilikan,arr_riwayat,arr_user):
    # Spesifikasi program : Memunculkan fitur yang dapat diakses user
	# KAMUS LOKAL
	# pilihLogin : int
	# ALGORITMA
    wait(1.5)
    clearScreen()
    # Mengimport fungsi pilih menu yang bisa dilakukan admin dan validasinya
    benar = True
    while benar:
        print('''-------------------------------
            BINOMO
-------------------------------''')
        print('Selamat datang,',username,'!')
        print("\nsilakan ketik 'help' jika membutuhkan bantuan")
        print("\nMeminta perintah berikutnya")
        ketik = input(">>")
        if (ketik == "list_game_toko"):
            wait(1.5)
            F07.ListGame(arr_game)
        elif (ketik == "buy_game"):
            wait(1.5)
            F08.buygame(iduser,arr_game,arr_kepemilikan,arr_riwayat,arr_user)
        elif (ketik == "list_game"):
            wait(1.5)
            F09.game_list(iduser,arr_kepemilikan,arr_game)
        elif (ketik == "search_my_game"):
            wait(1.5)
            F10.search_my_game(username, arr_game, arr_kepemilikan, arr_user)
        elif (ketik == "search_game_at_store"):
            wait(1.5)
            F11.search_game_at_store (arr_game)
        elif (ketik == "riwayat"):
            wait(1.5)
            F13.riwayat(username,arr_kepemilikan, arr_riwayat, arr_user)
        elif (ketik == "help"):
            wait(1.5)
            F14.helpuser()
        elif (ketik == "save"):
            wait(1.5)
            F16.save(arr_game,arr_kepemilikan,arr_riwayat,arr_user)
        elif (ketik == "logout"):
            wait(1.5)
            pilihan = input("Apakah Anda ingin logout dan kembali ke laman utama? (y/n) ") # menerima input pilihan
            while pilihan not in ["y", "n", "Y", "N"]: # pilihan tidak valid
                pilihan = input("Apakah Anda ingin logout dan kembali ke laman utama? (y/n) ")

            if pilihan == "y" or pilihan == "Y": # Kembali ke laman utama
                benar = False
                break
            else:
                clearScreen()
        # MINIGAME
        elif (ketik == "magic_shell"):
            wait(1.5)
            B02.kerangajaib()
        elif (ketik == "tictactoe"):
            wait(1.5)
            B03.tictactoe()
        else:
            print("\nperintah tidak valid, silahkan input ulang")
            wait(1.5)
            clearScreen()
            benar = True

def funcadmin(username,iduser,arr_game,arr_kepemilikan,arr_riwayat,arr_user):
    # Spesifikasi program : Memunculkan fitur yang dapat diakses admin
	# KAMUS LOKAL
	# pilihLogin : int
	# ALGORITMA
    wait(1.5)
    clearScreen()
    # Mengimport fungsi pilih menu yang bisa dilakukan admin dan validasinya
    benar = True
    while benar:
        print('''-------------------------------
            BINOMO
-------------------------------''')
        print('Selamat datang,',username,'!')
        print("\nsilakan ketik 'help' jika membutuhkan bantuan")
        print("\nMeminta perintah berikutnya")
        ketik = input(">>")
        if (ketik == "register"):
            wait(1.5)
            F02.registAdmin(arr_user)
        elif (ketik == "tambah_game"):
            wait(1.5)
            arr_game = F04.TambahGame(arr_game)
        elif (ketik == "ubah_game"):
            wait(1.5)
            F05.UbahGame(arr_game)
        elif (ketik == "ubah_stok"):
            wait(1.5)
            F06.UbahStok(arr_game)
        elif (ketik == "list_game_toko"):
            wait(1.5)
            F07.ListGame(arr_game)
        elif (ketik == "search_game_at_store"):
            wait(1.5)
            F11.search_game_at_store (arr_game)
        elif (ketik == "topup"):
            wait(1.5)
            F12.topup(arr_user)
        elif (ketik == "help"):
            wait(1.5)
            F14.helpadmin()
        elif (ketik == "save"):
            wait(1.5)
            F16.save(arr_game,arr_kepemilikan,arr_riwayat,arr_user)
        elif (ketik == "logout"):
            wait(1.5)
            pilihan = input("Apakah Anda ingin logout dan kembali ke laman utama? (y/n) ") # menerima input pilihan
            while pilihan not in ["y", "n", "Y", "N"]: # pilihan tidak valid
                pilihan = input("Apakah Anda ingin logout dan kembali ke laman utama? (y/n) ")

            if pilihan == "y" or pilihan == "Y": # Kembali ke laman utama
                benar = False
                break
            else:
                clearScreen()
        # MINIGAME
        elif (ketik == "magic_shell"):
            wait(1.5)
            B02.kerangajaib()
        elif (ketik == "tictactoe"):
            wait(1.5)
            B03.tictactoe()
        else:
            print("\nperintah tidak valid, silahkan input ulang")
            wait(1.5)
            clearScreen()
            benar = True

# Fungsi Tambahan Julian :

def lList(L):
    # Spesifikasi program : Menghitung panjang suatu list
    # KAMUS LOKAL
    # L = array [1..row] of array [1..col] of string
    # count, i : integer
    # ALGORITMA
    count = 0
    for i in L:
        count+=1
    return count

def writeCSV(cSv,M,col,row):
    # Spesifikasi program : Mengubah data pada Matriks menjadi sebuah CSV
    # KAMUS LOKAL
    # f,cSv : csv
    # row, i: integer
    # e,Konversi: string
    # M = array [1..row] of array [1..col] of string
    # ALGORITMA
    # Definisi baris dan kolom (didefinisikan sebelumnya)
    TabS = [" " for j in range(row)]
    Konversi = " "
    for j in range(row):
        e = ""
        for i in range(col):
            if i!=col-1:
                e+=M[j][i]+","
            else:
                e+=M[j][i]
                TabS[j]=e 
    for j in range(row):
        if j!=row-1: Konversi+=TabS[j] + '\n'
        else: Konversi+=TabS[j]
    f = open(cSv,"w")
    f.write(Konversi)
    f.close
