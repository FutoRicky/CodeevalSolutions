import sys

def isPrime(n):
    """"precondition n is a nonnegative integer
postcondition:  return True if n is prime and False otherwise."""
    if n < 2: 
         return False;
    if n % 2 == 0:
         # return False
         return n == 2
    k = 3
    while k*k <= n:
         if n % k == 0:
             return False
         k += 2
    return True

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    count=0
    rangeSaver=[]
    for i in test.strip().split(","):
        rangeSaver.append(i)
    for j in range(int(rangeSaver[0]),int(rangeSaver[1])+1):
        if isPrime(j):
            count+=1
    print count

test_cases.close()
