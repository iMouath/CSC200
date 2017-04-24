def changeString(string, pos, newChar):
    a = string[0:pos]
    b = string[pos + 1:]
    string = a + newChar + b
    return string


oldString = "Hello"
newString = changeString(oldString, 2, 'b')
print(oldString)
print(newString)
