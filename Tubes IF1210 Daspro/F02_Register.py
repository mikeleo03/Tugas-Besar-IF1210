# Program Register
# Spesifikasi program : Program yang akan dijalankan jika pengguna memilih "Register"

# KAMUS
# nama, username_baru, pswd_baru : string
# success : boolean

# ALGORITMA
# import fungsi, prosedur, dan variabel buatan dari file lain
import function as func
import variables as var

def usernamevalid(username):
    # Spesifikasi program : Memeriksa apakah username sudah valid
    # KAMUS LOKAL
    # valid : boolean
    # i, username : string
	# ALGORITMA
    # menggunakan pendekatan ASCII
    # A - Z : 65 - 90
    # a - z : 97 - 122
    # _ : 95, - : 45
    # 0 - 9 : 48 - 57
    valid = True
    for i in username:
        if not(ord(i)==45 or (48<=ord(i)<=57) or (65<=ord(i)<=90) or ord(i)==95 or (97<=ord(i)<=122)):
            valid = False
    return valid

def registervalid(username,arr_user):
    # Spesifikasi program : Memvalidasi apakah input username tidak pernah digunakan
    # KAMUS LOKAL
    # baris, b : integer
    # username : string
    # arr_user : array of string
	# ALGORITMA
    baris = var.length(arr_user)
    for b in range(baris):
        if arr_user[b][1] == username:
            return False

def adduser(username_baru,nama,pswd_baru,arr_user):
    # Spesifikasi program : Menambahkan data member baru pada list
    # KAMUS LOKAL
    # baris : integer
    # username_baru, nama, pswd_baru : string
    # baru, arr_user : array of string
    # ALGORITMA
    # Deklarasi array baru user
    baris = var.length(arr_user)
    arr_user += [['' for i in range(6)]]
    # mengisi array baru dengan data user baru
    arr_user[baris][0] += str(baris+1)
    arr_user[baris][1] += username_baru
    arr_user[baris][2] += nama
    arr_user[baris][3] += pswd_baru
    arr_user[baris][4] += "user"
    arr_user[baris][5] += str(0)

    # menambah array baru ke database
    return arr_user

def yesorno():
    # Spesifikasi program : Menanayakan apakah akan melanjutkan memasukkan input
    # KAMUS LOKAL
    # pil : string
	# ALGORITMA
    while True:
        print("Apakah akan melanjutkan memasukkan input? (y/n)")
        pil = input()
        if (pil == "n" or pil == "y"):
            break
        else:
            print("input salah,masukkan y/n. (y/n)")
    return(pil)

def registAdmin(arr_user):
    # Spesifikasi program : Memunculkan akses register new user untuk admin
    # KAMUS LOKAL
    # success : boolean
    # baris : integer
    # username_baru, nama, pswd_baru : string
    # baru, arr_user : array of string
	# ALGORITMA
    func.clearScreen()
    func.wait(1)
    nama = ""
    username_baru = ""
    pswd_baru = ""
    success = False
    while(success == False): # selama masih belum valid, akan meminta input
        print("=========== Daftarkan User Baru ===========")
        nama = input("Masukan nama : ")
        username_baru = input("Masukan username : ")
        pswd_baru = input("Masukan password : ")
        if registervalid(username_baru,arr_user) != False:
            if usernamevalid(username_baru):
                print("Loading...")
                func.wait(1)
                success = True
            else :
                print("Loading...")
                func.wait(1)
                print("\nUsername hanya dapat mengandung alfabet A-Z, a-z, underscore (_), strip (-), dan angka 0-9")
                if yesorno() == "n":
                    break
                else:
                    success = False
                func.wait(1)
                func.clearScreen()
        else:
            print("Loading...")
            func.wait(1)
            print(f"\nUsername {username_baru} sudah terpakai, silakan menggunakan username lain.")
            if yesorno() == "n":
                break
            else:
                success = False
            func.wait(1)
            func.clearScreen()

    # jika sudah benar
    if(success): 
        # Menambahkan data member baru pada list
        adduser(username_baru,nama,pswd_baru,arr_user)
        print(f"\nUsername {username_baru} telah berhasil register ke dalam “Binomo”.")
    func.goBackEnter()
    func.clearScreen()
