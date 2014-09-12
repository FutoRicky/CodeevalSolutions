import sys

def AgeDistribution(x):
    if 0<=x<=2:
        print("Still in Mama's arms")
    elif 3<=x<=4:
        print("Preschool Maniac")
    elif 5<=x<=11:
        print("Elementary school")
    elif 12<=x<=14:
        print("Middle school")
    elif 15<=x<=18:
        print("High school")
    elif 19<=x<=22:
        print("College")
    elif 23<=x<=65:
        print("Working for the man")
    elif 66<=x<=100:
        print("The Golden Years")
    elif 0>x>100:
        print("This program is for humans")
    return 0

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    AgeDistribution(int(test))
test_cases.close()

