directions = open("directions.txt", 'r') #open directions
dirlist = list(directions.readlines()) #make a list from the file
directions.close() #close file

#initiate vars for horizontal position and depth at 0
hp = 0
depth = 0

#loop through the list, take the last index of each line and apply it to the vars
#done by looking for the keyword in each index
for a in dirlist:
	if 'forward' in a:
		#print(a)
		#print(a[8])
		hp += int(a[8])

	if 'down' in a:
		#print(a)
		#print(a[5])
		depth += int(a[5])

	if 'up' in a:
		#print(a)
		#(a[3])
		depth -= int(a[3])

answer = hp * depth #multiply them

print("The answer is", answer) #give answer