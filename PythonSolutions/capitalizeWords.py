import sys
import string

sentence=[]
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    for i in test.strip().split(" "):
        sentence.append(i)
    for w in range(0,len(sentence)):
        
        if sentence[w][0] not in string.ascii_lowercase:
            print sentence[w],
        else:
            print sentence[w][0].upper() + sentence[w][1:],
    print 
    sentence=[]
test_cases.close()
