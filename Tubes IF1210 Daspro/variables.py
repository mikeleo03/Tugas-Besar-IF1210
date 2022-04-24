# Program Variables
# Spesifikasi program : intialisasi variabel-variabel yang akan digunakan di program lain
# Kumpulan variabel-variabel yang akan dipanggil hasil pengolahan csv

# KAMUS
# username, password : string
# data, users : csv

import B01_Cipher as B01

# SUBPROGRAM UTAMA - CSV PARSER
# 1. Membaca csv dan mengubahnya jadi string
def bacacsv(namafile):
    data = open(namafile)
    stringdata = data.read()
    data.close()
    # menambahkan "\n" jika belum
    if not(stringdata.endswith("\n")):
        stringdata += "\n"
    return stringdata

# 2. length untuk membaca panjang array (Fungsi tambahan Jason)
def length (arr):
    count = 0
    for i in arr:
        count = count + 1
    return count

# 3. Banyak kolom dalam csv
def banyakkolom(namafile):
    stringdata = bacacsv(namafile)
    # hitung jumlah baris dan kolom dengan for loop
    kolom = 1
    for i in stringdata:
        if i == ';':
            kolom += 1
        if i == '\n':
            break
    return kolom

# 4. Banyak baris pada csv
def banyakbaris(namafile):
    stringdata = bacacsv(namafile)
    baris = 0
    for i in stringdata:
        if i == '\n':
            baris += 1
    return baris

# 5. Ubah csv menjadi array yang bisa dimodifikasi
def csvtoarray(namafile):
    stringdata = bacacsv(namafile)
    barisdata = banyakbaris(namafile)
    kolomdata = banyakkolom(namafile)
    # Inisiasi array data
    arraydata = [['' for i in range (kolomdata)]for j in range (barisdata)]
    baris = 0
    kolom = 0

    #mengubah string ke array
    for i in stringdata:
        if i == ';':
            kolom += 1
        elif i == '\n':
            baris += 1
            kolom = 0
        else:
            arraydata[baris][kolom] += i
    return arraydata

# 6. pop baris pertama  (Fungsi tambahan Jason)
def pop_firstline(arr): 
    baris= length(arr)
    arr_baru = ['' for i in range (baris-1)]
    for i in range (baris-1):
        arr_baru[i] = arr[i+1]
    return arr_baru

# 7. filter array menjadi array_search  (Fungsi tambahan Jason)
def array_search (arr1, baris1, index, var1):
    # Spesifikasi program : memfilter array sesuai index dan variabel yang ditentukan

    # KAMUS LOKAL
    # arr_search : array of string

    # ALGORITMA
    # deklarasi array kosong
    arr_search = ["" for i in range (baris1)]
    baris2 = 0

    for i in range (baris1):
        if (arr1[i][index]== var1): # jika nilai dari array sesuai dengan variabel, menambahkan array tersebut ke array kosong
            arr_search[baris2]= arr1[i]
            baris2 +=1
    arr_filter =['' for i in range(baris2)] # deklarasi array lagi agar tidak ada array yg kosong
    for j in range (baris2):
        arr_filter[j]=arr_search[j] 
    return (arr_filter, baris2)

# 8. menghitung panjang isi kolom untuk merapikan hasil output  (Fungsi tambahan Jason)
def array_max_kolom(arr):
    # Spesifikasi program : menghitung panjang maksimal setiap kolom

    # KAMUS LOKAL
    # kolom_data, baris_data, panjang_max : integer
    # arr_kolom : array [1..kolom_data] of integer

    # ALGORITMA
    # deklarasi array kosong
    kolom_data = length(arr[0])
    baris_data = length(arr)
    arr_kolom = [0 for i in range (kolom_data)] # deklarasi array kosong

    # menghitung panjang maximal isi kolom dari setiap baris
    for j in range (kolom_data):
        panjang_max = length(arr[0][j])
        for i in range (1, baris_data):
            if (length(arr[i][j]) > panjang_max) :
                panjang_max = length(arr[i][j])
        arr_kolom[j] = panjang_max
    return arr_kolom 

# KUMPULAN SUBPROGRAM PENGOLAHAN DATA USER.CSV
# 1.
def role(username,password,arr_user):
    # Spesifikasi program : Menerima input username dan password serta mengeluarkan 
    # role yang dimiliki username
	# ALGORITMA
    baris = length(arr_user)
    for b in range(baris):
        if arr_user[b][1] == username and arr_user[b][3] == B01.cipher(password):
            return arr_user[b][4]

# 2.
def nama(username,arr_user):
    # Spesifikasi program : Menampilkan nama si pemilik username
	# ALGORITMA
    baris = length(arr_user)
    for b in range(baris):
        if arr_user[b][1] == username:
            return arr_user[b][2]

# 3.
def user_id(username,arr_user):
    # Spesifikasi program : Menampilkan id si pemilik username
	# ALGORITMA
    baris = length(arr_user)
    for b in range(baris):
        if arr_user[b][1] == username:
            return arr_user[b][0]

# 4.  (Fungsi tambahan Jason)
def usernamevalid(username,arr_user):  
    # Spesifikasi program : memvalidasi apakah username valid
    # ALGORITMA
    baris = length(arr_user)
    for b in range(baris):
        if arr_user[b][1] == username:
            return True
    return False
