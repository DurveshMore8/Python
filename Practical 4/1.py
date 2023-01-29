# Write a program that takes two lists and return True if they have at least one common member.

list1 = [3,4,5,6,7,1]
list2 = [12,43,32,10]
answer = False

for i in list1:
    for j in list2:
        if i == j:
            answer = True
            break

if answer:
    print(True)
else:
    print(False)