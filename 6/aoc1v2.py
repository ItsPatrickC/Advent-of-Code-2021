fish = [1,1,1,3,3,2,1,1,1,1,1,4,4,1,4,1,4,1,1,4,1,1,1,3,3,2,3,1,2,1,1,1,1,1,1,1,3,4,1,1,4,3,1,2,3,1,1,1,5,2,1,1,1,1,2,1,2,5,2,2,1,1,1,3,1,1,1,4,1,1,1,1,1,3,3,2,1,1,3,1,4,1,2,1,5,1,4,2,1,1,5,1,1,1,1,4,3,1,3,2,1,4,1,1,2,1,4,4,5,1,3,1,1,1,1,2,1,4,4,1,1,1,3,1,5,1,1,1,1,1,3,2,5,1,5,4,1,4,1,3,5,1,2,5,4,3,3,2,4,1,5,1,1,2,4,1,1,1,1,2,4,1,2,5,1,4,1,4,2,5,4,1,1,2,2,4,1,5,1,4,3,3,2,3,1,2,3,1,4,1,1,1,3,5,1,1,1,3,5,1,1,4,1,4,4,1,3,1,1,1,2,3,3,2,5,1,2,1,1,2,2,1,3,4,1,3,5,1,3,4,3,5,1,1,5,1,3,3,2,1,5,1,1,3,1,1,3,1,2,1,3,2,5,1,3,1,1,3,5,1,1,1,1,2,1,2,4,4,4,2,2,3,1,5,1,2,1,3,3,3,4,1,1,5,1,3,2,4,1,5,5,1,4,4,1,4,4,1,1,2]
fd = {}

#populate the fd according to the puzzle input
for a in range(0,9):
    fd[a] = fish.count(a)

#print(fd)
print("----")

'''
for each day, the amount of fish on day 0 is stored in zval,
on each day, every fish moves down by one, 
when they're on zero, they move to 6, but they also have a child, which goes to 8 as a newborn,
when newborns reach day zero, they go to day 6 like their parents
'''
for a in range(0, 256):
	#loop through days

    # print(f"day {a}: {fd}")
    zval = fd[0]
    # print(zval)

    for b in range(0, len(fd)):
    	#everyday, if b is less than 8, then the fish at that index assume the value of the next index
        # print(f"{b} - {fd[b]}")

        if b < 8:
            fd[b] = fd[b + 1]

    #fd index 8 is filled with the newborns from fish on day 0, day 6 gets both day 7s fish and day 0s fish!
    fd[8] = zval
    fd[6] += zval


    # print(f"Total: {tot}")

#calculate total
print(f"Amounts")

tot = 0
for a in fd:
    print(f"{a} : {fd[a]}")
    tot += fd[a]

print(f"Total: {tot}")
