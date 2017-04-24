def octalToDecimal(octString):
    #returns the decimal equivalent
    #of octString as an int
    place = 1
    sum = 0
    for i in range(len(octString)-1, -1, -1):
        sum = sum + (place * int(octString[i]))
        place = place * 8

    return sum

def hexToDecimal(hexString):
    #returns the decimal equivalent
    #of hexString as an int
    answer = 0 # initialize answer
    hexMap = "0123456789ABCDEF" # HexMap
    hexString = hexString.upper() # error proofing, to make sure received hex in uppercase
    for i in range(len(hexString)):
        c = hexString[i] # get the Char
        d = str.find(hexMap,c) # get location of Char
        answer = 16 * answer + d # Math magic to get the Char hex into Decimal
    return answer # return answer

print(hexToDecimal("d1ce"))
print(str(int("BAD", 16))) # for reference ONLY

