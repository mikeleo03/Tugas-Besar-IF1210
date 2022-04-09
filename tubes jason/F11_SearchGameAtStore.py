import variables as var
game = 'C:/Users/Asus/OneDrive - Institut Teknologi Bandung/Documents/ITB/TPB ITB 2021/Daspro/tugas/tubes/Tubes IF1210 Daspro/CSV/game.csv'
arr_game= var.csvtoarray(game)
baris= var.banyakbaris(game)
kolom = var.banyakkolom(game)

def pop_firstline(arr):
    baris= var.length(arr)
    arr_baru = [[] for i in range (baris-1)]
    for i in range (baris-1):
        arr_baru[i] += arr[i+1]
    return arr_baru

def array_search (arr1, baris1, index, var_game):
    arr_search = []
    baris2 = 0
    for i in range (baris1):
        if (arr1[i][index]== var_game):
            arr_search += [arr1[i]]
            baris2 +=1
    return (arr_search, baris2)

def search_game_at_store (arr_game):
    id = str(input("Masukkan ID Game: "))
    nama = str(input("Masukkan Nama Game: "))
    harga = str(input("Masukkan Harga Game: "))
    kategori = str(input("Masukkan Kategori Game: "))
    tahun = str(input("Masukkan Tahun Rilis Game: "))
    #deklarasi
    baris_game = baris-1
    baris_search = 0
    parameter = 0
    if (id==""):
        arr_search = pop_firstline(arr_game)
        baris_search = baris_game
    elif not(id==""):
        (arr_search,baris_search) = array_search(pop_firstline(arr_game), baris_game,0,id)
        parameter+=1

    if not(nama==""):
        (arr_search1,baris_search1) = array_search(arr_search, baris_search,1,nama)[0]
        baris_search1 = array_search(arr_search, baris_search,1,nama)[1]
        arr_search = arr_search1
        baris_search = baris_search1
        parameter+=1

    if not(kategori==""):
        arr_search1= array_search(arr_search, baris_search,2,kategori)[0]
        baris_search1 = array_search(arr_search, baris_search,2,kategori)[1]
        arr_search = arr_search1
        baris_search = baris_search1
        parameter+=1

    if not(tahun==""):
        arr_search1 = array_search(arr_search, baris_search,3,tahun)[0]
        baris_search1 = array_search(arr_search, baris_search,3,tahun)[1]
        arr_search = arr_search1
        baris_search = baris_search1
        parameter+=1
    
    if not(harga==""):
        arr_search1 = array_search(arr_search, baris_search,4,harga)[0]
        baris_search1 = array_search(arr_search, baris_search,4,harga)[1]
        arr_search = arr_search1
        baris_search = baris_search1
        parameter+=1
    
    print()
    print("Daftar Game pada toko yang memenuhi kriteria: ")
    if (parameter>0) and (baris_search==0):
        print("Tidak ada game pada toko yang memenuhi kriteria")
    else:
        for i in range (baris_search):
            print (str(i+1) + ".",end=" ")
            for j in range (kolom):
                if (j==kolom-1):
                    print(arr_search[i][j])
                else:
                    print(arr_search[i][j],end=" | ")
        
search_game_at_store(arr_game)
