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
  
def FindMin(M,col,row,x,mark):
    # Spesifikasi program : Mencari nilai minimum dari elemen matriks yang dipilih agar bisa melakukan sorting
    # KAMUS
    # i, j, k, x, col, row, mark: integer
    # min : array [1..col] of integer
    # M : array [1..row] of array [1..col] of string 
    # num1, num2 : string
    # ALGORITMA
    x = abs(x)
    min = [" " for k in range(col)]
    for j in range(row):
        if M[j][x]!=mark:
            for k in range(col):
                min[k] = M[j][k]
            break
    for j in range(row):
        if M[j][x]!=mark:
            if x!=4:
                if int(M[j][x])!=mark and int(M[j][x])<int(min[x]):
                    for k in range(col):
                        min[k] = M[j][k]
            else:
                num1 = ""
                num2 = ""
                for e in M[j][x]:
                    if e!=".": num1 += e
                for e in min[x]:
                    if e!=".": num2 += e
                if int(num1)!=mark and int(num1)<int(num2):
                    for k in range(col):
                        min[k] = M[j][k]
    return min

def FindMax(M,col,row,x,mark):
    # Spesifikasi program : Mencari nilai maksimum dari elemen matriks yang dipilih agar bisa melakukan sorting
    # KAMUS
    # i, j, k, x, col, row, mark: integer
    # max : array [1..col] of integer
    # M : array [1..row] of array [1..col] of string 
    # num1, num2 : string
    # ALGORITMA
    x = abs(x)
    max = [" " for k in range(col)]
    for j in range(row):
        if M[j][x]!=mark:
            for k in range(col):
                max[k] = M[j][k]
            break
    for j in range(row):
        if M[j][x]!=mark:
            if x!=4:
                if int(M[j][x])!=mark and int(M[j][x])>int(max[x]):
                    for k in range(col):
                        max[k] = M[j][k]
            else:
                num1 = ""
                num2 = ""
                for e in M[j][x]:
                    if e!=".": num1 += e
                for e in max[x]:
                    if e!=".": num2 += e
                if int(num1)!=mark and int(num1)>int(num2):
                    for k in range(col):
                        max[k] = M[j][k]
    return max         

def Fill_M(M,N,col,row,x,mark,min,max):
    # Spesifikasi program : Membuat matriks baru yang berisi nilai elemen yang sudah disorting sesuai dengan keinginan user
    # KAMUS
    # i, j, k, x, col, row, mark, con: integer
    # min, max : array [1..col] of integer
    # M, N : array [1..row] of array [1..col] of string 
    # num1, num2 : string
    # ALGORITMA
    con = 0
    j = 0
    if x>=0:
        while con<row:
            if M[j][x]==min[x]:
                for k in range(col):
                    N[con][k] = min[k]
                M[j][x] = mark
                min = FindMin(M,col,row,x,mark)
                j = 0
                con+=1
            else: j+=1
    else:
        x = abs(x)
        while con<row:
            if M[j][x]==max[x]:
                for k in range(col):
                    N[con][k] = max[k]
                M[j][x] = mark
                max = FindMax(M,col,row,x,mark)
                j = 0
                con+=1
            else: j+=1
    return N


def ListGame(M):
    # Spesifikasi program : Merupakan sub-program utama dalam sorting matriks, sub-program ini menjadi penghubung antara 
    # sub-program lainnya dalam menjalankan funcgsi list game ini
    # KAMUS
    # i, x, col, row, mark: integer
    # val : boolean
    # min, max : integer
    # M, N : array [1..row] of array [1..col] of string 
    # ALGORITMA
    mark = -9999
    col = 6
    row = var.length(M)
    SLG = [["" for i in range(col)] for j in range(row)]
    for i in range(col):
        SLG[0][i] = M[0][i]
    x = SSort()
    if x!=0 and x!=-165:
        min = FindMin(M,col,row,x,mark)
        max = FindMax(M,col,row,x,mark)
    val = True
    if x>0: SL = Fill_M(M,SLG,col,row,x,mark,min,max)                         # Menampilkan data naik
    elif x==0:
        print("Skema sorting berupa id")
        SL = M
    else:                                                                     # Menampilkan data turun
        if x==(-4) or x==(-3): SL = Fill_M(M,SLG,col,row,x,mark,min,max)      
        else: 
            val = False
            print("Skema Sorting tidak valid!")
    if val:
        showSort(SL,row)
