import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    numbers=[]
    for i in test.strip().split(","):
        numbers.append(int(i))
    for n in range(0,1000):
        powerNumber=numbers[1]*n
        if powerNumber>numbers[0]:
            print powerNumber
            break
test_cases.close()
