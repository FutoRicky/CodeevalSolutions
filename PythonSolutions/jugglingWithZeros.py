import sys

def StringToBinary(flag,zero):
    val=str()
    if flag=="0":
        for i in zero:
            val+="0"
    elif flag=="00":
        for i in zero:
            val+="1" 
    return (val)

binary=str()
num=1
flag=""
zero=""
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    for i in test.strip().split(" "):
        if num%2!=0:
            flag=i
            num+=1
        elif num%2==0:
            zero=i
            binary+=StringToBinary(flag,zero)
            num+=1
    print(int(binary, 2))
    binary=""
test_cases.close()

