import sys
test_cases = open(sys.argv[1], 'r')

def funVerifyNumbers(i, test):
    count=0
    for n in range(0,len(test)):
        if int(test[n])==i:
            count+=1
    if int(test[i])==count:
        return True
    else:
        return False

for test in test_cases:
    check=False
    test = test.strip()
    for i in range(0,len(test)):
        if funVerifyNumbers(i,test)==False:
            print 0
            break
        elif i==len(test)-1:
            check=True
    if check:
        print 1

test_cases.close()
