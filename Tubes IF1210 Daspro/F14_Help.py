# Program Help
# Spesifikasi program : Program yang akan dijalankan jika pengguna memilih "Help"

# KAMUS
# -

# ALGORITMA
# import fungsi, prosedur, dan variabel buatan dari file loginpage.py dan variables.py
import function as func

def help():
    # Spesifikasi program : Memunculkan akses help secara general
	# ALGORITMA
    func.wait(1)
    print('''============ HELP ============

++ FUNGSI ADMIN ++
1. register - Untuk melakukan registrasi user baru
2. tambah_game - Untuk menambah game yang dijual pada toko
3. ubah_game - Untuk mengubah game pada toko
4. ubah_stok - Untuk mengubah stok sebuah game pada toko
5. list_game_toko - Untuk melihat list game yang dijual pada toko
6. search_game_at_store - Untuk mencari game yang dijual pada toko
7. topup - Untuk menambahkan saldo pada user
8. Help - Memberikan panduan penggunaan pada sistem
9. Save - Untuk melakukan penyimpanan data ke dalam file setelah dilakukan perubahan
0. Logout - Untuk keluar dari aplikasi

++ FUNGSI USER ++
1. list_game_toko - Untuk melihat list game yang dijual pada toko
2. buy_game - Untuk membeli game yang ada di toko
3. list_game - Memberikan daftar game yang dipunyai user
4. search_my_game - Memberikan informasi detil mengenai game yang dipunyai user
5. search_game_at_store - Untuk mencari game yang dijual pada toko
6. riwayat - Untuk mengetahui daftar game yang pernah dibeli oleh user
7. Help - Memberikan panduan penggunaan pada sistem
8. Save - Untuk melakukan penyimpanan data ke dalam file setelah dilakukan perubahan
0. Logout - Untuk keluar dari aplikasi

00. Exit - Keluar dari sistem

++ FUNGSI BONUS - MINIGAME ++
1. magic_shell
2. tictactoe
''')
    func.goBackEnter()
    func.clearScreen()

def helpadmin():
    # Spesifikasi program : Memunculkan akses help untuk admin
	# ALGORITMA
    func.clearScreen()
    func.wait(1)
    print('''============ HELP ============

1. register - Untuk melakukan registrasi user baru
2. tambah_game - Untuk menambah game yang dijual pada toko
3. ubah_game - Untuk mengubah game pada toko
4. ubah_stok - Untuk mengubah stok sebuah game pada toko
5. list_game_toko - Untuk melihat list game yang dijual pada toko
6. search_game_at_store - Untuk mencari game yang dijual pada toko
7. topup - Untuk menambahkan saldo pada user
8. Help - Memberikan panduan penggunaan pada sistem
9. Save - Untuk melakukan penyimpanan data ke dalam file setelah dilakukan perubahan
0. Logout - Untuk keluar dari aplikasi

++ FUNGSI BONUS - MINIGAME ++
1. magic_shell
2. tictactoe
''')
    func.goBackEnter()
    func.clearScreen()

def helpuser():
    # Spesifikasi program : Memunculkan akses help untuk user
	# ALGORITMA
    func.clearScreen()
    func.wait(1)
    print('''============ HELP ============

1. list_game_toko - Untuk melihat list game yang dijual pada toko
2. buy_game - Untuk membeli game yang ada di toko
3. list_game - Memberikan daftar game yang dipunyai user
4. search_my_game - Memberikan informasi detil mengenai game yang dipunyai user
5. search_game_at_store - Untuk mencari game yang dijual pada toko
6. riwayat - Untuk mengetahui daftar game yang pernah dibeli oleh user
7. Help - Memberikan panduan penggunaan pada sistem
8. Save - Untuk melakukan penyimpanan data ke dalam file setelah dilakukan perubahan
0. Logout - Untuk keluar dari aplikasi

++ FUNGSI BONUS - MINIGAME ++
1. magic_shell
2. tictactoe
''')
    func.goBackEnter()
    func.clearScreen()