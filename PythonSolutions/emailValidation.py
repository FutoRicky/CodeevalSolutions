import sys
import re

emailCheck= re.compile(r"(^[-!#$%&'*+/=?^_`{}|~0-9A-Z]+(\.[-!#$%&'*+/=?^_`{}|~0-9A-Z]+)*"  # dot-atom
    r'|^"([\001-\010\013\014\016-\037!#-\[\]-\177]|\\[\001-011\013\014\016-\177])*"' # quoted-string
    r')@(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?$', re.IGNORECASE)  # domain)

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test.strip()!="":
        if emailCheck.match(test.strip()):
            print("true")
        else: 
            print("false")
    else:
        pass
           

test_cases.close()
