import function as fun    
def SSort():
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
    i = 0
    k = 0
    PKolE = [0 for k in range(6)]
    while i<6:
        max = fun.lList(M[0][i])
        for j in range(row):
            if fun.lList(M[j][i])>max:
                max = fun.lList(M[j][i])
        PKolE[k] = max
        i+=1
        k+=1
    for j in range (row):
        for i in range(6):
            kol_i = fun.lList(M[j][i])
            if kol_i==PKolE[i]:
                if i==0 and j!=0:
                    e = str(j)+". "+M[j][i]+" ||"
                else: 
                    e = M[j][i]+" ||"
                print(e, end="")
            else:
                sel = PKolE[i]-kol_i+1
                if i==0:
                    e = M[j][i]+((sel+2)*" ")+" ||"
                else :
                    e = M[j][i]+(sel*" ")+"||"
                print(e, end="")
            fun.wait(0.001)
        print("")
  
def FindMin(M,col,row,x,mark):
    x = abs(x)
    min = [" " for k in range(col)]
    for j in range(1,row):
        if M[j][x]!=mark:
            for k in range(col):
                min[k] = M[j][k]
            break
    for j in range(1,row):
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
    x = abs(x)
    max = [" " for k in range(col)]
    for j in range(1,row):
        if M[j][x]!=mark:
            for k in range(col):
                max[k] = M[j][k]
            break
    for j in range(1,row):
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
    con = 1
    j = 1
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


def SortList(M,col,row):
    mark = -9999
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
        
# Spesifikasi program : Menambahkan game pada list
# KAMUS
# file : csv
# GList : array [1..row] of array [1..col] of string
# ALGORITMA
file = open("game.csv",'r')
# # Definisi baris dan kolom (didefinisikan sebelumnya)
col = 6
row = fun.count_row("game.csv")
GList = fun.OpenCSV(file,col,row) # Menginput csv ke dalam array
SortList(GList,col,row)
