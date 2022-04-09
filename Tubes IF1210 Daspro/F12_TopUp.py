# Spesifikasi program : Program untuk top up saldo dari user

# KAMUS
# 

# ALGORITMA
# import fungsi, prosedur, dan variabel buatan dari file lain
import variables as var 
csv ='C:/Users/Asus/Downloads/tubes/user.csv'
arraydatauser = var.csvtoarray(csv)
barisuser = var.banyakbaris(csv)
kolomuser = var.banyakkolom(csv)

def usernamevalid(username):
    for b in range(barisuser):
        if arraydatauser[b][1] == username:
            return True
    return False

def topup (arraydatauser):

    username = str(input("Masukan username: "))
    saldo = int(input("Masukan saldo: "))
    if (usernamevalid(username)):
        for b in range(barisuser):
            if arraydatauser[b][1] == username:
                i=b
        nama = arraydatauser[i][2]
        saldoawal = arraydatauser[i][5]
        saldoakhir = int(saldoawal) + saldo
        if (saldoakhir<0):
            print()
            print("Masukan tidak valid.")
        else:
            arraydatauser[i][5]=str(saldoakhir)
            print()
            print ("Top up berhasil. Saldo", nama, "bertambah menjadi",saldoakhir)
    else:
        print()
        print ('Username "'+str(username) + '" tidak ditemukan.' )