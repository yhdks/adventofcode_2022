with open('input4.txt') as f:
    tot = 0
    lst = []
    contained = False
    for line in f.readlines():
        contained = False
        line = line.replace('-',' ')
        line = line.replace(',',' ')
        lst = line.split()

        print(lst)
        # if the first is contained by the second
        if ((int(lst[0]) >= int(lst[2])) and (int(lst[1]) <= int(lst[3]))):
            contained = True
            print("C")
        if ((int(lst[2]) >= int(lst[0])) and (int(lst[3]) <= int(lst[1]))):
            contained = True
            print("D")
        if ((int(lst[0]) <= int(lst[2])) and (int(lst[1]) <= int(lst[3])) and (int(lst[1]) >= int(lst[2]))):
            contained = True
            print("A")
        if ((int(lst[2]) <= int(lst[0])) and (int(lst[3]) <= int(lst[1])) and (int(lst[3]) >= int(lst[0]))):
            contained = True
            print("B")

        if (contained):
            tot += 1
    print (tot)
