def isPrime(n):
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

import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    primes=""
    for i in range(2,int(test.strip())):
        if isPrime(i):
            primes+=str(i) + ","
    primes=primes[:-1]
    print primes
                
test_cases.close()

