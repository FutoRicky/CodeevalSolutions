import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    duplicateList=[]
    uniqueList=[]
    listPrint=""
    for i in test.strip().split(","):
        duplicateList.append(i)
    for i in range(0,len(duplicateList)):
        if duplicateList[i] not in uniqueList:
            uniqueList.append(duplicateList[i])
    for i in range(0,len(uniqueList)):
        if i == len(uniqueList)-1:
            listPrint += str(uniqueList[i])
        else:
            listPrint += str(uniqueList[i]) + ","
    print listPrint

test_cases.close()
