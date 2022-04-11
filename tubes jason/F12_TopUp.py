# Program Top Up
# Spesifikasi program : Program untuk top up saldo dari user

# KAMUS
# csv : CSV
# arraydatauser : array of csv
# barisuser, kolomuser : integer

# ALGORITMA
# import fungsi, prosedur, dan variabel buatan dari file lain
import function as func
import variables as var 
csv ='C:/Users/Asus/Downloads/tubes/user.csv'
arraydatauser = var.csvtoarray(csv)
barisuser = var.banyakbaris(csv)
kolomuser = var.banyakkolom(csv)

def topup (arraydatauser):
    # Spesifikasi program : menambahkan saldo pada user

    # KAMUS LOKAL
    # i, b : integer
    # username, saldo : string (string karena menyesuaikan dengan tipe data array)
    
    # ALGORITMA
    func.clearScreen()
    func.wait(1)
    print("=========== Top Up Saldo ===========")
    username = str(input("Masukan username: "))
    saldo = int(input("Masukan saldo: "))

    if (var.usernamevalid(username)): # validasi username
        # mencari username yang sesuai di csv
        for b in range(barisuser):
            if arraydatauser[b][1] == username:
                i = b # menyimpan indeks tempat username
        nama = arraydatauser[i][2]
        saldoawal = arraydatauser[i][5]
        saldoakhir = int(saldoawal) + saldo
        if (saldoakhir<0): # jika saldo hasilnya kurang dari 0 maka tidak valid
            print()
            print("Masukan tidak valid.")
        else:
            arraydatauser[i][5]=str(saldoakhir)
            print()
            print ("Top up berhasil. Saldo", nama, "bertambah menjadi",saldoakhir)
    else: # tidak ada username yang sesuai
        print()
        print ('Username "'+str(username) + '" tidak ditemukan.' )
    print()
    func.goBackEnter()



