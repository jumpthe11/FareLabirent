# Geri izleme algoritması ile çalışıyor
# Rastgele Bir labirent oluşturur ve en kısa yolu algoritma ile bulur.
import random
import PySimpleGUI as sg
import numpy as np
# Labirent büyüklüğü N*N büyüklüğünde kare
N = 10
cevap = [[0]*N for i in range(N)]
# Cevabı yazdırması için for döngüsü
"""""
def printSolution( sol ):
	
	for i in sol:
		for j in i:
			print(str(j) + " ", end ="")
		print("")
"""
#x ve y'nin geçerli olup olmadığını kontrol ediyor
def isSafe( maze, x, y ):
	
	if x >= 0 and x < N and y >= 0 and y < N and maze[x][y] == 1:
		return True
	
	return False
def solveMaze( maze ):
	
	# N*N boyutunda 2D array dizisi oluşturuyor
	sol = [ [ 0 for j in range(N) ] for i in range(N) ]
	
	if solveMazeUtil(maze, 0, 0, sol) == False:
		print("Çıkmaz Sokak. Yeni labirent Oluşturuluyor...")
		return False
	
	#printSolution(sol) # En kısa çıkış yolunu yazdırır (üstteki fonksiyonu açmayı unutma)
	return sol
	
# Özyinelemeli algoritma
def solveMazeUtil(maze, x, y, sol):
	# if (x, y is goal) return True
	if x == N - 1 and y == N - 1:
		sol[x][y] = 1
		return True
		
	# maze[x][y] Labirenti var mı kontrol et
	if isSafe(maze, x, y) == True:
		# x ve y'yi çıkış yolunu işaretle
		sol[x][y] = 1
		
		# x yönünde ilerle
		if solveMazeUtil(maze, x + 1, y, sol) == True:
			return True
			
		# x yönü çıkış vermediyse
		# aşağı in ve y yönünden git
		if solveMazeUtil(maze, x, y + 1, sol) == True:
			return True
		
		# Hiçbiri çalışmaz ise
		# çözüm yolunun parçası x ve y işaretini kaldır
		sol[x][y] = 0
		return False
	#Labirenti oluşturur. 0'lar duvar, 1'ler yol
def mazeolustur(maze):
	maze[0][0]=1
	maze[N-1][N-1]=1
	for sutun in range(N):
		for satir in range(N):
			rng = np.random.default_rng()
			maze[sutun][satir]=rng.integers(low=0, high=2)
	return maze
if __name__ == "__main__":
	maze = [[0]*N for i in range(N)]
	maze=mazeolustur(maze)
	maze[0][0]=1
	maze[N-1][N-1]=1
	#Labirent'in çıkış yolu olana kadar yeni labirent üret
	while solveMaze(maze) == False:
		maze=mazeolustur(maze)
		#ilk ve son köşeleri yol olarak işaretlemek lazım ki çözüme ulaşılsın
		maze[0][0]=1
		maze[N-1][N-1]=1
cevap = solveMaze(maze)
print(' ')
	# Labirentin normal halini yazdır
def Goster():
    sg.theme('Dark Blue 3')
    MAX_ROWS = MAX_COL = N
    layout =   [[sg.Text('Labirent', font='Default 25')]]
    # Matrix board olarak tutuyor
    board = []
    for row in range(MAX_ROWS):
        layout_row = []
        for col in range(MAX_COL):
            layout_row.append(sg.Button(maze[row][col], size=(4, 2), pad=(0,0), border_width=0, key=(row,col)))

        board.append(layout_row)
    layout += board
    layout +=  [[sg.Button('Bul',key='Ara', button_color=('white', 'Blue'))]]
    window = sg.Window('Fare Labirenti', layout)
    while True:   
        event, values = window.read()
        print(event, values)
        if event in (sg.WIN_CLOSED, 'Ara'):
            break
	#Labirentin çıkış yolunu göster
def CozumGoster():
    sg.theme('Dark Blue 3')
    MAX_ROWS = MAX_COL = N
    layout =   [[sg.Text('Labirent', font='Default 25')]]
    board = []
    for row in range(MAX_ROWS):
        layout_row = []
        for col in range(MAX_COL):
            layout_row.append(sg.Button(maze[row][col], size=(4, 2), pad=(0,0), border_width=0, key=(row,col)))
            if cevap[row][col] == 1:
                layout_row.pop(col)
                layout_row.insert(col,sg.Button(1,button_color='red', size=(4, 2), pad=(0,0), border_width=0, key=(row,col)))
        board.append(layout_row)
    layout += board
    layout +=  [[sg.Button('Pencereyi Kapat', button_color=('white', 'red'))]]
    window = sg.Window('Fare Labirenti', layout)
    while True:         
        event, values = window.read()
        print(event, values)
        if event in (sg.WIN_CLOSED, 'Pencereyi Kapat'):
            break
    window.close()
Goster()
CozumGoster()
