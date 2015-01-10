import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    letter=""
    boolLetter=False
    test.strip()
    for i in range(0,len(test)):
        if boolLetter==False:
            for j in range(0, len(test)):
                if test[i]==test[j] and i!=j:
                    break
                elif j==len(test)-1:
                    print test[i]
                    boolLetter=True
                    break

test_cases.close()
