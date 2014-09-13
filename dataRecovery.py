import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    saver=[]
    text=""
    textList=[]
    positionList=[]
    num=0
    exists=int()
    counter=0
    for l in test.strip().split(";"):
        saver.append(l)
    for i in saver[0].split(" "):
        textList.append(i)
    for j in saver[1].split(" "):
        positionList.append(j)

    for i in range(0,len(positionList)):
        positionList[i]=int(positionList[i])

    accomodator=[None]*len(textList)

    for n in range(1,len(textList)):
        if n not in positionList:
            accomodator[n]=textList[len(textList)-1]
            exists=n       

    for item in positionList:
        accomodator[item-1]=textList[counter]
        counter+=1
        if counter>item:
            accomodator[exists-1]=textList[counter]

    for word in accomodator:
            text+=str(word) + " "
    print text
test_cases.close()
