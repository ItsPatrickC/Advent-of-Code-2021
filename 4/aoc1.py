'''numbers = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]

card0 = [ [22,13,17,11,0],[8,2,23,4,24],[21,9,14,16,7],[6,10,3,18,5],[1,12,20,15,19] ]
card1 = [[],[],[],[],[]]
card2 = [[],[],[],[],[]]

'''
from boardclass import Board

f = open("exjustboards.txt", "r")
lines = f.readlines()
f.close()

numbers = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]

print(len(lines))
#board0 = Board(lines[0],lines[1],lines[2],lines[3],lines[4], "board 0")
#board1 = Board(lines[6],lines[7],lines[8],lines[9],lines[10], "board 1")
#board2 = Board(lines[12],lines[13],lines[14],lines[15],lines[16], "board 2")


#need an automated method of populating the boards from the data file
indices = [0,1,2,3,4]
name = 'board'
boardnames = []

for a in range(3):
	boardnames.append(f"board{a}")

boards = []
print(boardnames)

for a in range(len(boardnames)):
	exec(f"board{a} = Board(lines[indices[0]],lines[indices[1]],lines[indices[2]],lines[indices[3]],lines[indices[4]],f'board{a}')")
	indices[0] += 6
	indices[1] += 6
	indices[2] += 6
	indices[3] += 6
	indices[4] += 6





print(board0)
print(board1)
print(board2)
print(type(board1.row0[0]))

def draw(num, board):
	board.mark(num)

def bingocheck(board):
	loop = 0
	for a in board.whole:
		
		#print("-----")
		#print(a)
		if a[0][-1] == "a" and a[1][-1] == "a" and a[2][-1] == "a" and a[3][-1] == "a" and a[4][-1] == "a":
			#print(a)
			print(f"Horizontal BINGO in {board.name}")
			print(board)
			return True


	for a in range(0,4):
		points = 0
		for b in board.whole:
			#print(b[a])
			if b[a][-1] == "a":
				points += 1
		
		#print("-----")
		if points == 5:
			print(board)
			print(f"Vertical BINGO in {board.name}")
			return True

for a in numbers:
	print(f"Drawing number {a}!")
	
	draw(a,board0)
	if bingocheck(board0):
		break
	
	draw(a,board1)
	if bingocheck(board1):
		break

	draw(a,board2)
	if bingocheck(board2):
		break


#bingocheck(board0)




