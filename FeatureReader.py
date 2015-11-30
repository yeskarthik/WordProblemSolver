def readAndConvertFeatures(qIndex):
    with open('data/'+str(qIndex)+'.txt') as f:
        result = []
        equation = ''
        for i, line in enumerate(f):
            #print i, line
            if i==1 or (i-1)%3 == 0:
                #print line 
                equation = line[line.index('>')+2:len(line)-2]

            if i==4 or ((i-3)%3 == 0 and i != 0):                
                
                if line[0] == '1' and line[1] == ' ':                    
                    result.append((1, line, equation))
                elif line[0] == '-' and line[1] == '1' and line[2] == ' ':
                    result.append((-1, line, equation))
                

    final = []
    for res in result:
        arr = []
        for i in range(0, 219347):
            arr.append(0)

        look = res[1][3:].split(' ')
        #print look 
        for i, k in enumerate(look):
            #print i, k
            if (i+1) % 3 == 0:
                #print k
                arr[int(look[i-2])] = k

        final.append((res[0], arr, res[2]))
    return final



#print readAndConvertFeatures('1035')


