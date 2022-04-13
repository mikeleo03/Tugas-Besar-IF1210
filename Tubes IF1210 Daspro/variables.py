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
    return (arr_search, baris2)

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
# 1. Inisialisasi
arraydatauser = csvtoarray('user.csv')
barisuser = banyakbaris('user.csv')
kolomuser = banyakkolom('user.csv')

# 2.
def loginvalid(username,password):
    # Spesifikasi program : Memvalidasi apakah input username dan password sudah valid
	# ALGORITMA
    for b in range(barisuser):
        if arraydatauser[b][1] == username and arraydatauser[b][3] == password:
            return True

# 3.
def role(username,password):
    # Spesifikasi program : Menerima input username dan password serta mengeluarkan 
    # role yang dimiliki username
	# ALGORITMA
    for b in range(barisuser):
        if arraydatauser[b][1] == username and arraydatauser[b][3] == password:
            return arraydatauser[b][4]

# 4.
def nama(username):
    # Spesifikasi program : Menampilkan nama si pemilik username
	# ALGORITMA
    for b in range(barisuser):
        if arraydatauser[b][1] == username:
            return arraydatauser[b][2]

# 5.
def registervalid(username):
    # Spesifikasi program : Memvalidasi apakah input username tidak pernah digunakan
	# ALGORITMA
    for b in range(barisuser):
        if arraydatauser[b][1] == username:
            return False

# 6.
def nextnumber():
    # Spesifikasi program : menentukan penomoran untuk data berikutnya
	# ALGORITMA
    for b in range(barisuser-1,1,-1): # reverse loop
        return int(arraydatauser[b][0]) + 1

# 7.
def adduser(username_baru,nama,pswd_baru):
    # Spesifikasi program : Menambahkan data member baru pada list
    # ALGORITMA
    # Deklarasi array baru user
    baru = ['' for i in range(6)]
    # mengisi array baru dengan data user baru
    baru[0] = nextnumber()
    baru[1] = username_baru
    baru[2] = nama
    baru[3] = pswd_baru
    baru[4] = "user"
    baru[5] = 0

    # menambah array baru ke database
    arraydatauser[nextnumber()-1] += [baru]

# 8.
def user_id(username):
    # Spesifikasi program : Menampilkan id si pemilik username
	# ALGORITMA
    for b in range(barisuser):
        if arraydatauser[b][1] == username:
            return arraydatauser[b][0]

# 9.  (Fungsi tambahan Jason)
def usernamevalid(username):  
    # Spesifikasi program : memvalidasi apakah username valid
    # ALGORITMA
    for b in range(barisuser):
        if arraydatauser[b][1] == username:
            return True
    return False

# KUMPULAN SUBPROGRAM PENGOLAHAN DATA KEPEMILIKAN.CSV
# 1. Inisialisasi
arraydatakepemilikan = csvtoarray('kepemilikan.csv')
bariskepemilikan = banyakbaris('kepemilikan.csv')
kolomkepemilikan = banyakkolom('kepemilikan.csv')

# 2.
def addkepemilikan(gameid_baru,userid_baru):
    # Spesifikasi program : Menambahkan data game baru pada list kepemilikan
    # ALGORITMA
    # Deklarasi array baru user
    gamebaru = ['' for i in range(2)]
    # mengisi array baru dengan data user baru
    gamebaru[0] = gameid_baru
    gamebaru[1] = int(userid_baru)

    # menambah array baru ke database
    arraydatakepemilikan[nextnumber()-1] += [gamebaru]

# KUMPULAN SUBPROGRAM PENGOLAHAN DATA RIWAYAT.CSV
# 1. Inisialisasi
arraydatariwayat = csvtoarray('riwayat.csv')
barisriwayat = banyakbaris('riwayat.csv')
kolomriwayat = banyakkolom('riwayat.csv')

# 3.
def addriwayat(ID_Game,namagame,hargagame,ID_user,tahun):
    # Spesifikasi program : Menambahkan data riwayat pembelian game oleh user
    # ALGORITMA
    # Deklarasi array baru user
    riwayatbaru = ['' for i in range(5)]
    # mengisi array baru dengan data user baru
    riwayatbaru[0] = ID_Game
    riwayatbaru[1] = namagame
    riwayatbaru[2] = hargagame
    riwayatbaru[3] = ID_user
    riwayatbaru[4] = tahun

    # menambah array baru ke database
    arraydatariwayat[nextnumber()-1] += [riwayatbaru]
