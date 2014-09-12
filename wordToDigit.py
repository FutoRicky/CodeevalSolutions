import sys

def WordConverter(x):
    test=str()
    if (x=="zero"):
        test="0"
    elif (x=="one"):
        test="1"
    elif (x=="two"):
        test="2"
    elif (x=="three"):
        test="3"
    elif (x=="four"):
        test="4"
    elif (x=="five"):
        test="5"
    elif (x=="six"):
        test="6"
    elif (x=="seven"):
        test="7"
    elif (x=="eight"):
        test="8"
    elif (x=="nine"):
        test="9"
    return (test)
    
t=str()
strwords=str()
test_cases=open(sys.argv[1],'r')
for line in test_cases:
    strwords=line.strip().split(";")
    for i in range(0,len(strwords)):
        t+=WordConverter(strwords[i])
    print (t)
    t=str()
