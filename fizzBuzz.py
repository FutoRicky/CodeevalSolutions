import sys

count=0
a=int()
b=int()
n=int()

def FizzBuzz(a,b,n):
    for j in range(1,n+1):
        int(j)
        int(a)
        int(b)
        int(n)
        if (j%a==0 and j%b==0):
            print "FB",
        elif j%a==0:
            print "F",
        elif j%b==0:
            print "B",
        else:
            print j,
    print "\n"    
    return 0 


test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    for i in test.strip().split(" "):
       if count==0:
           a=int(i)
           count+=1
       elif count==1:
           b=int(i)
           count+=1
       elif count==2:
           n=int(i)
           count=0
       
       FizzBuzz(a,b,n)
    a=int()
    b=int()
    n=int()
test_cases.close()
