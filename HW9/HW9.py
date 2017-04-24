def removeConsonants(lst):
    # take a list as a parameter and removes
    # all consonants from that list returning
    # the modified list
    # ['h','e','l','l','o'] -> ['e','o']
    answer = []
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    for i in lst:
        if i not in consonants:
            answer.append(i)
    return answer

lst = ['h', 'e', 'l', 'l', 'o']
print(removeConsonants(lst))
