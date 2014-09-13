import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    wordList=[]
    numberList=[]
    fixedString=""
    for i in test.strip().split(","):
        try:
            numberList.append(int(i))
        except:
            wordList.append(i)
    for w in range(0,len(wordList)):
        if w == len(wordList)-1:
            fixedString+=wordList[w]
        else:
            fixedString+= wordList[w]+","
    for n in range(0,len(numberList)):
        if n == len(numberList)-1:
            fixedString+=str(numberList[n])
        else:
            if n==0 and fixedString!="":
                fixedString+="|" + str(numberList[n]) + ","
            else:
                fixedString+=str(numberList[n]) + ","
    print fixedString
test_cases.close()

