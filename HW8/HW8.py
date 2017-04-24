def stringToList(s):
    # returns the list version of the string s
    # "lol" -> ['l','o','l']
    lst = []
    for i in s:
        lst.append(i)
    return lst

print(stringToList("lol"))
