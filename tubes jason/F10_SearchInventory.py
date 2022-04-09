import variables as var
game = 'C:/Users/Asus/OneDrive - Institut Teknologi Bandung/Documents/ITB/TPB ITB 2021/Daspro/tugas/tubes/Tubes IF1210 Daspro/CSV/game.csv'
data_inv = 'C:/Users/Asus/OneDrive - Institut Teknologi Bandung/Documents/ITB/TPB ITB 2021/Daspro/tugas/tubes/Tubes IF1210 Daspro/CSV/kepemilikan.csv'
hist = 'C:/Users/Asus/OneDrive - Institut Teknologi Bandung/Documents/ITB/TPB ITB 2021/Daspro/tugas/tubes/Tubes IF1210 Daspro/CSV/riwayat.csv'
arr_game= var.pop_firstline(var.csvtoarray(game))
baris_game= var.length(arr_game) 
kolom_game = var.length(arr_game[0])

arr_data= var.pop_firstline(var.csvtoarray(data_inv))
baris_data= var.length(arr_data)
kolom_data = var.length(arr_data[0])

arr_hist= var.pop_firstline(var.csvtoarray(hist))
baris_hist= var.length(arr_hist)
kolom_hist = var.length(arr_hist[0])

def array_search (arr1, baris1, index, var1):
    arr_search = []
    baris2 = 0
    for i in range (baris1):
        if (arr1[i][index]== var1):
            arr_search+= [arr1[i]]
            baris2 +=1
    return (arr_search, baris2)

def my_game(user_id):
    baris_inv = var.length(arr_data)
    arr=[[]]
    baris=0
    for i in range (baris_inv):
        if arr_data[i][1] == user_id:
            arr,baris = array_search(arr_hist,baris_hist,3,user_id)
    return(arr,baris)

def search_my_game(username,arr_game,arr_data,arr_hist):
    user_id = '1'
    id = str(input("Masukkan ID Game: "))
    tahun = str(input("Masukkan Tahun Rilis Game: "))
    
    arr_mygame,baris_mygame = my_game(user_id)
    parameter = 0
    if (id ==""):
        arr_search = arr_mygame
        baris_search = baris_mygame
    elif not(id==""):
        arr2,baris2 = array_search(arr_mygame,baris_mygame,0,id)
        arr_search = arr2
        baris_search=baris2
        parameter+=1

    if not(tahun==""):
        arr2,baris2 = array_search(arr_search,baris_search,4,tahun)
        arr_search = arr2
        baris_search=baris2
        parameter+=1
    
    print()
    print("Daftar game pada inventory yang memenuhi kriteria:")
    if (parameter>0) and (baris_search==0):
        print("Tidak ada game pada inventory-mu yang memenuhi kriteria")
    else:
        kolom = var.length(arr_search[0])
        for i in range (baris_search):
            print (str(i+1) + ".",end=" ")
            for j in range (kolom):
                if (j==kolom-1):
                    print(arr_search[i][j])
                elif (j!=3):
                    print(arr_search[i][j],end=" | ")

