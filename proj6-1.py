with open('input6.txt') as f:
    answer = 0
    count = 0
    currentList = []
    for line in f.readlines():
        for word in line:
            if count >= 4:
                currentList.pop(count%4)
            
            currentList.insert(count%4, word)
            count += 1

            if len(set(currentList)) == 4:
                answer = count
                break
    
    print(answer)