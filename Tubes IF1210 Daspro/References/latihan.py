success = False
nama = input("Masukan nama : ")
username_baru = input("Masukan username : ")
pswd_baru = input("Masukan password : ")
import csv
with open("user.csv",newline='') as user :
    data_user = csv.reader(user)
    for line in data_user:
        if(username_baru not in line[1]):
            success = True
            print("berhasil")
            break
        else :
            print(f"Username {username_baru} sudah terpakai, silakan menggunakan username lain.")