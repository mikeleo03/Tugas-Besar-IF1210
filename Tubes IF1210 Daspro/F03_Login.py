# Program Login
# Spesifikasi program : Program yang akan diterima user/admin saat pertama kali masuk aplikasi

# KAMUS
# username, password : string
# success : boolean

# ALGORITMA
# import fungsi, prosedur, dan variabel buatan dari file lain
import function as func
import variables as var

import F02_Register as F02
import F08_BuyGame as F08
import F10_SearchInventory as F10
import F11_SearchGameAtStore as F11
import F12_TopUp as F12
import F13_Riwayat as F13
import F14_Help as F14

arr_game= var.csvtoarray('game.csv')
arr_data= var.pop_firstline(var.csvtoarray('kepemilikan.csv'))
arr_hist= var.pop_firstline(var.csvtoarray("riwayat.csv"))
arraydatauser = var.csvtoarray('user.csv')

def funcuser(username,ID_user):
    # Spesifikasi program : Memunculkan fitur yang dapat diakses user
	# KAMUS LOKAL
	# pilihLogin : int
	# ALGORITMA
    func.wait(1.5)
    func.clearScreen()
    # Mengimport fungsi pilih menu yang bisa dilakukan admin dan validasinya
    pilihLogin = 100
    while(pilihLogin != 0): # Masih bisa input pilihan
        func.clearScreen()
        pilihLogin = func.pilihMenuUser()
        if(pilihLogin == 1): # list_game_toko
            print("# jalan fungsi register")
        elif (pilihLogin == 2): # buy_game
            F08.buygame(ID_user)
        
        elif (pilihLogin == 4): # search_my_game
            F10.search_my_game(username)
        elif (pilihLogin == 5): # search_game_at_store
            F11.search_game_at_store(arr_game)
        elif (pilihLogin == 6): # riwayat
            F13.riwayat(username)
        elif (pilihLogin == 7): # help
            F14.funchelpUser()

def funcadmin():
    # Spesifikasi program : Memunculkan fitur yang dapat diakses admin
	# KAMUS LOKAL
	# pilihLogin : int
	# ALGORITMA
    func.wait(1.5)
    func.clearScreen()
    # Mengimport fungsi pilih menu yang bisa dilakukan admin dan validasinya
    pilihLogin = 100
    while(pilihLogin != 0): # Masih bisa input pilihan
        func.clearScreen()
        pilihLogin = func.pilihMenuAdmin()
        if(pilihLogin == 1): # register
            F02.registAdmin()
        elif (pilihLogin == 2): # tambah_game
            print("# jalan fungsi tambah_game")

        elif (pilihLogin == 6): # search_game_at_store
            F11.search_game_at_store(arr_game)
        elif (pilihLogin == 7): # topup
            F12.topup(arraydatauser)
        elif (pilihLogin == 8): # help
            F14.funchelpAdmin()

def login():
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
        if var.loginvalid(username,password): # cek username dan pass valid
            print("Loading...")
            func.wait(1)
            func.clearLast
            print(f"Halo {var.nama(username)}!, Selamat datang di 'Binomo!'")

            # Masuk main program
            iduser = int(var.user_id(username))
            if var.role(username,password) == "admin": # jika admin
                funcadmin()
            else: # var.role(username,password) == "user", jika bukan admin
                funcuser(username,iduser)
            func.wait(1.5)
            success = True
            break
        else : # kalau username dan pass tidak valid 
            print("Loading...")
            func.wait(1)
            func.clearLast
            print("Password atau username salah atau tidak ditemukan.")
            func.wait(1.5)
            func.clearScreen()