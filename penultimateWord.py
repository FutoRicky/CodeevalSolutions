import sys

wordList=[]
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    for i in test.strip().split(" "):
        wordList.append(i)
    print wordList[len(wordList)-2]
    wordList=[]

test_cases.close()
