import sys
test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    numbers1String=""
    numbers2String=""
    control=[]
    numbers1=[]
    numbers2=[]
    for i in test.strip().split(" | "):
        control.append(i)
    numbers1String=control[0]
    numbers2String=control[1]
    
    for n1 in numbers1String.split(" "):
        numbers1.append(n1)
    for n2 in numbers2String.split(" "):
        numbers2.append(n2)
        
    for j in range(0,len(numbers1)):
        if j != len(numbers1)-1:
            print int(numbers1[j])*int(numbers2[j]),
        else:
            print int(numbers1[j])*int(numbers2[j])
test_cases.close()

