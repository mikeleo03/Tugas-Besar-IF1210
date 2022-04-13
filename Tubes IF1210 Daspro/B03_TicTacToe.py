# Program Tic-Tac-Toe
# Spesifikasi program : Program yang akan dijalankan jika pengguna ingin bermain tic-tac-toe

# KAMUS
# board : matriks character

# ALGORITMA
# import fungsi, prosedur, dan variabel buatan dari file lain
import function as func

# definisi papan tic-tac-toe
board = [['_' for b in range (3)] for k in range (3)]

def menang(char):
    # Spesifikasi program : Persyaratan agar salah satu pemain menang beserta outputnya
	# KAMUS LOKAL
	# char : character
    # board : matriks character
	# ALGORITMA
    # Menang secara horizontal
    if board[0][0] == board[0][1] == board[0][2] == char:
        print("Selamat!,",char,"menang secara horizontal.")
        return True
    elif board[1][0] == board[1][1] == board[1][2] == char:
        print("Selamat!,",char,"menang secara horizontal.")
        return True
    elif board[2][0] == board[2][1] == board[2][2] == char:
        print("Selamat!,",char,"menang secara horizontal.")
        return True
    # Menang secara vertikal
    elif board[0][0] == board[1][0] == board[2][0] == char:
        print("Selamat!,",char,"menang secara vertikal.")
        return True
    elif board[0][1] == board[1][1] == board[2][1] == char:
        print("Selamat!,",char,"menang secara vertikal.")
        return True
    elif board[0][2] == board[1][2] == board[2][2] == char:
        print("Selamat!,",char,"menang secara vertikal.")
        return True
    # Menang secara diagonal
    elif board[0][0] == board[1][1] == board[2][2] == char:
        print("Selamat!,",char,"menang secara diagonal.")
        return True
    elif board[0][2] == board[1][1] == board[2][0] == char:
        print("Selamat!,",char,"menang secara diagonal.")
        return True

def inputgagal(polabaris,polakolom):
    # Spesifikasi program : Validasi apakah input polabaris dan polakolom valid
	# KAMUS LOKAL
	# polabaris, polakolom : integer
	# ALGORITMA
    if (polabaris < 1 or polabaris > 3 or polakolom < 1 or polakolom > 3):
        return True

def inputpernah(polabaris,polakolom):
    # Spesifikasi program : Validasi apakah kotak input polabaris dan polakolom sudah pernah digunakan sebelumnya
	# KAMUS LOKAL
	# polabaris, polakolom : integer
	# ALGORITMA
    if board[polakolom-1][polabaris-1] == "O" or board[polakolom-1][polabaris-1] == "X":
        return True

def pemain(char):
    # Spesifikasi program : pola pengisian kotak yang dilakukan pemain beserta outputnya
	# KAMUS LOKAL
	# polabaris, polakolom : integer
    # char : character
    # board : matriks character
	# ALGORITMA
    while True:
        print(f"\nPemain {char}, silakan masukkan bagian yang ingin diisi")
        polabaris = int(input("Masukkan baris : "))
        polakolom = int(input("Masukkan kolom : "))
        if inputgagal(polabaris,polakolom):
            print("\ninput salah, silakan masukkan bilangann antara 1-3")
        else :
            if inputpernah(polabaris,polakolom):
                print("\nPola sudah pernah diisi sebelumnya, coba lagi")
            else:
                board[polakolom-1][polabaris-1] = char
                False
                for b in range (3):
                    for k in range (3):
                        print(board[b][k],end='')
                    print('')
                break

def tictactoe():
    # Spesifikasi program : fungsi tictactoe yang akan dipanggil di program utama
	# KAMUS LOKAL
	# counti, i : integer
    # attempt : array of character
    # board : matriks character
	# ALGORITMA
    func.clearScreen()
    func.wait(1)
    print('''=================================
        GAME TIC-TAC-TOE
=================================
''')
    print("Selamat datang kembali!")
    func.wait(1)
    print('''\n++ Peraturan Dasar ++
Pemain 1 akan menggunakan tanda X
Pemain 2 akan menggunakan tanda O
Pemain yang menyelesaikan 3 tanda berturut-turut akan menjadi pemenang!
''')
    print("++ Kondisi awal papan ++")

    for b in range (3):
        for k in range (3):
            print(board[b][k],end='')
        print('')

    print("\n++ Permainan dimulai! ++")

    counti = 9
    attempt = ['' for i in range(9)] # inisialisasi
    # kumpulan character dalam array untuk proses pergiliran
    for i in range(1,10):
        if (i % 2) != 0:
            attempt[i-1] = "X"
        else:
            attempt[i-1] = "O"

    # Proses permainannya berjalan, dan output jika menang dan seri
    for i in range(9):
        pemain(attempt[i])
        counti -= 1
        if menang('X') or menang('O'):
            break
        elif counti == 0:
            print("Permainan berakhir seri!")
            break

    func.goBackEnter()