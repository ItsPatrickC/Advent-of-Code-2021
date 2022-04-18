


#numbersfile = open("bindata.txt", "r")
numbersfile = open("bindata0.txt", "r")

numbers = list(numbersfile.readlines()) #make a list of each line in the file
numbers2 = numbers.copy()

numbersfile.close()

#ograte = [0,0,0,0,0,0,0,0,0,0,0,0]
ograte = [0,0,0,0,0]


for a in range(0,len(ograte)):

	print(f"------------------ loop {a} ------------------")


	count0,count1 = 0,0

	print(f"on loop {a}, numbers has a len() of {len(numbers)}")

	for number in numbers:
		if int(number[a]) == 1:
			count1 += 1
		else:
			count0 += 1

	if count1 >= count0:
		lookfor = "1"
	else:
		lookfor = "0"

	ograte[a] = int(lookfor)

	print(f"we are looking for {lookfor} in ograte[{a}]")

	newnumbers = []
	for number in numbers:
		if number[a] == lookfor:
			newnumbers.append(number)

	#print(newnumbers)
	numbers = newnumbers
	print()



print(ograte)





