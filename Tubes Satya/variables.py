# Program Variables
# Spesifikasi program : intialisasi variabel-variabel yang akan digunakan di program lain
# Kumpulan variabel-variabel yang akan dipanggil hasil pengolahan csv

# KAMUS
# username, password : string
# data, users : csv

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

# 2. Banyak character dalam csv
def banyakchar(namafile):
    stringdata = bacacsv(namafile)
    # banyak char pada data
    chara = 0
    for row in stringdata:
        chara += 1
    return chara

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
    # Inisiasi array data
    arraydata = [['']]
    baris = 0
    kolom = 0

    #mengubah string ke array
    for i in stringdata:
        if i == ';':
            arraydata[baris] += ['']
            kolom += 1
        elif i == '\n':
            arraydata += [['']]
            baris += 1
            kolom = 0
        else:
            arraydata[baris][kolom] += i
    # mengisi arrAkhir dengan data dari csv
    arrAkhir = [['' for i in range(kolom)] for j in range(baris)]
    for i in range(baris):
        arrAkhir[i] = arraydata[i]
    return arrAkhir

# 6. Fungsi len 
def length (arr):
    count = 0
    for i in arr:
        count = count + 1
    return count

# 7. Pop baris pertama
def pop_firstline(arr):
    baris= length(arr)
    arr_baru = [[] for i in range (baris-1)]
    for i in range (baris-1):
        arr_baru[i] += arr[i+1]
    return arr_baru

# 8. Remove
def popArr(arr, a):
    arr_baru=[]
    for i in range (length(arr)):
        if i!=a:
            arr_baru += [arr[i]]
    return arr_baru

def banyak_kolom_array(arr):
    count = 0
    for i in arr[0]:
        count = count + 1
    return count

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

