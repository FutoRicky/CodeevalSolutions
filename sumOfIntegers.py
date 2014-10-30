import sys
test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    suma=-100000
    largest=-100000
    integerList=[]
    for n in test.strip().split(","):
        integerList.append(int(n))

    if len(integerList)==1:
        largest=integerList[0]

    else:
        for i in range(0,len(integerList)):
            for j in range(i+1,len(integerList)+1):
                if i!=j:
                    suma = sum(integerList[i:j])
                if suma>=largest:
                    largest=suma
    print largest

test_cases.close()
