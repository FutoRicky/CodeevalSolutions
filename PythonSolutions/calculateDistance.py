import sys
from math import sqrt
def DistCalc(x1,x2,y1,y2):
    dist = sqrt( (x2 - x1)**2 + (y2 - y1)**2 )
    print int(dist)

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    coordinates=[]
    for i in test.strip().split(" "):
        coordinates.append(i)
    x1=coordinates[0].replace("(", "")
    x1=x1.replace(",", "")
    x2=coordinates[2].replace("(", "")
    x2=x2.replace(",", "")
    y1=coordinates[1].replace(")", "")
    y2=coordinates[3].replace(")", "")

    DistCalc(int(x1),int(x2),int(y1),int(y2))

test_cases.close()
