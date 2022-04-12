import F16_Save as F16


def exit(arr_game, arr_kepemilikan, arr_riwayat, arr_user):
    pilihan = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
    
    while pilihan not in ["y", "n", "Y", "N"]:
        pilihan = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")

    if pilihan == "y" or pilihan == "Y":
        F16.save(arr_game, arr_kepemilikan, arr_riwayat, arr_user)