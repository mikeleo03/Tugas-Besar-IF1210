# Program BuyGame
# Spesifikasi program : User dapat membeli Game dengan menggunakan prosedur ini

# KAMUS
# ID_user : string

# ALGORITMA
# import fungsi, prosedur, dan variabel buatan dari file lain
import function as func
import variables as var

def addkepemilikan(gameid_baru,userid_baru,arr_kepemilikan):
    # Spesifikasi program : Menambahkan data game baru pada list kepemilikan
    # KAMUS LOKAL
    # userid_baru, baris : integer
    # gameid_baru : string
    # gamebaru, arr_kepemilikan : array of string
    # ALGORITMA
    # Deklarasi array baru user
    gamebaru = ['' for i in range(2)]
    baris = var.banyakbaris(arr_kepemilikan)
    # mengisi array baru dengan data user baru
    gamebaru[0] = gameid_baru
    gamebaru[1] = int(userid_baru)

    # menambah array baru ke database
    arr_kepemilikan[baris] += [gamebaru]

def addriwayat(ID_Game,namagame,hargagame,ID_user,tahun,arr_riwayat):
    # Spesifikasi program : Menambahkan data riwayat pembelian game oleh user
    # KAMUS LOKAL
    # hargagame, ID_user, tahun, baris : integer
    # ID_Game, namagame : string
    # riwayatbaru, arr_riwayat : array of string
    # ALGORITMA
    # Deklarasi array baru user
    riwayatbaru = ['' for i in range(5)]
    baris = var.banyakbaris(arr_riwayat)
    # mengisi array baru dengan data user baru
    riwayatbaru[0] = ID_Game
    riwayatbaru[1] = namagame
    riwayatbaru[2] = hargagame
    riwayatbaru[3] = ID_user
    riwayatbaru[4] = tahun

    # menambah array baru ke database
    arr_riwayat[baris] += [riwayatbaru]

def buygame(ID_user,arr_game, arr_kepemilikan, arr_riwayat, arr_user):
    # Spesifikasi program : Memunculkan akses buygame untuk user
    # KAMUS LOKAL
    # hargagame, saldo, indeksdata : integer
    # namagame, ID_Game : string
    # success, saldocukup, punya : boolean
    # gameid_kepemilikan, id_pemilik : array of string
    # data_game_toko, data_harga_game, data_stok_game : array of string
	# ALGORITMA
    func.clearScreen()
    func.wait(1)
    hargagame = 0
    saldo = 0
    indeksdata = 0
    namagame = ''
    ID_Game = ''
    success = False
    saldocukup = True
    punya = False

    bariskepemilikan = var.banyakbaris(arr_kepemilikan)
    barisgame = var.banyakbaris(arr_game)
    
    print("=========== Beli Game Baru ===========")
    ID_Game = input("Masukkan ID Game: ")
    # Masukkan semua data ke array
    gameid_kepemilikan = ['' for i in range(bariskepemilikan)]
    id_pemilik = ['' for i in range(bariskepemilikan)]
    data_game_toko = ['' for i in range(barisgame)]
    data_harga_game = ['' for i in range(barisgame)]
    data_stok_game = ['' for i in range(barisgame)]
    for b in range(bariskepemilikan):
        gameid_kepemilikan[b] = arr_kepemilikan[b][0]
        id_pemilik[b] = arr_kepemilikan[b][1]
    for b in range(barisgame):
        data_game_toko[b] = arr_game[b][0]
        data_harga_game[b] = arr_game[b][4]
        data_stok_game[b] = arr_game[b][5]
    saldo = int(arr_user[ID_user][5])
        
    # Pengolahan data berdasar kemungkinan
    for i in range(bariskepemilikan):
        # Kasus 1 : Game sudah dimiliki
        if gameid_kepemilikan[i] == ID_Game and int(id_pemilik[i]) == ID_user:
            success = False
            punya = True
            break
        else :
            for i in range(barisgame):
                # Kasus 2 : Berhasil, game ada, game belum dimiliki, dan saldo cukup
                if data_game_toko[i] == ID_Game and saldo >= int(data_harga_game[i]) and int(data_stok_game[i])>0:
                    indeksdata += i
                    namagame = ID_Game
                    hargagame += int(data_harga_game[i])
                    success = True
                    break
                # Kasus 3 : Game ada, game belum dimiliki, tetapi saldo tidak mencukupi
                elif data_game_toko[i] == ID_Game and saldo < int(data_harga_game[i]) and int(data_stok_game[i])>0:
                    saldocukup = False
                    break 
                # Kasus 4 : Game habis, game belum dimiliki, dan tidak ada di arraygame
                elif ID_Game not in data_game_toko :
                    success = False
                    break

    # Segala macam kemungkinan output
    if punya == True and success == False: # Jika game sudah dipunyai
        print("Loading...")
        func.wait(1)
        print("\nAnda sudah memiliki Game tersebut!")
    elif saldocukup == False and success == False: # Jika game ada, tapi saldo tidak cukup
        print("Loading...")
        func.wait(1)
        print("\nSaldo anda tidak cukup untuk membeli Game tersebut!")
    elif success == False : # Jika semuanya gagal
        print("Loading...")
        func.wait(1)
        print("\nStok Game tersebut sedang habis!") 
    elif success == True : # sudah sukses 
        print("Loading...")
        func.wait(1)
        # Mengurangi saldo, menambah game ke koleksi
        saldo -= hargagame
        addkepemilikan(ID_Game,ID_user,arr_kepemilikan)
        addriwayat(ID_Game,namagame,hargagame,ID_user,2022,arr_riwayat)
        print("\nGame",namagame,"berhasil dibeli!")
    func.goBackEnter()