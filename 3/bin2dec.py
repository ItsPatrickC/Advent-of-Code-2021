def bin2dec(num):
    isbin = True
    bins = [1, 0] #list for validating whether given number is binary
    numlst = list(str(num)) #turn given number into iterable
    decnum = 0
    
    #for loop to convert numlst to ints
    for a in range(0, len(numlst)):
        numlst[a] = int(numlst[a])
    
    #if number isn't binary
    for a in range(0, len(numlst)):
        if numlst[a] not in bins:
            isbin = False
            return f"{num} is not a binary number"
    
    #if number is binary
    for a in range(0, len(numlst)):
        #poww var becomes the appropriate exponent on each loop
        poww = len(numlst)-a-1 #done according to the method in the docstring
        
        #if the current index of numlst is a 1, then pow is used to add to the decimal representation of decnum
        if numlst[a] == 1:
            decnum += 1 * (2**poww)
        
        #print(a, ' ', poww)
    
    print(f"{num} is {decnum}, bin2dec")
    return decnum

def binreverse(num):
    binno = ""
    isbin = True
    bins = [1, 0] #list for validating whether given number is binary
    numlst = list(str(num)) #turn given number into iterable
    decnum = 0
    
    #for loop to convert numlst to ints
    for a in range(0, len(numlst)):
        numlst[a] = int(numlst[a])
    
    #if number isn't binary
    for a in range(0, len(numlst)):
        if numlst[a] not in bins:
            isbin = False
            return f"{num} is not a binary number"

    #reverse the number
    for a in range(0, len(numlst)):

        if numlst[a] == 1:
            numlst[a] = 0
        elif numlst[a] == 0:
            numlst[a] = 1

    #if number is binary
    for a in range(0, len(numlst)):
        #poww var becomes the appropriate exponent on each loop
        poww = len(numlst)-a-1 #done according to the method in the docstring
        
        #if the current index of numlst is a 1, then pow is used to add to the decimal representation of decnum
        if numlst[a] == 1:
            decnum += 1 * (2**poww)
        
        binno += str(numlst[a])



    
    print(f"{binno} is {decnum} binreverse")
    return decnum