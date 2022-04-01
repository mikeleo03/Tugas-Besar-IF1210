# Program Variables
# Spesifikasi program : intialisasi variabel-variabel yang akan digunakan di program lain
# Kumpulan variabel-variabel yang akan dipanggil hasil pengolahan csv

# KAMUS
# username, password : string
# data, users : csv

def loginvalid(username,password):
    # Spesifikasi program : Memvalidasi apakah input username dan password sudah valid
	# ALGORITMA
    import csv
    with open('user.csv') as data:
        users = csv.reader(data,delimiter=',') # membaca data
        for row in users:
            if username in row[1] and password == row[3]:
                return True

def role(username,password):
    # Spesifikasi program : Menerima input username dan password serta mengeluarkan 
    # role yang dimiliki username
	# ALGORITMA
    import csv
    with open('user.csv') as data:
        users = csv.reader(data,delimiter=',') # membaca data
        for row in users:
            if username in row[1] and password == row[3]:
                return (row[4])

def nama(username):
    # Spesifikasi program : Menampilkan nama si pemilik username
	# ALGORITMA
    import csv
    with open('user.csv') as data:
        users = csv.reader(data,delimiter=',') # membaca data
        for row in users:
            if username in row[1]:
                return (row[2])