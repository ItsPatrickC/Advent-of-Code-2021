

numbersfile = open("bindata.txt", "r")
#numbersfile = open("bindata0.txt", "r")

numbers = list(numbersfile.readlines()) #make a list of each line in the file
numbers2 = numbers

numbersfile.close()

ograte = [0,0,0,0,0,0,0,0,0,0,0,0]
#ograte = [0,0,0,0,0]


#print(f"orginial numbers {numbers}")

for a in range(0,len(ograte)):

	print("-----------------------")
	#print(f"orginial numbers left: {numbers}")
	#print(f"loop {a} numbers2: {numbersy}")

	print(f"numbers left: {len(numbers)}")

	#if only one number is left, that is the rating
	

	count0 = 0
	count1 = 0

	for b in numbers: #find the most common value in each column
		#print(b[a])
		if b[a] == str(1):
			count1 += 1
		elif b[a] == str(0):
			count0 += 1

	#show what we're looking for
	if count0 == count1:
		lookfor = "1"
	elif max(count0,count1) == count0:
		lookfor = "0"
	elif max(count0,count1) == count1:
		lookfor = "1"
	#for each loop, show how many 1s and 0s
	print("index", a)
	print("0s:" ,count0)
	print("1s:", count1)
	print(f"looking for {lookfor}s in index {a}")

	#update ograte accordingly
	if count0 == count1:
		ograte[a] = 1
	elif count1 > count0:
		ograte[a] = 1
	elif count0 > count1:
		ograte[a] = 0

	#good list and bad list for each loop
	numbersn = []
	numbersy = []

	#loop through numbers by the index
	for c in numbers:
		#if it does, put in good list
		if int(c[a]) == ograte[a]:
			numbersy.append(c)
		else: #if the index doesn't match, put in bad list
			#print(f"{c} doesn't match this index")
			numbersn.append(c)
		
	#tell us what numbers should and shouldn't be kept
	print("numbers that need removing:", len(numbersn))
	print("numbers that should be kept:", len(numbersy))

	#make sure only the good numbers are in the next loop by becoming the good list
	numbers = numbersy

	if len(numbers) == 1:
		print("oxygen generator rating is", numbers[0])
		ograte = numbers[0]
		break
	

	#print("new numbers:", numbers)
print(f"the oxygen generator rating is .. {ograte}")


print("------------------------------------------------")


#now for the c02 rating

#c02rate = [0,0,0,0,0]
c02rate = [0,0,0,0,0,0,0,0,0,0,0,0]

for a in range(0,len(c02rate)):



	print("-----------------------")

	#if there's only one left, that is the rating we're looking for
	print(f"numbers left: {len(numbers2)}")

	#if only one number is left, that is the rating

	count0 = 0
	count1 = 0

	for b in numbers2: #find the most common value in each column
		#print(b[a])
		if b[a] == str(1):
			count1 += 1
		elif b[a] == str(0):
			count0 += 1

	#show what we're looking for
	if count0 == count1:
		lookfor = "0"
	elif min(count0,count1) == count0:
		lookfor = "0"
	elif min(count0,count1) == count1:
		lookfor = "1"
	#for each loop, show how many 1s and 0s
	print("index", a)
	print("0s:" ,count0)
	print("1s:", count1)
	print(f"looking for {lookfor}s")

	#update ograte accordingly
	if count0 == count1:
		c02rate[a] = 0
	elif count1 > count0:
		c02rate[a] = 0
	elif count0 > count1:
		c02rate[a] = 1

	#good list and bad list for each loop
	numbersn = []
	numbersy = []

	#loop through numbers by the index
	for c in numbers2:
		if int(c[a]) != c02rate[a]: #if the index doesn't maych, put in bad list
			#print(f"{c} doesn't match this index")
			numbersn.append(c)
		else: #if it does, put in good list
			numbersy.append(c)



	#tell us what numbers should and shouldn't be kept
	print("numbers that should be removed:", len(numbersn))
	print("numbers that  should  be  kept:", len(numbersy))

	
	#make sure only the good numbers are in the next loop by becoming the good list

	numbers2 = numbersy

	if len(numbers2) == 1:
		print("c02 rate is", numbers2[0])
		c02rate = numbers2[0]
		break
	
	#print("new numbers:", numbers)

print("----------------------------------------------------------------------------------")

print(f"the oxygen generator rating is .. {ograte}")
print("the c02rating is.. ",c02rate)

