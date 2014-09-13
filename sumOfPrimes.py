import itertools

primeCounter=0
accum=0
prime=True
for i in itertools.count(2):
    for divisor in range(2,i):
        if i%divisor==0:
            prime=False
            break;
    if prime:
        accum+=i
        primeCounter+=1
    else:
        prime=True
    if primeCounter==1000:
        break;
print accum
