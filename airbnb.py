def lookSeeOne(n):
    count = 0
    seq = []
    
    nList = map(str, str(n))
    for i in range(len(nList)):
        count += 1
        if i+1 == len(nList) or (not nList[i+1] == nList[i]):
            print i
            seq.append(str(count))
            seq.append(nList[i])
            count = 0
    print seq
    return int(''.join(seq))