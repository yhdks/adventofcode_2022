with open('input3.txt') as f:
    tot = 0
    alphab = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    count = 0
    line1, line2, line3 = "", "", ""
    for line in f.readlines():
        if (count == 0):
            line1 = line
            count += 1
            print("count==0")
        elif (count == 1):
            line2 = line
            count += 1
            print("count==1")
        else:
            count = 0
            line3 = line
            #curr = set.intersection(set(line1), set(line2), set(line3))
            curr = set(line1).intersection(set(line2), set(line3))
            curr.remove('\n')
            tot += int(alphab.find(list(curr)[0])) + 1
            print((curr))
            print(tot)
    print(tot)