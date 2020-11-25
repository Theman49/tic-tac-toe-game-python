import random             # module untuk menggunakan random()

#inisiasi variable yang dibutuhkan
total = 4 # jumlah berapa kali pemain mendapatkan giliran main
totalPlay = 0 # inisisasi awal saat player1 main
scoreP1 = 0 # score awal player1
scoreP2 = 0 # score awal player2

# player
player = {
    1 : 'X',
    2 : 'O'
}
# board
board = [
    ['top1','top2','top3'],
    ['mid1','mid2','mid3'],
    ['btm1','btm2','btm3']
]
boardProgress = [
    ['_','_','_'],
    ['_','_','_'],
    ['_','_','_']
]


def get_random_pos(a):              
    n = 0
    while n < 1:
        random1 = random.randint(0,2)
        random2 = random.randint(0,2)                     # fungsi untuk mengambil bilangan acak untuk menentukan
        pos = board[random1][random2]
        cek = boardProgress[random1][random2]                     # baris dan kolom berapa yang belum terisi 'x' atau 'o'
        
        if cek != 'X' and cek != 'O':                     # jika != 'x' dan != 'o' maka akan diisikan sesuai bagian pemain
            boardProgress[random1][random2] = player[a]           # jika sudah terisi, maka akan mencari sampai ada tempat yang kosong
            n+=1
    print(pos + " -> " + player[a])

def user():
    n = 0
    while n < 1:
        row = int(input("row : "))
        col = int(input("col : "))                   # fungsi untuk mengambil bilangan acak untuk menentukan
        row-=1
        col-=1
        pos = board[row][col]                     # baris dan kolom berapa yang belum terisi 'x' atau 'o'
        cek = boardProgress[row][col]                     # baris dan kolom berapa yang belum terisi 'x' atau 'o'
        
        if cek != 'X' and cek != 'O':                     # jika != 'x' dan != 'o' maka akan diisikan sesuai bagian pemain
            boardProgress[row][col] = player[1]           # jika sudah terisi, maka akan mencari sampai ada tempat yang kosong
            n+=1
        else:
            print("Sudah Terisi")
    print(pos + " -> " + player[1])

def showingResult():
    print(boardProgress[0][0] + " | " + boardProgress[0][1] + " | " + boardProgress[0][2])    
    print("--|---|--")
    print(boardProgress[1][0] + " | " + boardProgress[1][1] + " | " + boardProgress[1][2])        # fungsi untuk menampilkan hasil akhir dari permainan
    print("--|---|--")
    print(boardProgress[2][0] + " | " + boardProgress[2][1] + " | " + boardProgress[2][2])

def whoWin(x,y):
    if x > y:
        result = ("Player 1 (X) win!!!")
    elif x == y:
        result = ("Draw")                                           # fungsi untuk menampilkan siapa pemenangnya antara player1 dan player2
    else:
        result = ("Player 1 (X) lose!!!")
    print("Result : " + result)

def boards(x):
    if x == 1:
        print("row\col\t   1\t   2\t   3")
        for i in range(3):
            print("  " + str(i+1) + "\t" + str(board[i]))
    if x == 2:
        print("row\col\t  1    2    3")
        for i in range(3):
            print("  " + str(i+1) + "\t" + str(boardProgress[i]))
    
# menampilkan board awal saat permainan akan dimulai
# for line in board:
#     print(line)
    
# guide
boards(1)
# print("row\col\t   1\t   2\t   3")
# for i in range(3):
#     print("  " + str(i+1) + "\t" + str(board[i]))

print("")

# permainan dimulai oleh player1
user()

# permainan dilanjutkan oleh player2 dan bergantian dengan player1 hingga masing mendapatkan 4x main dan board terisi penuh
while totalPlay < total:        # akan dijalankan jika totalPlay < total, pada awal permainan --> 0 < 4
    boards(2)
    get_random_pos(2)
    boards(2)
    user()
    totalPlay+=1                # setiap kali 2 pemain sudah mendapatkan giliran, maka totalPlay akan bertambah 1

print("")
showingResult()                 # memanggil fungsi menampilkan hasil akhir

# melakukan penilaian dari hasil akhir permainan
for i in range(3):
    # mengecek board setiap baris
    if boardProgress[i][0] == boardProgress[i][1] == boardProgress[i][2] == 'X':
        scoreP1+=1
    if boardProgress[i][0] == boardProgress[i][1] == boardProgress[i][2] == 'O':
        scoreP2+=1
    # mengecek boardProgress setiap kolom
    if boardProgress[0][i] == boardProgress[1][i] == boardProgress[2][i] == 'X':
        scoreP1+=1
    if boardProgress[0][i] == boardProgress[1][i] == boardProgress[2][i] == 'O':
        scoreP2+=1
# mengecek boardProgress posisi diagonal
if boardProgress[0][0] == boardProgress[1][1] == boardProgress[2][2] == 'X' or boardProgress[0][2] == boardProgress[1][1] == boardProgress[2][0] == 'X':
    scoreP1+=1
if boardProgress[0][0] == boardProgress[1][1] == boardProgress[2][2] == 'O' or boardProgress[0][2] == boardProgress[1][1] == boardProgress[2][0] == 'O':
    scoreP2+=1

print("")
print("score P1 (X) : " + str(scoreP1))
print("score P2 (O) : " + str(scoreP2))

whoWin(scoreP1, scoreP2)     # memanggil fungsi untuk menentukan siapa pemenangnya
