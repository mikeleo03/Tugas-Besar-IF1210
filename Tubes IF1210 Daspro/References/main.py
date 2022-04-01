# Program main
# SIMULASI KERJA BINOMO
# Spesifikasi program : Program utama simulasi BINOMO

# KAMUS
# nama, username_baru, pswd_baru : string
# pilihLogin : int

# ALGORITMA
# import fungsi, prosedur, dan variabel buatan dari file loginpage.py dan variables.py
import login as lp
import variables as var
import csv 
with open("user.csv",newline='') as user :
    reader = csv.reader(user)

pilihLogin = 100
while(pilihLogin != 0):
    lp.clearScreen()
    pilihLogin = lp.pilihLogin()
    if(pilihLogin == 1): # Daftar Akun
        print("REGISTER")
        nama = ""
        username_baru = ""
        pswd_baru = ""
        success = False
        # tries = 0
        while(success == False):
            nama = input("Masukan nama : ")
            username_baru = input("Masukan username : ")
            pswd_baru = input("Masukan password : ")
            if(username_baru not in var.akun[1]):
                success = True
                break
            lp.clearLast()
            print(f"Username {username_baru} sudah terpakai, silakan menggunakan username lain.")

        if(success): 
            var.akun[0].append(4)
            var.akun[1].append(username_baru)
            var.akun[2].append(nama)
            var.akun[3].append(pswd_baru)
            var.akun[4].append("user")
            var.akun[5].append(0)
            print(f"\nUsername {username_baru} telah berhasil register ke dalam “Binomo”.")
        lp.goBackEnter()
        lp.clearScreen()

    elif(pilihLogin == 2): # Login
        print('LOGIN')
        username = ""
        password = ""
        success = False
        while(success == False): # selama input salah, program akan terus meminta input
            username = input("Masukan username : ")
            password = input("Masukan password : ")
            for i in var.akun[1]:
                if i == username: # kalau username ada di database
                    idx = var.akun[1].index(username) # definisi index data di database
            if(password == var.akun[3][idx]): # cek username dan pass valid
                success = True
                break
            lp.clearLast
            print("Password atau username salah atau tidak ditemukan.") # kalau username dan pass tidak valid

        if(success): # kalau username dan pass valid
            print(f"\n Halo {var.akun[2][idx]}!, Selamat datang di 'Binomo!'")
            # Masuk main program
            # jika admin...
            # jika bukan admin...
            # lp.wait(1.5)
            # lp.clearScreen()
            # lp.SIX(var.akun, var.sudahAbsen, var.absensi, idx)
        else: 
            print("Maaf, anda harus login terlebih dahulu untuk mengirim perintah selain 'login'")

# exit program
print("Dadah, sampai jumpa lagi! :D")
lp.wait(1)