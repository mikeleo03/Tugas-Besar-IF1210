# Program Admin
# Spesifikasi program : Program yang akan dijalankan jika pengguna merupakan admin

# KAMUS
# pilihLogin : int

# ALGORITMA
# import fungsi, prosedur, dan variabel buatan dari file lain
import function as func
import variables as var
import help
import register

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
            register.registAdmin()
        elif (pilihLogin == 2): # tambah_game
            print("# jalan fungsi tambah_game")
            # dst.....
        elif (pilihLogin == 8): # help
            help.funchelpAdmin()