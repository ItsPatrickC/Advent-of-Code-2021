
f=open("lines.txt", "r")
lines = f.readlines()
f.close

f=open("lines1.txt", "r")
lines1 = f.readlines()
f.close

f=open("lines2.txt", "r")
lines2 = f.readlines()
f.close

#diag = ['.','.','.','.','.','.','.','.','.','.']


diag = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]

for a in diag:
	print(a)



def readlines(line):
	'''
	reads through the input (both example and actual puzzle input)
	and puts the numbers in a list, 
	pos is a list with 4 empty strings, to become the x1,y1,x2,y2 list
	posit is the empty string that may be added to each loop
	p is the index

	the outer loop looks at the lines, and sets up those variables,
		the inner loop, looks at every index of that/those line/lines
		and if they're numeric, adds them to a string that will be added to the respective index of the pos list,
		if they're a comma or a dash, as appears in the inputs, the index is incremented by 1,
		so that the next numeric character will be added to the next index instead.

		tested with both example input (1 digit numbers) 
		and with actual puzzle input(generally 3 digit numbers) 
		and both work
	'''

	positions = []
	for a in range(0,len(line)):
		
		#print(line[a])
		pos = ["", "", "", ""]
		posit = ""
		p = 0

		for b in line[a]:

			if b in ["0","1","2","3","4","5","6","7","8","9"]:
				pos[p] += b

			if b == ",":
				p += 1

			if b == "-":
				p += 1

		#print(pos)

		positions.append(pos)
	return positions



#readlines(lines1)


def makeline(line):
	'''
	   x axis

	y 

	a
	x
	i
	s 

	or "in the xth column of the yth row'''

	x1 = int(line[1])
	y1 = int(line[0])
	x2 = int(line[3])
	y2 = int(line[2])

	diag[x1][y1] += 1
	diag[x2][y2] += 1


	for a in diag:
		print(a)

	

lines = readlines(lines)


for a in lines:
	print("---")
	print(a)
	makeline(a)
	

print("---final---")
for a in diag:
	print(a)