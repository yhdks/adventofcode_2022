with open('input.txt') as f:
    maxx = 0
    curr = 0
    lst = []
    for line in f.readlines():
        if len(line.strip()) == 0:
            lst.append(curr)
            #if curr > maxx:
            #    maxx = curr
            curr = 0
        else:
            curr += int(line)
    lst.sort(reverse=True)
    maxx = lst[0] + lst[1] + lst[2]
    print(maxx)