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

def showM(M,col,row):
    # Spesifikasi program : Menampilkan matriks pada usser
    # KAMUS LOKAL
    # M = array [1..row] of array [1..col] of string
    # x, y, l, k : integer
    # ALGORITMA
    # Definisi baris dan kolom (didefinisikan sebelumnya)
    for l in range(row):
        for k in range(col):
            print(M[l][k], end=" ")
        print("")

def count_row(rawData):
    # Spesifikasi program : Menghitung jumlah baris pada CSV
    # KAMUS LOKAL
    # rawData,cSv, File : csv
    # row : integer
    # i : char
    # ALGORITMA
    # Definisi baris dan kolom (didefinisikan sebelumnya)
    cSv = open(rawData,"r")
    File = cSv.readlines()
    row = 0
    cSv.close()
    for i in File:
        row+=1
    return row

def OpenCSV(cSv,col,row):
    # Spesifikasi program : Mengubah data pada CSV menjadi sebuah array
    # KAMUS LOKAL
    # cSv, File : csv
    # i, j, r1, r2, l: integer
    # k, e, s ,c: string
    # l : char
    # arrayCsV1, arrayCsV2, arrayCsV1 = array [1..row] of array [1..col] of string
    # ALGORITMA
    # Definisi baris dan kolom (didefinisikan sebelumnya)
    File = cSv.readlines()
    cSv.close()
    arrayCsV1 = [["" for i in range(col)]for j in range(row)]
    arrayCsV2= [["" for i in range(col)]for j in range(row)]
    arrayCsV3= [["" for i in range(col)]for j in range(row)]
    j = 0
    for k in File:
        l = 0
        e = ""
        arrayCsV1[j] = k
        r1 = lList(k)
        while l<r1:
            if j!=row-1:
                if k[l]!='\n':
                    e+=k[l]
            else: e+=k[l]
            l+=1
        arrayCsV2[j] = e
        j+=1
    j = 0
    for c in arrayCsV2:
        s = ""
        c += ","
        r2 = lList(c)
        i = 0
        for l in range(r2):
            if c[l]!=",":
                s += c[l]
            else: 
                arrayCsV3[j][i] = s  
                s = ""
                i+=1
        if i==col:
            j+=1
    return arrayCsV3
    
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