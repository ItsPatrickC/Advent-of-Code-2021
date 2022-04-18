
from boardclass import Board

#open file and use readlines to get data
f = open("datajustboards.txt", "r")
lines = f.readlines()
f.close()

#long lsit of numbers to be called out
numbers = [79,9,13,43,53,51,40,47,56,27,0,14,33,60,61,36,72,48,83,42,10,86,41,75,16,80,15,93,95,45,68,96,84,11,85,63,18,31,35,74,71,91,39,88,55,6,21,12,58,29,69,37,44,98,89,78,17,64,59,76,54,30,65,82,28,50,32,77,66,24,1,70,92,23,8,49,38,73,94,26,22,34,97,25,87,19,57,7,2,3,46,67,90,62,20,5,52,99,81,4]

print(len(lines))

#need an automated method of populating the boards from the data file
#use these to address the indices in lines for each board
indices = [0,1,2,3,4]

#populate a list of strings to use as variable names via a for loop and formatting
boardnames = []
for a in range(100):
	boardnames.append(f"board{a}")

#a list to store the boards
boards = []
#print(boardnames)

'''via the exec function and string formatting, 
initiate a board for each name in boardnames list, populating the boards from lines list
and after each one, increment every index of indices by 6 so that the next 
one starts on the right line, then append them to boards

very janky but it works correctly'''
for a in range(len(boardnames)):
	exec(f"board{a} = Board(lines[indices[0]],lines[indices[1]],lines[indices[2]],lines[indices[3]],lines[indices[4]],f'board{a}')")
	indices[0] += 6
	indices[1] += 6
	indices[2] += 6
	indices[3] += 6
	indices[4] += 6
	exec(f"boards.append(board{a})")

#just testing to see if the above worked
print(board0)
print(board99)

#print(type(board1.row0[0]))

#function to check if a given number is present on a board, then if so mark it as such
def draw(num, board):
	board.mark(num)

#function to check and return True if a vertical or horizontal line is all marked
def bingocheck(board):
	for a in board.whole:
		
		#print("-----")
		#print(a)
		if a[0][-1] == "a" and a[1][-1] == "a" and a[2][-1] == "a" and a[3][-1] == "a" and a[4][-1] == "a":
			#print(a)
			print(f"Horizontal BINGO in {board.name}")
			#print(board)
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


'''main loop

loop through numbers on a, 
	in nested loop, go through the boards:
		draw a, automatically marking it on any board it appears on
		if bingo is true on anyboard, break the loop and set the over bool to True
		will print out that a winner has been found and stop'''
for a in numbers:
	print(f"Drawing number {a}!")
	over = False

	for b in boards:
		
		#print(b)
		draw(a,b)
		if bingocheck(b):
			#break
			over = True
			print(b)
			break
	
	if over:
		print("WE HAVE A WINNER")

		break
