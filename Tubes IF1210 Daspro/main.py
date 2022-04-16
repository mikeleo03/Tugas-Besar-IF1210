# Program main
# SIMULASI KERJA BINOMO
# Spesifikasi program : Program utama simulasi BINOMO

# KAMUS
# 
# 

# ALGORITMA
# import fungsi, prosedur, dan variabel buatan dari file login.py dan variables.py
import function as func
import variables as var

import F02_Register as F02
import F03_Login as F03
import F08_BuyGame as F08
import F09_ListGame as F09
import F10_SearchInventory as F10
import F11_SearchGameAtStore as F11
import F12_TopUp as F12
import F13_Riwayat as F13
import F14_Help as F14
import F15_Load as F15
import F16_Save as F16
import F17_Exit as F17
import function as func

F15.load()

arr_game = F15.load_data()[0]
arr_kepemilikan = F15.load_data()[1]
arr_riwayat = F15.load_data()[2]
arr_user = F15.load_data()[3]
user_id = 1 #contoh

import function as func
import variables as var

'''
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
'''

benar = True
while benar:
    print("Meminta perintah berikutnya")
    ketik = input()
    if (ketik == "list_game"):
        F09.game_list(user_id, arr_kepemilikan, arr_game)
    elif (ketik == "save"):
        func.wait(3)
        F16.save(arr_game, arr_kepemilikan, arr_riwayat, arr_user)
    elif (ketik == "exit"):
        func.wait(3)
        F17.exit(arr_game, arr_kepemilikan, arr_riwayat, arr_user)
        benar = False
    else:
        print("\nperintah tidak valid, silahkan input ulang")
        benar = True


# Fungsi yang mungkin masuk loop pilih menu (Kumpulin sini dulu ges)
F02.registAdmin(arr_user)
F03.login(arr_user)
F08.buygame(user_id,arr_game, arr_kepemilikan, arr_riwayat, arr_user)
F09.game_list(user_id, arr_kepemilikan, arr_game)
F14.help()
F16.save(arr_game, arr_kepemilikan, arr_riwayat, arr_user)
F17.exit(arr_game, arr_kepemilikan, arr_riwayat, arr_user)