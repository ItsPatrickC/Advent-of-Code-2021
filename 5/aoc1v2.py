'''
new idea:

nevert mind the visualisation, as the actual input data is way bigger than the example data
instead, just take the coordinates, and put those numbers and any between them in a dictionary,
when the next line is read, do the same

so, it'll still be "x1,y1,x2,y2" but instead it should take the 1st and second coordinate, and all the ones in between,
check if they're in the dict, if they are, just increment them in the dict, if not, add them with a value of 0

the x axis is the column
the y axis is the row
'''

positions = []
posdict = {}
diagslist = []


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

def betweens(coord):
	'''
	this function takes in a coord (a list of 4 numbers)
	x1,x2,y1,y2 become the appropriate elements of the given coord
	then it adds the two xs and ys to a list, and does the same for any coordinates between them
	as long as either the two xs or two ys are equal or the difference between x1 & x2 is the same as the difference between y1 & y2
	
	making it do the diagonal inbetweens is more difficult than the horizontal or vertical ones,
	it's done by assessing x1 (or ax1) against x2 then incrementing or decrementing appropriately,
	when it's done the x coordinate, it appends that to diagos,
	then when it's done the y coordinate, it appends that too. 
	it does this because the different x1 & y1 might need to go different ways to become
	the same as x2 & y2. 
	When they're equal to x2 & y2, they're appended again to make sure both ends of the 
	line appear in the diagonals list

	the two between lists at the bottom are commented out to save output when used with actual puzzle input
	'''


	xbetweens = []
	ybetweens = []
	diagbetweens = []
	x1 = int(coord[0])
	x2 = int(coord[2])
	y1 = int(coord[1])
	y2 = int(coord[3])

	if abs(x1-x2) == abs(y1-y2):
		#print(coord,"diagonal match!")
		#needs to append like the others but it's tricky because diagonal

		ax1, ax2, ay1, ay2 = x1, x2, y1, y2
		diagslist.append([x1,y1])


		while ax1 != ax2 and ay1 != ay2:

			positions.append(f"{ax1}, {ay1}")
			diagbetweens.append(f"{ax1}, {ay1}")

			diagos = []

			if ax1 < ax2:
				ax1 += 1
				#print(ax1)

			if ax1 > ax2:
				ax1 -= 1
				#print(ax1)

			diagos.append(ax1)

			if ay1 < ay2:
				ay1 += 1
				#print(ay1)

			if ay1 > ay2:
				ay1 -= 1
				#print(ay1)

			diagos.append(ay1)

			#print(diagos)
			diagslist.append(diagos)

			if ax1 == ax2 and ay1 == ay2:
				positions.append(f"{ax1}, {ay1}")
				diagbetweens.append(f"{ax1}, {ay1}")



	if x1 == x2:
		#print(coord, "X axis matching")
		
		if y1 < y2:
			a = y1

			while a <= y2:
				ybetweens.append(f"{x1}, {a}")
				positions.append(f"{x1}, {a}")
				a += 1
				#print(a)

		elif y1 > y2:
			a = y1

			while a >= y2:
				ybetweens.append(f"{x1}, {a}")
				positions.append(f"{x1}, {a}")
				a -= 1

	if y1 == y2:
		#print(coord, "Y axis matching")

		if x1 < x2:
			a = x1

			while a <= x2:
				xbetweens.append(f"{a}, {y1}")
				positions.append(f"{a}, {y1}")
				a += 1
				#print(a)

		elif x1 > x2:
			a = x1

			while a >= x2:
				xbetweens.append(f"{a}, {y1}")
				positions.append(f"{a}, {y1}")
				a -= 1

	'''if len(xbetweens):
		print(f"X betweens: {xbetweens}")
		print("----------")


	if len(ybetweens):
		print(f"Y betweens: {ybetweens}")
		print("----------")

	if len(diagbetweens):
		print(f"Diagonal betweens: {diagbetweens}")
		print("----------")'''


#get the input
f=open("lines.txt", "r")
lines = f.readlines()
f.close

#lines = readlines(lines)

f = open("input.txt", "r")
lines = f.readlines()
f.close

#refine the input using readlines so it's suitable for the betweens function
lines = readlines(lines)


#for a in lines:
	#print(a)

#print(lines)
print("This program takes a long time to execute when using actual puzzle input")
print("---")

#loop thru lines, pass all of them to the betweens function
for a in lines:
	betweens(a)


'''
loop thru positions now that it's populated
for each one, it will either create or overwrite that value with
however many times the key appears in the list
'''

for a in positions:
	posdict[a] = str(positions.count(a))

'''
for a in posdict:
	print(f"[{a}], {posdict[a]}")'''

#count how many keys in position dictionary have a value of more than 1 and then display it
overlaps = 0
for a in posdict:
	#print(f"[{a}] : {posdict[a]}")
	if int(posdict[a]) > 1:
		overlaps += 1

print(f"{overlaps} overlaps in this input")




