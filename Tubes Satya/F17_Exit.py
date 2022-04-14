# Program Exit
# Spesifikasi program : Program yang akan dijalankan jika pengguna ingin keluar dari program

# KAMUS
# exit : procedure

# ALGORITMA

# import fungsi, prosedur, dan variabel buatan dari file lain
import F16_Save as F16

def exit(arr_game, arr_kepemilikan, arr_riwayat, arr_user):
    # Spesifikasi program : Mengakhiri program dan memberi pilihan save

	# KAMUS LOKAL
	# pilihan : string
    # F16.save() : procedure

	# ALGORITMA
    pilihan = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ") # menerima input pilihan
    
    while pilihan not in ["y", "n", "Y", "N"]: # pilihan tidak valid
        pilihan = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")

    if pilihan == "y" or pilihan == "Y": # melakukan save program
        F16.save(arr_game, arr_kepemilikan, arr_riwayat, arr_user)
