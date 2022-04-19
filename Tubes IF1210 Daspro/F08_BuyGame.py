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
    baris = var.length(arr_kepemilikan)
    arr_kepemilikan += [['' for i in range(2)]]
    # mengisi array baru dengan data user baru
    arr_kepemilikan[baris][0] += gameid_baru
    arr_kepemilikan[baris][1] += userid_baru

    # menambah array baru ke database
    return arr_kepemilikan

def addriwayat(ID_Game,namagame,hargagame,ID_user,tahun,arr_riwayat):
    # Spesifikasi program : Menambahkan data riwayat pembelian game oleh user
    # KAMUS LOKAL
    # hargagame, ID_user, tahun, baris : integer
    # ID_Game, namagame : string
    # riwayatbaru, arr_riwayat : array of string
    # ALGORITMA
    # Deklarasi array baru user
    baris = var.length(arr_riwayat)
    arr_riwayat += [['' for i in range(5)]]
    # mengisi array baru dengan data user baru
    arr_riwayat[baris][0] += ID_Game
    arr_riwayat[baris][1] += namagame
    arr_riwayat[baris][2] += hargagame
    arr_riwayat[baris][3] += ID_user
    arr_riwayat[baris][4] += tahun

    # menambah array baru ke database
    return arr_riwayat

def buygame(ID_user,arr_game, arr_kepemilikan, arr_riwayat, arr_user):
    # Spesifikasi program : Memunculkan akses buygame untuk user
    # KAMUS LOKAL
    # saldo, indeksdata, stok : integer
    # namagame, ID_Game, hargagame : string
    # success, saldocukup, punya : boolean
    # gameid_kepemilikan, id_pemilik : array of string
    # data_game_toko, data_harga_game, data_stok_game : array of string
	# ALGORITMA
    func.clearScreen()
    func.wait(1)
    saldo = 0
    indeksdata = 0
    stok = 0
    hargagame = ''
    namagame = ''
    ID_Game = ''
    success = False
    saldocukup = True
    punya = False

    bariskepemilikan = var.length(arr_kepemilikan)
    barisgame = var.length(arr_game)-1
    
    print("=========== Beli Game Baru ===========")
    ID_Game = input("Masukkan ID Game: ")
    # Masukkan semua data ke array
    gameid_kepemilikan = ['' for i in range(bariskepemilikan)]
    id_pemilik = ['' for i in range(bariskepemilikan)]
    data_game_toko = ['' for i in range(barisgame)]
    data_nama_game = ['' for i in range(barisgame)]
    data_harga_game = ['' for i in range(barisgame)]
    data_stok_game = ['' for i in range(barisgame)]

    saldo = int(arr_user[ID_user-1][5])
    for b in range(bariskepemilikan):
        gameid_kepemilikan[b] = arr_kepemilikan[b][0]
        id_pemilik[b] = arr_kepemilikan[b][1]
    for k in range(barisgame):
        data_game_toko[k] = arr_game[k][0]
        data_nama_game[k] = arr_game[k][1]
        data_harga_game[k] = arr_game[k][4]
        data_stok_game[k] = arr_game[k][5]
        
    # Pengolahan data berdasar kemungkinan
    for i in range(bariskepemilikan):
        # Kasus 1 : Game sudah dimiliki
        if gameid_kepemilikan[i] == ID_Game and int(id_pemilik[i]) == int(ID_user):
            punya = True
            success = False
            break
        else :
            for i in range(barisgame):
                # Kasus 2 : Berhasil, game ada, game belum dimiliki, dan saldo cukup
                if data_game_toko[i] == ID_Game and saldo >= int(data_harga_game[i]) and int(data_stok_game[i])>0:
                    indeksdata += i
                    namagame = data_nama_game[i]
                    hargagame = data_harga_game[i]
                    # mengurangi stok
                    stokawal = data_stok_game[i]
                    stok = int(stokawal) - 1
                    arr_game[i][5] = str(stok)
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
    elif success == False and punya == False : # Jika semuanya gagal
        print("Loading...")
        func.wait(1)
        print("\nStok Game tersebut sedang habis!") 
    elif success == True : # sudah sukses 
        print("Loading...")
        func.wait(1)
        # Mengurangi saldo, menambah game ke koleksi
        saldo -= int(hargagame)
        addkepemilikan(ID_Game,str(ID_user),arr_kepemilikan)
        addriwayat(ID_Game,namagame,hargagame,str(ID_user),str(2022),arr_riwayat)
        arr_user[ID_user-1][5] = str(saldo)
        print("\nGame",namagame,"berhasil dibeli!")
    func.goBackEnter()
    func.clearScreen()
    return arr_game, arr_kepemilikan, arr_riwayat, arr_user