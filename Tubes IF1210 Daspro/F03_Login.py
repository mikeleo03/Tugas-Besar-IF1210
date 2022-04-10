# Program Login
# Spesifikasi program : Program yang akan diterima user/admin saat pertama kali masuk aplikasi

# KAMUS
# username, password : string
# success : boolean

# ALGORITMA
# import fungsi, prosedur, dan variabel buatan dari file lain
import function as func
import variables as var

import F02_Register
import F08_BuyGame
import F10_SearchInventory
import F11_SearchGameAtStore
import F12_TopUp
import F13_Riwayat
import F14_Help

arr_game= var.csvtoarray('game.csv')
arr_data= var.pop_firstline(var.csvtoarray('kepemilikan.csv'))
arr_hist= var.pop_firstline(var.csvtoarray("riwayat.csv"))
arraydatauser = var.csvtoarray('user.csv')

def funcuser(ID_user):
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
            F08_BuyGame.buygame(ID_user)
        
        elif (pilihLogin == 4): # search_my_game
            F10_SearchInventory.search_my_game()
        elif (pilihLogin == 5): # search_game_at_store
            F11_SearchGameAtStore.search_game_at_store(arr_game)
        elif (pilihLogin == 6): # riwayat
            F13_Riwayat.riwayat()
        elif (pilihLogin == 7): # help
            F14_Help.funchelpUser()

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
            F02_Register.registAdmin()
        elif (pilihLogin == 2): # tambah_game
            print("# jalan fungsi tambah_game")

        elif (pilihLogin == 6): # search_game_at_store
            F11_SearchGameAtStore.search_game_at_store(arr_game)
        elif (pilihLogin == 7): # topup
            F12_TopUp.topup(arraydatauser)
        elif (pilihLogin == 8): # help
            F14_Help.funchelpAdmin()

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
            funcuser(iduser)
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