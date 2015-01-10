import sys

longestWord=""
check=""

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    for w in test.strip().split(" "):
        check=w
        if len(check)>len(longestWord):
            longestWord=check
    print longestWord
    longestWord=""
    check=""

test_cases.close()
