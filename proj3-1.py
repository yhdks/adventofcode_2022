
with open('input3.txt') as f:
    tot = 0
    alphab = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for line in f.readlines():
        ind = len(line) - 1
        ind = int(ind / 2)
        curr = set.intersection(set(line[:ind]), set(line[ind:]))
        tot += int(alphab.find(list(curr)[0])) + 1
    print(tot)