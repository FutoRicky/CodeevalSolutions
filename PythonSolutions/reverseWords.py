import sys

wordList=[]
reverse=""
count=0
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    for word in test.strip().split(" "):
        wordList.append(word)
    for i in range(len(wordList)-1,-1,-1):
        reverse+=wordList[i]
        reverse+=" "
    print reverse
    wordList=[]
    reverse=""

test_cases.close()
