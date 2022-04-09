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

# len 
def length (arr):
    count = 0
    for i in arr:
        count = count + 1
    return count

# 6. pop baris pertama
def pop_firstline(arr):
    baris= length(arr)
    arr_baru = [[] for i in range (baris-1)]
    for i in range (baris-1):
        arr_baru[i] += arr[i+1]
    return arr_baru

# 7. remove
def popArr(arr, a):
    arr_baru=[]
    for i in range (length(arr)):
        if i!=a:
            arr_baru += [arr[i]]
    return arr_baru

# KUMPULAN SUBPROGRAM PENGOLAHAN DATA USER.CSV
# 1. Inisialisasi
arraydatauser = csvtoarray('C:/Users/Asus/Downloads/tubes/user.csv')
barisuser = banyakbaris('C:/Users/Asus/Downloads/tubes/user.csv')
kolomuser = banyakkolom('C:/Users/Asus/Downloads/tubes/user.csv')

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