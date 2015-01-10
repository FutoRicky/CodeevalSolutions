import sys

stringArray = []
count=1
rollerCoaster=""

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    stringArray=list(test.strip())
    for e in range(0,len(stringArray)):
        if stringArray[e].isalpha():
            if count%2!=0:
                stringArray[e]=stringArray[e].upper()
                count+=1
            else:
                stringArray[e]=stringArray[e].lower()
                count+=1
        else:
            pass
    for l in stringArray:
        rollerCoaster+=l
    print rollerCoaster
    stringArray=[]
    count=1
    rollerCoaster=""
            
test_cases.close()
