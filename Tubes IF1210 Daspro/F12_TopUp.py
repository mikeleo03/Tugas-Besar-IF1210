# Program Top Up
# Spesifikasi program : Program untuk top up saldo dari user

# KAMUS

# array_user : array of user

# ALGORITMA
# import fungsi, prosedur, dan variabel buatan dari file lain
import function as func
import variables as var 


def topup (arr_user):
    # Spesifikasi program : menambahkan saldo pada user

    # KAMUS LOKAL
    # i, b, saldo, saldoakhir : integer
    # username, saldoawal, nama : string (string karena menyesuaikan dengan tipe data array)
    
    # ALGORITMA
    func.clearScreen()
    func.wait(1)
    print("=========== Top Up Saldo ===========")
    username = str(input("Masukan username: "))
    saldo = int(input("Masukan saldo: "))
    barisuser = var.length(arr_user)
    
    if (var.usernamevalid(username,arr_user)): # validasi username
        # mencari username yang sesuai di csv
        for b in range(barisuser):
            if arr_user[b][1] == username:
                i = b # menyimpan indeks tempat username
        nama = arr_user[i][2]
        saldoawal = arr_user[i][5]
        saldoakhir = int(saldoawal) + saldo
        if (saldoakhir<0): # jika saldo hasilnya kurang dari 0 maka tidak valid
            print()
            print("Masukan tidak valid.")
        elif saldo<0:
            arr_user[i][5]=str(saldoakhir)
            print()
            print ("Top up berhasil. Saldo", nama, "berkurang menjadi",saldoakhir)
        else:
            arr_user[i][5]=str(saldoakhir)
            print()
            print ("Top up berhasil. Saldo", nama, "bertambah menjadi",saldoakhir)
    else: # tidak ada username yang sesuai
        print()
        print ('Username "'+str(username) + '" tidak ditemukan.' )
    print()
    func.goBackEnter()
    return arr_user
