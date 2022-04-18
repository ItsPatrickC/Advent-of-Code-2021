depthdata = open("1 data.txt", "r")#read the file with the data
#print(depthdata.read())

depthsliststr = depthdata.readlines() #put the data in a list
depthslistint = [] # a blank list to store ints (the data is currently strings)

for a in depthsliststr: #loop thru str lists
	#depthslist[a] = int(depthslist[a])
	depthslistint.append(int(a)) #append an int version to the int list
	

#print(depthslistint)
answer = 0 #start at 0

for a in range(0,len(depthslistint)): #loop thru the ints list
	if depthslistint[a] > depthslistint[a-1]: #if the value is higher/deeper than the previous one, increment answer
		answer += 1

print("the answer is", answer) #give answer (this one was correct!)
