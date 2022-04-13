# Program Kerang Ajaib
# Spesifikasi program : Program yang akan dijalankan jika pengguna memilih "kerangajaib" dan menampilkan jawaban acak dari pertanyaan

# KAMUS

# ALGORITMA
# import fungsi, prosedur, dan variabel buatan dari file lain
import function as func
import time
import variables as var

def lcg(x):
    # Spesifikasi program : algoritma dari LCG

    # KAMUS LOKAL
    # a, m, c : integer

    a = 10      # konstanta pengali (nilainya tidak akan berpengaruh pada hasil lcg)
    m = 5       # konstanta modulus (nilainya bergantung dengan banyaknya output yang dihasilkan)
    c = time.gmtime().tm_sec    # time.gmtime().tm_sec menghasilkan detik real time
    x = (a * x + c ) % m        # Persamaan lcg yang menghasilkan random number
    return x 

def kerangajaib():
    # Spesifikasi program : menampilkan jawaban secara acak

    # KAMUS LOKAL
    # num_rand, total : integer
    # question : string (string karena menyesuaikan dengan tipe data array)

    # ALGORITMA
    func.clearScreen()
    func.wait(1)
    print("=========== Kerang Ajaib ===========")
    question = str(input("Apa pertanyaan mu? "))
    total = var.length(question) # menghitung panjang pertanyaan
    num_rand = lcg(total) # menyimpan hasil angka dari algoritma LCG
    
    if (num_rand==0):
        print("Ya")
    elif (num_rand ==1):
        print("Tidak")
    elif (num_rand ==2):
        print("Bisa Jadi")
    elif (num_rand ==3):
        print("Mungkin")
    elif (num_rand ==4):
        print("Gak ada yang tau")