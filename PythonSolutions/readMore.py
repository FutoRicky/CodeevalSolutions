import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    line = test.strip()
    newLine = ""

    if len(line)<=55:
        print line
    elif len(line)>55:
        line = line[0:40]
        if line.rfind(' ') != -1:
            line=line[0:line.rfind(' ')]

        line+= "... <Read More>"

        print line


test_cases.close()
