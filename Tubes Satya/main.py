# Program main
# SIMULASI KERJA BINOMO
# Spesifikasi program : Program utama simulasi BINOMO

# KAMUS
# 
# 

# ALGORITMA
# import fungsi, prosedur, dan variabel buatan dari file login.py dan variables.py

import F09_ListGame as F09
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



# Lalu, menjalankan fungsi admin jika admin dan user jika user