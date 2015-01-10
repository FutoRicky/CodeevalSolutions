import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    argument=[]
    for i in test.strip().split(", "):
        argument.append(i)
    for l in range(0,len(argument[1])):
        argument[0]=argument[0].replace(argument[1][l],"")
    print argument[0]
        
test_cases.close()
