'''how to get ratings:
go through the list of numbers, considering only the first bit of them
keep only numbers which fit the criteria, discard those that don;t
if only one number, stop, that is the rating you're looking for
otherwise, repeat process, considering the next bit to the right

To find oxygen generator rating, 
determine the most common value (0 or 1) 
in the current bit position, 
and keep only numbers with that bit in that position. 
If 0 and 1 are equally common, 
keep values with a 1 in the position being considered.


To find CO2 scrubber rating, 
determine the least common value (0 or 1) 
in the current bit position, 
and keep only numbers with that bit in that position. 
If 0 and 1 are equally common, 
keep values with a 0 in the position being considered.
'''

from bin2dec import bin2dec,binreverse #binary conversion functions I made ages ago
numbersfile = open("bindata0.txt", "r")

numbers = list(numbersfile.readlines()) #make a list of each line in the file
numbers2 = []
#print(numbers2, "hello")
numbersfile.close()

ograte = [0,0,0,0,0]
csrate = 0

print(f"orginial numbers {numbers}")
#orate
for a in range(0,len(ograte)): #loop through the length of ograte

	#print(a, numbers)

	count0 = 0
	count1 = 0

	for b in numbers: #find the most common value in each column
		print(b[a])
		if b[a] == str(1):
			count1 += 1
		elif b[a] == str(0):
			count0 += 1

	#show it
	print("index", a)
	print("0s:" ,count0)
	print("1s:", count1)

	#update ograte accordingly
	if count0 == count1:
		ograte[a] = 1

	elif count1 > count0:
		ograte[a] = 1

	elif count0 > count1:
		ograte[a] = 0


	#go through numbers again and 
	#if indexes match then add good numbers to numbers2


	for c in range(0,len(numbers)): #loops through each number looking at that index, points out which should be removed
		#print(a,"a")
		#print(c,"c")
		
		if int(numbers[c][a]) == ograte[a]:
			if numbers[c] not in numbers2:
				#print(f"keeping {numbers[c]} in numbers2")
				numbers2.append(numbers[c])
			else:
				#print("number already in numbers2")
				pass
		
		elif int(numbers[c][a]) != ograte[a]:
			#print(f"if ograte index {a} is {ograte[a]} then {numbers[c]} should be removed")
			#print(f"removing {numbers[c]} from numbers")
			if numbers[c] in numbers2:
				numbers2.remove(numbers[c])
			else:
				pass

		print(numbers2, "in c loop")
	#numbers = numbers2
		

		



	print(f"numbers: {numbers}")
	print(f"new ones{numbers2}")
	print("-----")
	


print(numbers2)
print(len(numbers2))
print("ograte", ograte)