# Program Search_My_Game
# Spesifikasi program : Program yang akan dijalankan jika pengguna memilih "search_my_game" dan akan mencari game di inventory user

# KAMUS
# arr_game, arr_kepemilikan : array of string
# username : string

# ALGORITMA
# import fungsi, prosedur, dan variabel buatan dari file lain
import function as func
import variables as var

def my_game(username, arr_game, arr_kepemilikan):
    # Spesifikasi program : menghasilkan array dari inventory game user

    # KAMUS LOKAL
    # baris_data, baris_game, baris: integer
    # user_id : string
    # arr, arr_filter : array of string
    # i, j : integer

    # ALGORITMA
    user_id = var.user_id(username)
    #deklarasi array
    arr_data = var.pop_firstline(arr_kepemilikan)
    baris_data = var.length(arr_data) # baris dari array kepemilikan
    arr_game2 = var.pop_firstline(arr_game)
    baris_game = var.length(arr_game2)
    
    arr = ['' for i in range(baris_data)] # deklarasi array kosong
    baris=0
    for i in range (baris_data):
        if arr_data[i][1] == user_id:
            game_id = arr_data[i][0]
            arr[baris] = (var.array_search(arr_game2,baris_game,0, game_id)[0])[0] #memfilter array riwayat sesuai user_id
            baris +=var.array_search(arr_game2,baris_game,0, game_id)[1]

    arr_filter =['' for i in range(baris)] # deklarasi array lagi agar tidak ada array yg kosong
    for j in range (baris):
        arr_filter[j]=arr[j]

    return(arr_filter,baris)

def search_my_game(username, arr_game, arr_kepemilikan):
    # Spesifikasi program : menghasilkan array dari filter inventory game user, username sudah dicek dan pasti valid

    # KAMUS LOKAL
    # baris_mygame, parameter, kolom_search, baris2 : integer
    # user_id, game_id, tahun : string (string karena menyesuaikan dengan tipe data array)
    # arr_mygame, arr2 : array of string

    # ALGORITMA
    func.clearScreen()
    func.wait(1)
    print("=========== Search My Game ===========")
    game_id = str(input("Masukkan ID Game: "))
    tahun = str(input("Masukkan Tahun Rilis Game: "))
    
    arr_mygame,baris_mygame = my_game(username,arr_game, arr_kepemilikan)
    parameter = 0 # deklarasi jumlah parameter yang diinput user
    # filter data sesuai input parameter
    if (game_id ==""):
        arr_search = arr_mygame
        baris_search = baris_mygame
    elif not(game_id==""):
        arr2,baris2 = var.array_search(arr_mygame,baris_mygame,0,game_id)
        arr_search = arr2
        baris_search=baris2
        parameter+=1

    if not(tahun==""):
        arr2,baris2 = var.array_search(arr_search,baris_search,4,tahun)
        arr_search = arr2
        baris_search=baris2
        parameter+=1
    
    print()
    print("Daftar game pada inventory yang memenuhi kriteria:")
    if ((parameter>0) and (baris_search==0)) or (baris_search==0): # user memasukkan lebih dari 1 parameter dan tidak ada sesuai atau user tidak memiliki game
        print("Tidak ada game pada inventory-mu yang memenuhi kriteria")
    else:
        kolom_search = var.length(arr_search[0]) # menghitung panjang kolom dari array filter
        panjang_kolom = var.array_max_kolom(arr_search) # agar hasil output lebih rapi

        # menampilkan hasil array filter
        for i in range (baris_search):
            print (str(i+1) + ".",end=" ")
            for j in range (kolom_search):
                max_length = panjang_kolom[j]
                length_kolom = var.length(arr_search[i][j])
                if (j==kolom_search-2):
                    print(arr_search[i][j])
                elif (j!=5): # menampilkan hasil array kecuali kolom bagian user_id
                    print(arr_search[i][j]+ " "*(max_length-length_kolom),end=" | ")
    print()
    func.goBackEnter()
