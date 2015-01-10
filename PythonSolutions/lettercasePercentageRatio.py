import sys

def funAverages(upperCount,lowerCount, wordLength):
    upperPercentage=(float(upperCount)/wordLength)*100
    lowerPercentage=(float(lowerCount)/wordLength)*100
    
    print "lowercase:",
    print "{0:.2f}".format(lowerPercentage),
    print "uppercase:", 
    print "{0:.2f}".format(upperPercentage)

    return 0

letters=[]
upperCount=0
lowerCount=0
wordLength=0

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    wordLength=len(test.strip())
    letters=list(test.strip())
    for i in range(0,len(letters)):
        if letters[i].isupper():
            upperCount+=1
        else:
            lowerCount+=1
    funAverages(upperCount,lowerCount,wordLength)
    letters=[]
    upperCount=0
    lowerCount=0
test_cases.close()
