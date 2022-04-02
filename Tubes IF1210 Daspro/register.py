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

def yesorno():
    # Spesifikasi program : Menanayakan apakah akan melanjutkan memasukkan input
	# ALGORITMA
    print("Apakah akan melanjutkan memasukkan input? (y/n)")
    while True:
        pil = input()
        if (pil == "n" or pil == "y"):
            break
        else:
            print("input salah,masukkan y/n. (y/n)")
    return(pil)

def registAdmin():
    # Spesifikasi program : Memunculkan akses register new user untuk admin
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
        if var.registervalid(username_baru) != False:
            if usernamevalid(username_baru):
                print("Loading...")
                func.wait(1)
                success = True
            else :
                print("Loading...")
                func.wait(1)
                print("Username hanya dapat mengandung alfabet A-Z, a-z, underscore (_), strip (-), dan angka 0-9")
                if yesorno() == "n":
                    break
                else:
                    success = False
                func.wait(1)
                func.clearScreen()
        else:
            print("Loading...")
            func.wait(1)
            print(f"Username {username_baru} sudah terpakai, silakan menggunakan username lain.")
            if yesorno() == "n":
                break
            else:
                success = False
            func.wait(1)
            func.clearScreen()

    # jika sudah benar
    if(success): 
        # Menambahkan data member baru pada list
        var.adduser(username_baru,nama,pswd_baru)
        print(f"\nUsername {username_baru} telah berhasil register ke dalam “Binomo”.")
    func.goBackEnter()