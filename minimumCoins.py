import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    coin1=1
    coin3=3
    coin5=5
    minimum=0
    test=int(test.strip())
    if test>=coin5:
        while(test>=coin5):
            test-=coin5
            minimum+=1
    if test>=coin3:
        while(test>=coin3):
            test-=coin3
            minimum+=1
    if test>=coin1:
        while(test>=coin1):
            test-=coin1
            minimum+=1    
        
    print minimum

test_cases.close()
