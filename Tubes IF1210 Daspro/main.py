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

import F03_Login as F03
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

import function as func
import variables as var

benar = True
while benar:
    print("\nMeminta perintah berikutnya")
    ketik = input()
    if (ketik == "login"):
        func.wait(2)
        F03.login(arr_game,arr_kepemilikan,arr_riwayat,arr_user)
    elif (ketik == "help"):
        func.wait(2)
        F14.help()
    elif (ketik == "exit"):
        func.wait(2)
        F17.exit(arr_game,arr_kepemilikan, arr_riwayat,arr_user)
        benar = False
        break
    else:
        print("\nperintah tidak valid, silahkan input ulang")
        benar = True