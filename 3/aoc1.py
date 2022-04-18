from bin2dec import bin2dec,binreverse #binary conversion functions I made ages ago
numbersfile = open("bindata.txt", "r")

numbers = list(numbersfile.readlines()) #make a list of each line in the file
numbersfile.close()



grate = [0,0,0,0,0,0,0,0,0,0,0,0] #list for the gamma rate
grates = "" #string version
erate = "" #epsilon string

for a in range(0,12): #go thu indices first

	#every loop, count the 1s and 0s in each column
	count0 = 0
	count1 = 0


	for b in range(0,len(numbers)): #go through each index of numbers list looking to see if that index is 1 or 0
		
		print("index", a, "of number", b, "is", numbers[b][a])

		#if that digit is 1, add to count1, else add to count0
		if numbers[b][a] == str(1):
			count1 += 1
		else:
			count0 += 1

	print("0s:", count0)
	print("1s:", count1)

	if count1 > count0: #if more 1s in these indices than 0s, change the value to 1, otherwise do nothing
		grate[a] = 1
	else:
		pass
	grates += str(grate[a])

	print("grate value",a, "=", grate[a])
	print(grates)

gratei = bin2dec(grates) #use old function to get decimal conversion
erate = binreverse(grates) #reverse grates (flip 1s to 0s and 0s to 1s)

crate = gratei * erate #consumption rate is grate * erate
print(f"the consumption rate is {crate}") #give answer