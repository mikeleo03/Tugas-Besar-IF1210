# Program Login
# Spesifikasi program : Program yang akan diterima user/admin saat pertama kali masuk aplikasi

# KAMUS
# username, password : string
# success : boolean

# ALGORITMA
# import fungsi, prosedur, dan variabel buatan dari file lain
import function as func
import variables as var
import admin as adm
import user as us

func.clearScreen()
print('''-------------------------------
          LOGIN PAGE
-------------------------------
''')
username = ""
password = ""
success = False # flag
while(success == False): # selama input salah, program akan terus meminta input
    username = input("Masukan username : ")
    password = input("Masukan password : ")
    if var.loginvalid(username,password): # cek username dan pass valid
        print("Loading...")
        func.wait(1)
        func.clearLast
        print(f"Halo {var.nama(username)}!, Selamat datang di 'Binomo!'")

        # Masuk main program
        if var.role(username,password) == "admin": # jika admin
            adm.funcadmin()
        else: # var.role(username,password) == "user", jika bukan admin
            us.funcuser()
        func.wait(1.5)
        success = True
        break
    else : # kalau username dan pass tidak valid 
        print("Loading...")
        func.wait(1)
        func.clearLast
        print("Password atau username salah atau tidak ditemukan.")