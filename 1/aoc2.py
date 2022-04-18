'''this is for the 2nd part of day 1,
I didn't end up using the file writing method, I just used
the list instead as its easier, but keeping the file
writing stuff in here for future reference anyway'''

depthdata = open("1 data.txt", "r")#read the file with the data
#print(depthdata.read())

depthsliststr = depthdata.readlines() #put the data in a list
depthslistint = [] # a blank list to store ints (the data is currently strings)

for a in depthsliststr: #loop thru str lists
	#depthslist[a] = int(depthslist[a])
	depthslistint.append(int(a)) #append an int version to the int list

#a function that returns the sum of 3 given numbers
def sum3(num1, num2, num3):
	result = int(num1 + num2 + num3)
	#print(result)
	return int(result)

sumdata = open('sumdata.txt', 'w') #create a file to store values
sumlist = []

for a in range(0,len(depthslistint)-2): #-2 because otherwise when it gets to the 3rd last index it causes an error
	b = sum3(depthslistint[a], depthslistint[a+1], depthslistint[a+2]) #create variable b every loop, which stores the sum3 result of every index and the next 2 indices
	sumdata.write(str(b)) #write it in the sumdata file
	sumdata.write('\n') #put a new line for readability

	sumlist.append(int(b)) #append to list of sums

sumdata.close() #close sumdata after
#print(sumlist)

answer = 0 #start at 0

for a in range(0,len(sumlist)): #loop thru the sums list
	if sumlist[a] > sumlist[a-1]: #if the value is higher/deeper than the previous one, increment answer
		answer += 1

print("the answer is", answer) #give answer (this one was correct!)