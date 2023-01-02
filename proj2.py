with open('input2.txt') as f:
    tot = 0
    curr = 0
    for line in f.readlines():
        if ("A X" in line) or ("B Y" in line) or ("C Z" in line):
            tot += 3
            print("A")
        if ("A Y" in line) or ("B Z" in line) or ("C X" in line):
            tot += 6
            print("B")
        if "X" in line:
            tot += 1
            print("C")
        if "Y" in line:
            tot += 2
            print("D")
        if "Z" in line:
            tot += 3
            print("E")
        print(line)
        print(tot)
    print(tot)