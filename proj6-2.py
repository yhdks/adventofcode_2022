with open('input6.txt') as f:
    answer = 0
    count = 0
    currentList = []
    for line in f.readlines():
        for word in line:
            if count >= 14:
                currentList.pop(count%14)
            
            currentList.insert(count%14, word)
            count += 1

            if len(set(currentList)) == 14:
                answer = count
                break
    
    print(answer)