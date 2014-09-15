import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    word=""
    check=[]
    for i in test.strip().split(","):
        check.append(i)
    word = check[1]
    
    if check[0].endswith(word):
        print 1
    else:
        print 0
test_cases.close()


