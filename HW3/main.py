_9 = 0
_13 = 0
_27 = 0
_81 = 0

for i in range(1, 1000001):
    if (i % 9 == 0):
        _9 += 1
    elif (i % 13 == 0):
        _13 += 1
    elif (i % 27 == 0):
        _27 += 1
    elif (i % 81 == 0):
        _81 += 1

print("Numbers that are divisible by 09:", _9)
print("Numbers that are divisible by 13:", _13)
print("Numbers that are divisible by 27:", _27)
print("Numbers that are divisible by 81:", _81)
print("Total Numbers: ", _9 + _13 + _27 + _81)

count = 0
for i in range(1, 1000001):
    if(i % 9 == 0 or i % 13 == 0 or i % 27 == 0 or i % 81 == 0):
        count += 1
print(count)
print((_9+_13+_27+_81)-count)
