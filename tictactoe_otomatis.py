import random             # module untuk menggunakan random()

#inisiasi variable yang dibutuhkan
total = 4 # jumlah berapa kali pemain mendapatkan giliran main
totalPlay = 0 # inisisasi awal saat player1 main
scoreP1 = 0 # score awal player1
scoreP2 = 0 # score awal player2

# player
player = {
    1 : 'x',
    2 : 'o'
}
# board
board = [
    ['top1','top2','top3'],
    ['mid1','mid2','mid3'],
    ['btm1','btm2','btm3']
]

def get_random_pos(a):              
    n = 0
    while n < 1:
        random1 = random.randint(0,2)
        random2 = random.randint(0,2)                     # fungsi untuk mengambil bilangan acak untuk menentukan
        pos = board[random1][random2]                     # baris dan kolom berapa yang belum terisi 'x' atau 'o'
        
        if pos != 'x' and pos != 'o':                     # jika != 'x' dan != 'o' maka akan diisikan sesuai bagian pemain
            board[random1][random2] = player[a]           # jika sudah terisi, maka akan mencari sampai ada tempat yang kosong
            n+=1
    print(pos + " -> " + player[a])

def showingResult():
    print(board[0][0] + " | " + board[0][1] + " | " + board[0][2])    
    print("--|---|--")
    print(board[1][0] + " | " + board[1][1] + " | " + board[1][2])        # fungsi untuk menampilkan hasil akhir dari permainan
    print("--|---|--")
    print(board[2][0] + " | " + board[2][1] + " | " + board[2][2])

def whoWin(x,y):
    if x > y:
        result = ("Player 1 (x) win!!!")
    elif x == y:
        result = ("Draw")                                           # fungsi untuk menampilkan siapa pemenangnya antara player1 dan player2
    else:
        result = ("Player 1 (x) lose!!!")
    print("Result : " + result)


# menampilkan board awal saat permainan akan dimulai
for line in board:
    print(line)

print("")

# permainan dimulai oleh player1
get_random_pos(1)

# permainan dilanjutkan oleh player2 dan bergantian dengan player1 hingga masing mendapatkan 4x main dan board terisi penuh
while totalPlay < total:        # akan dijalankan jika totalPlay < total, pada awal permainan --> 0 < 4
    get_random_pos(2)
    get_random_pos(1)
    totalPlay+=1                # setiap kali 2 pemain sudah mendapatkan giliran, maka totalPlay akan bertambah 1

print("")
showingResult()                 # memanggil fungsi menampilkan hasil akhir

# melakukan penilaian dari hasil akhir permainan
for x in range(3):
    # mengecek board setiap baris
    if board[x][0] == board[x][1] == board[x][2] == 'x':
        scoreP1+=1
    if board[x][0] == board[x][1] == board[x][2] == 'o':
        scoreP2+=1
    # mengecek board setiap kolom
    if board[0][x] == board[1][x] == board[2][x] == 'x':
        scoreP1+=1
    if board[0][x] == board[1][x] == board[2][x] == 'o':
        scoreP2+=1
# mengecek board posisi diagonal
if board[0][0] == board[1][1] == board[2][2] == 'x' or board[0][2] == board[1][1] == board[2][0] == 'x':
    scoreP1+=1
if board[0][0] == board[1][1] == board[2][2] == 'o' or board[0][2] == board[1][1] == board[2][0] == 'o':
    scoreP2+=1

print("")
print("score P1 (x) : " + str(scoreP1))
print("score P2 (o) : " + str(scoreP2))

whoWin(scoreP1, scoreP2)     # memanggil fungsi untuk menentukan siapa pemenangnya
