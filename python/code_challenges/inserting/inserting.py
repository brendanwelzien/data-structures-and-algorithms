def inserting_list(theList):
    for a in range(1, len(theList)):
        pos = theList[a]
        b = a-1

        while pos < theList[b] and b >= 0:
            theList[b] = theList[b + 1]
            b = b - 1
        pos = theList[b + 1]

theList = [5, 10, 6, 2, 4]

print(inserting_list(theList))
