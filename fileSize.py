from os import path
import sys
test_cases = open(sys.argv[1], 'r')
size=path.getsize(sys.argv[1])
print size

test_cases.close()

