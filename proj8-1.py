with open('input8.txt') as f:
    answer = 0
    count = 0
    
    numRow = 0
    numCol = 0

    currentList = []
    for line in f.readlines():
        currentList.append(list(line))
        numRow += 1

    numCol = len(currentList[0]) - 1

    for i in range(numRow):
        for j in range(numCol):
            currentList[i]
    