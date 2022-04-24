import function as func
import variables as var
def SSort():
    # Spesifikasi program : Menerima input user dalam menentukan skema sorting yang diinginkan
    # KAMUS
    # S : string
    # ALGORITMA
    S = str(input("Skema Sorting : "))
    if S=="harga+":
        return 4
    elif S=="harga-":
        return -4
    elif S=="tahun+":
        return 3
    elif S=="tahun-":
        return -3
    elif S=='':
        return 0
    else: return -165

def showSort(M,row):
    # Spesifikasi program : Menampilkan skema sorting yang diinginkan ke layar
    # KAMUS
    # i, j, k, max, kol_i, sel : integer
    # PKolE : array [1..6] of integer
    # M : array [1..row] of array [1..6] of string 
    # e : string
    # ALGORITMA
    i = 0
    k = 0
    PKolE = [0 for k in range(6)]
    while i<6:
        max = func.lList(M[0][i])
        for j in range(row):
            if func.lList(M[j][i])>max:
                max = func.lList(M[j][i])
        PKolE[k] = max
        i+=1
        k+=1
    for j in range (row):
        for i in range(6):
            kol_i = func.lList(M[j][i])
            if kol_i==PKolE[i]:
                if i==0:
                    e = str(j+1)+". "+M[j][i]+" ||"
                else: 
                    e = M[j][i]+" ||"
                print(e, end="")
            else:
                sel = PKolE[i]-kol_i+1
                if i==0:
                    e = str(j+1)+"."+((sel)*" ")+M[j][i]+" ||"
                else :
                    e = M[j][i]+(sel*" ")+"||"
                print(e, end="")
            func.wait(0.001)
        print("")
  
def get_max(arr, index_start,index):
    max = int(arr[index_start][abs(index)])
    for i in range (index_start, var.length(arr)):
        if int(arr[i][index]) > max :
            max=int(arr[i][index])
    return max

def get_min(arr, index_start,index):
    min = int(arr[index_start][abs(index)])
    for i in range (index_start, var.length(arr)):
        if int(arr[i][index]) < min :
            min=int(arr[i][index])
    return min

def get_idx(arr, number, index):
    for i in range(len(arr)-1, -1, -1):
        if arr[i][abs(index)] == str(number):
            return i

def swap(array, indeks_1, indeks_2):
    arraytemp = array[indeks_1]
    array[indeks_1]=array[indeks_2]
    array[indeks_2]=arraytemp

def sortList(arr,index):
    val =True
    if index>0:
        for i in range(var.length(arr)):
            minArr = get_min(arr, i, index)
            minIdx = get_idx(arr, minArr,index)
            swap(arr, i, minIdx)   # Menampilkan data naik
    elif index==0:
        print("Skema sorting berupa id")
        return arr
    else:                                                                     # Menampilkan data turun
        if index==(-4) or index==(-3): 
            index = abs(index)
            for i in range(var.length(arr)):
                maxArr = get_max(arr, i, index)
                maxIdx = get_idx(arr, maxArr,index)
                swap(arr, i, maxIdx)    
        else: 
            val = False
            print("Skema Sorting tidak valid!")
    if val:
        return arr
    else:
        return 0

def ListGame(arr):
    # Spesifikasi program : mengurut

    # KAMUS LOKAL
    # kolom_data, baris_data, panjang_max : integer
    # arr_kolom : array [1..kolom_data] of integer

    # ALGORITMA
    # deklarasi array kosong
    index = SSort()
    arr_sort= sortList(arr,index)
    if arr_sort!=0:
        showSort(arr_sort, var.length(arr_sort))

    func.goBackEnter()
    func.clearScreen()
