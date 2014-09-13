import sys

letters=[]
swapCase=""

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    letters=list(test.strip())
    for i in range(0,len(letters)):
        if letters[i].isupper():
            letters[i]=letters[i].lower()
        elif letters[i].islower():
            letters[i]=letters[i].upper()
        else:
            pass
    for l in letters:
        swapCase+=l
    print swapCase
    letters=[]
    swapCase=""
            
test_cases.close()
