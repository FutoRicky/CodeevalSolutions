import sys
suma=0
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
        suma+=int(test)
print suma

test_cases.close()
