# Program function
# Spesifikasi program : Kumpulan fungsi dan prosedur yang akan dipanggil pada program lain 

# ALGORITMA
# import module os, sys, dan time
import os
import sys
import time

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

def pilihMenuAdmin():
	# Spesifikasi program : Memilih menu yang akan digunakan Admin
	# KAMUS LOKAL
	# pilih : int
	# ALGORITMA
	print('''-------------------------------
            BINOMO
-------------------------------''')
	print('''
Pilih menu:
1. register
2. tambah_game
3. ubah_game
4. ubah_stok
5. list_game_toko
6. search_game_at_store
7. topup
8. help
9. save
0. exit
		''')
	pilih = input("Pilih nomor menu: ")
	if(not(pilih.isnumeric()) or int(pilih) < 0 or int(pilih) > 9):
		clearScreen()
		print("Menu tidak terdaftar! Silahkan coba lagi")
		clearScreen()
		pilih = pilihMenuAdmin()
	return(int(pilih))

def pilihMenuUser():
	# Spesifikasi program : Memilih menu yang akan digunakan User
	# KAMUS LOKAL
	# pilih : int
	# ALGORITMA 
	print('''-------------------------------
            BINOMO
-------------------------------''')
	print('''
Pilih menu:
1. list_game_toko
2. buy_game
3. list_game
4. search_my_game
5. search_game_at_store
6. riwayat
7. help
8. save
0. exit
		''')
	pilih = input("Pilih nomor menu: ")
	if(not(pilih.isnumeric()) or int(pilih) < 0 or int(pilih) > 8):
		clearScreen()
		print("Menu tidak terdaftar! Silahkan coba lagi")
		pilih = pilihMenuUser()
	return(int(pilih))