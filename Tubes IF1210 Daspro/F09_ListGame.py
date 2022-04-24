# Program List Game
# Spesifikasi program : Program yang akan dijalankan jika pengguna ingin melihat game yang dimiliki

# KAMUS
# var : module
# game_list : procedure

# ALGORITMA

# import fungsi, prosedur, dan variabel buatan dari file lain
import variables as var

def game_list(user_id, arr_kepemilikan, arr_game):
    # Spesifikasi program : Menampilkan list game yang dimiliki

	# KAMUS LOKAL
	# cond : bool
    # games : array of string
    # user_id : integer
    # arr_kepemilikan, arr_game: array of array of string
    # count, i, j, k, l, m : integer

	# ALGORITMA
    cond = False
    games = ["" for j in range(var.length(arr_kepemilikan))] # inisialisasi array game yang dimiliki
    count = 0

    for i in range(var.length(arr_kepemilikan)): # melakukan pengulangan untuk menghitung jumlah game
        if arr_kepemilikan[i][1] == str(user_id):
            cond = True
            games[count] = arr_kepemilikan[i][0]
            count = count + 1
    
    for k in range(var.length(arr_game)):   # melakukan pengulangan untuk menuliskan list ke layar
        for m in range(var.length(arr_kepemilikan)):
            if arr_game[k][0] == games[m]:
                print(str(m+1) + ".", end=" ")
                for l in range(5):
                    if l == 4:
                        print(arr_game[k][l])
                    else:
                        print(arr_game[k][l], end="  |  ")
    
    # menuliskan ke layar jika tidak ada game yang dimiliki
    if not cond:
        print("Maaf, kamu belum membeli game. Ketik perintah beli_game untuk beli")
