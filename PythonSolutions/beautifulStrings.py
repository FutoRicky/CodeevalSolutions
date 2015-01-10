accum=0
beauty=26

import sys
from collections import Counter
import string
import re
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    dictPrueba=Counter(''.join(re.findall("[a-zA-Z]+", test)).strip().replace(" ","").lower())
    dictPrueba=dictPrueba.most_common()
    for i in range(0,len(dictPrueba)):
        accum+=dictPrueba[i][1]*beauty
        beauty-=1
    print accum
    accum=0
    beauty=26
test_cases.close()
