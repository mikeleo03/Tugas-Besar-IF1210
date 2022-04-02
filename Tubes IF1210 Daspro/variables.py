# Program Variables
# Spesifikasi program : intialisasi variabel-variabel yang akan digunakan di program lain
# Kumpulan variabel-variabel yang akan dipanggil hasil pengolahan csv

# KAMUS
# username, password : string
# data, users : csv

# KUMPULAN SUBPROGRAM PENGOLAHAN DATA USER.CSV
# 1. Mengubah user.csv menjadi array arraydatauser 
datauser = open("user.csv")
stringdata = datauser.read()
datauser.close()
# menambahkan "\n" jika belum
if not(stringdata.endswith("\n")):
    stringdata += "\n"

# banyak char pada data
chara = 0
for row in stringdata:
    chara += 1

# definisi baris dan kolom (didefinisikan sebelumnya)  
kolom = 6
baris = 4

# Inisiasi array data
arraydatauser = [["" for k in range (kolom)] for b in range (baris)]
start = 0
finish = -1
# mengisi arrydata dengan data dari csv
for b in range(baris):
    for k in range(kolom):
        start = finish + 1
        if (k == kolom - 1):
            finish = stringdata[start:chara].find('\n') + finish + 1
        else:
            finish = stringdata[start:chara].find(',') + finish + 1
        arraydatauser[b][k] = stringdata[start:finish]

# 2.
def loginvalid(username,password):
    # Spesifikasi program : Memvalidasi apakah input username dan password sudah valid
	# ALGORITMA
    # definisi baris dan kolom (didefinisikan sebelumnya)  
    kolom = 6
    baris = 4

    # Validasi username dan password
    for b in range(baris):
        if arraydatauser[b][1] == username and arraydatauser[b][3] == password:
            return True

# 3.
def role(username,password):
    # Spesifikasi program : Menerima input username dan password serta mengeluarkan 
    # role yang dimiliki username
	# ALGORITMA
    # definisi baris dan kolom (didefinisikan sebelumnya)  
    kolom = 6
    baris = 4

    # Cek role berdasar username
    for b in range(baris):
        if arraydatauser[b][1] == username and arraydatauser[b][3] == password:
            return arraydatauser[b][4]

# 4.
def nama(username):
    # Spesifikasi program : Menampilkan nama si pemilik username
	# ALGORITMA
    # definisi baris dan kolom (didefinisikan sebelumnya)  
    kolom = 6
    baris = 4

    # outputkan nama berdasarkan username
    for b in range(baris):
        if arraydatauser[b][1] == username:
            return arraydatauser[b][2]

# 5.
def registervalid(username):
    # Spesifikasi program : Memvalidasi apakah input username tidak pernah digunakan
	# ALGORITMA
    # definisi baris dan kolom (didefinisikan sebelumnya)  
    kolom = 6
    baris = 4

    # Validasi username tidak pernah digunakan
    for b in range(baris):
        if arraydatauser[b][1] == username:
            return False

# 6.
def nextnumber():
    # Spesifikasi program : menentukan penomoran untuk data berikutnya
	# ALGORITMA
    # definisi baris dan kolom (didefinisikan sebelumnya)  
    kolom = 6
    baris = 4

    # Outputkan no data berikutnya
    for b in range(baris-1,1,-1): # reverse loop
        baris += 1
        return int(arraydatauser[b][0]) + 1

# 7.
def adduser(username_baru,nama,pswd_baru):
    # Spesifikasi program : Menambahkan data member baru pada list
    # ALGORITMA
    # definisi baris dan kolom (didefinisikan sebelumnya)  
    kolom = 6
    baris = 4

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

# Bisa dilanjut...
# KUMPULAN SUBPROGRAM PENGOLAHAN DATA GAME.CSV
# KUMPULAN SUBPROGRAM PENGOLAHAN DATA RIWAYAT.CSV dst