# Program User
# Spesifikasi program : Program yang akan dijalankan jika pengguna merupakan user

# KAMUS
# pilihLogin : int

# ALGORITMA
# import fungsi, prosedur, dan variabel buatan dari file lain
import function as func
import variables as var
#import help

def funcuser():
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
            print("# jalan fungsi tambah_game")
            # dst.....
        #elif (pilihLogin == 7): # help
            #help.funchelpUser()