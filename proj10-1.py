with open('input10.txt') as f:
    answer = 0
    cycleNo = 0
    sigStr = 0
    val = 1

    for line in f.readlines():
        if "noop" in line:
            cycleNo += 1
        elif "addx" in line:
            cycleNo += 1

        if (cycleNo % 40 == 20) and cycleNo < 230:
            sigStr += cycleNo * val

        if "addx" in line:
            cycleNo += 1
            temp = int(line.split()[1])
            
            if (cycleNo % 40 == 20) and cycleNo < 230:
                sigStr += cycleNo * val
            val += temp
        
    print (sigStr)

    