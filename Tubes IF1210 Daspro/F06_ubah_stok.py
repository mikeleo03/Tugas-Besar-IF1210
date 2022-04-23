import function as func
def UbahStok(M):
    # Spesifikasi program : Menambahkan stok game pada matriks
    # KAMUS
    # M : array [1..row] of array [1..col] of string
    # row, s, result : integer
    # Val,Found : boolean
    # ALGORITMA
    Id = str(input("Masukkan id game : "))
    Val = True
    Found = False
    i = 0
    row = func.count_row("game.csv")
    while Found==False and i<row:
        if Id==M[i][0]:
            Found = True
        else: i+=1
    if Found:
        s = int(input("Masukkan jumlah : "))
        result = int(M[i][5]) + s
        if s>0:
            print("Stok game",M[i][1],"berhasil ditambah. stok sekarang : "+str(result))
            M[i][5] = str(result)
        else:
            if result>=0:
                print("Stok game",M[i][1],"berhasil dikurangi. stok sekarang : "+str(result))
                M[i][5] = str(result)
            else:
                print("Stok game",M[i][1],"gagal dikurangi. stok sekarang : ",M[i][5],"(<"+str(s)+")")
                Val = False
    else: 
        print("Tidak ada game dengan ID tersebut")
    # Jika stok berhasil diubah
    if Val:
        return M
