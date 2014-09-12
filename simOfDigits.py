import sys

test_cases = open(sys.argv[1], 'r')
a=str()
suma=0
intnumber=str()

for test in test_cases:
    a=list(str(test.strip()))
    for i in a:
        intnumber=int(i)
        suma+=intnumber
    print(suma)
    suma=0
test_cases.close()
