people = []


def addPerson(fname, lname, age):
    person = {}
    person["fname"] = fname
    person["lname"] = lname
    person["age"] = age
    people.append(person)


def addPersonFromUser():
    fname = input("Please Enter a First Name:")
    lname = input("Please Enter a Last Name:")
    age = input("Please Enter an age:")
    addPerson(fname, lname, int(age))


def findPerson(age):
    for person in people:
        if (person["age"] == age):
            return person
    return -1


def insertionSort():
    for currStartPos in range(1, len(people)):
        theFollower = currStartPos
        while (theFollower > 0 and people[theFollower]["age"] < people[theFollower - 1]["age"]):
            swapHelper = people[theFollower]
            people[theFollower] = people[theFollower - 1]
            people[theFollower - 1] = swapHelper
            theFollower = theFollower - 1


def findPersonBinarySearch(age):
    # should return a person who age is equivalent
    # to age or a -1 if it was not found
    begin = 0
    end = len(people) - 1
    while (begin <= end):
        middle = (end + begin) // 2
        if (people[middle]["age"] == age):
            return people[middle]
        else:
            # which half of the list is the val
            # potentially in?
            if (age < people[middle]["age"]):
                end = middle - 1
            else:
                begin = middle + 1
    return -1

addPerson("Mike", "Litman", 23)
addPerson("Dave", "Litman", 21)
addPerson("Van", "Nguyen", 25)
addPerson("Clark", "Smith", 34)
addPerson("Steve", "Jones", 18)
addPerson("Lucy", "Wilson", 29)
# print(people)
insertionSort()
# print(people)
print(findPersonBinarySearch(18))

