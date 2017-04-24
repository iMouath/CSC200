def decimalToBinary(num):
    # return the binary string version
    # of the decimal num
    # example 10 -> "1010"
    binString = "" # place holder for our computed binary
    while num > 0:
        rem = num % 2 # get reminder and assign it to variable rem
        binString = str(rem) + binString # add the reminder to the string, rem needs to be a string
        num = num // 2 # divide by 2 and loop back
    return binString

print(decimalToBinary(10))
