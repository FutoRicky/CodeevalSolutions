import sys

splitter=[]
numbers=[]
endLoop=False

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    for i in test.strip().split(";"):
        splitter.append(i)
    numbers=splitter[1].split(",")
    for n1 in range(0,len(numbers)):
        for n2 in range(1,len(numbers)):
            if numbers[n1]==numbers[n2] and n1!=n2:
                print numbers[n1]
                endLoop=True
        if endLoop:
            break
            
    splitter=[]
    numbers=[]
    endLoop=False
test_cases.close()
