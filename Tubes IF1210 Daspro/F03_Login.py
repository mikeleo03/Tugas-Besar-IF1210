# Program Login
# Spesifikasi program : Program yang akan diterima user/admin saat pertama kali masuk aplikasi

# KAMUS
# username, password : string
# success : boolean

# ALGORITMA
# import fungsi, prosedur, dan variabel buatan dari file lain
import function as func
import variables as var
import B01_Cipher as B01

def loginvalid(username,password,arr_user):
    # Spesifikasi program : Memvalidasi apakah input username dan password sudah valid
	# ALGORITMA
    baris = var.length(arr_user)
    for b in range(baris):
        if arr_user[b][1] == username and B01.cipher(arr_user[b][3]) == B01.cipher(password):
            return True

def login(arr_game,arr_kepemilikan,arr_riwayat,arr_user):
    # Spesifikasi program : Akses utama bagi setiap pengguna yang masuk
	# ALGORITMA
    func.clearScreen()
    username = ""
    password = ""
    success = False # flag
    while(success == False): # selama input salah, program akan terus meminta input
        print('''-------------------------------
          LOGIN PAGE
-------------------------------
''')
        username = input("Masukan username : ")
        password = input("Masukan password : ")
        if loginvalid(username,password,arr_user): # cek username dan pass valid
            print("Loading...")
            func.wait(1)
            func.clearLast
            print(f"Halo {var.nama(username,arr_user)}!, Selamat datang di 'Binomo!'")

            # Masuk main program
            iduser = int(var.user_id(username,arr_user))
            if var.role(username,password,arr_user) == "admin": # jika admin
                func.funcadmin(username,iduser,arr_game,arr_kepemilikan,arr_riwayat,arr_user)
            else: # var.role(username,password) == "user", jika bukan admin
                func.funcuser(username,iduser,arr_game,arr_kepemilikan,arr_riwayat,arr_user)
            func.wait(1.5)
            success = True
            return success
        else : # kalau username dan pass tidak valid 
            print("Loading...")
            func.wait(1)
            func.clearLast
            print("Password atau username salah atau tidak ditemukan.")
            func.wait(1.5)
            func.clearScreen()