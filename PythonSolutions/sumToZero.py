import sys

numbers=[]
count=0

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    for i in test.strip().split(','):
        numbers.append(int(i))
    for n1 in range(0,len(numbers)):
        for n2 in range(n1+1,len(numbers)):
            for n3 in range(n2+1,len(numbers)):
                for n4 in range(n3+1,len(numbers)):
                    if numbers[n1]+numbers[n2]+numbers[n3]+numbers[n4]==0:
                        count+=1
    print count
    count=0
    numbers=[]
test_cases.close()

