
with open('input10.txt') as f:
    answer = 0
    cycleNo = 0
    sigStr = 0
    val = 1
    sprPos = ""
    
    #sprPos = "........................................"
    #temp = list(sprPos)
    
    #for i in range(val-1, val+2):
    #    temp[i] = "#"
    #sprPos = "".join(temp)
    #print (sprPos)

    for line in f.readlines():
        cycleNo += 1

        if cycleNo%40 <= val + 2:
            sprPos += "#"
        else:
            sprPos += "."

        if (cycleNo % 40 == 0) and cycleNo < 250:
            sigStr += cycleNo * val
            print(sprPos)
            sprPos = ""
            

        if "addx" in line:
            cycleNo += 1

            if cycleNo%40 <= val + 2:
                sprPos += "#"
            else:
                sprPos += "."

            temp = int(line.split()[1])
            
            if (cycleNo % 40 == 0) and cycleNo < 250:
                sigStr += cycleNo * val
                print(sprPos)
                sprPos = ""
            val += temp
        #print(val)
    #print (sigStr)

    