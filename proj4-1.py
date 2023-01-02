with open('input4.txt') as f:
    tot = 0
    lst = []
    fullyContained = False
    for line in f.readlines():
        fullyContained = False
        line = line.replace('-',' ')
        line = line.replace(',',' ')
        lst = line.split()

        # if the first is fully contained by the second
        if ((int(lst[0]) >= int(lst[2])) and (int(lst[1]) <= int(lst[3]))):
            fullyContained = True
        elif ((int(lst[2]) >= int(lst[0])) and (int(lst[3]) <= int(lst[1]))):
            fullyContained = True

        if (fullyContained):
            tot += 1
    print (tot)


