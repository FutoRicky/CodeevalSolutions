import sys

mapping=[str(x) for x in range(1,27)]
def decodeNumber(test):
    if not test:
        return 1

    count = 0

    for i in mapping:
        if test.startswith(i):
            count += decodeNumber(test[len(i):])

    return count

    if checkFirstLast==2:
        count+=1
    return count + 1

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip()
    print decodeNumber(test)

test_cases.close()
