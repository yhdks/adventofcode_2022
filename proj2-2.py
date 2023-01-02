with open('input2.txt') as f:
    tot = 0
    for line in f.readlines():
        if ("A Y" in line) or ("B X" in line) or ("C Z" in line):
            tot += 1
            print("Rock")
        if ("A Z" in line) or ("B Y" in line) or ("C X" in line):
            tot += 2
            print("Paper")
        if ("A X" in line) or ("B Z" in line) or ("C Y" in line):
            tot += 3
            print("Scissors")
        
        if "X" in line:
            tot += 0
            print("lose")
        if "Y" in line:
            tot += 3
            print("Draw")
        if "Z" in line:
            tot += 6
            print("win")
        print(line)
        print(tot)
    print(tot)