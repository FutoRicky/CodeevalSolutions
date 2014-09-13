mport sys

alphabet = ["a", "b","c", "d","e", "f","g", "h","i", "j","k", "l","m", "n","o", "p","q", "r","s", "t","u", "v","w", "x","y", "z"]


test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    wordsNotThere = ""
    test.strip()
    for i in alphabet:
        if i in test.lower():
            pass
        else:
            wordsNotThere+=i
    if wordsNotThere=="":
        print "NULL"
    else:
        print wordsNotThere

test_cases.close()

