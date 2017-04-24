def insertionSort(lst):
    for i in range(1, len(lst)):
        currentvalue = lst[i]
        pos = i

        while pos > 0 and lst[pos - 1] > currentvalue:
            lst[pos] = lst[pos - 1]
            pos = pos - 1

        lst[pos] = currentvalue


def binarySearch(lst, value):
    insertionSort(lst)
    middle = len(lst) // 2
    if (value == lst[middle]):
        return True
    else:
        if (value < lst[middle]):
            return binarySearch(lst[:middle], value)
        else:
            return binarySearch(lst[middle + 1:], value)


lst = [54, 26, 93, 17, 77, 31, 44, 55, 20]

found = binarySearch(lst, 93)
if found:
    print("Value found")
else:
    print("Value Not found")
