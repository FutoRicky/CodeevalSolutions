import sys
test_cases = open(sys.argv[1], 'r')

morseCode = {'.-':'A', '-...':'B', '-.-.':'C', '-..':'D', '.':'E', '..-.':'F',
'--.':'G', '....':'H', '..':'I', '.---':'J', '-.-':'K', '.-..':'L', '--':'M',
'-.':'N', '---':'O', '.--.':'P', '--.-':'Q', '.-.':'R', '...':'S', '-':'T',
'..-':'U', '...-':'V', '.--':'W', '-..-':'X', '-.--':'Y', '--..':'Z', " ":" ",
'.----':'1', '..---':'2', '...--':'3', '....-':'4', '.....':'5', '-....':'6',
'--...':'7', '---..':'8', '----.':'9', '-----':'0'}

code = " "

for test in test_cases:
  for j in test.strip().split("  "):
    for i in j.strip().split(" "):
        code+=morseCode[i]
    code+=" "
  print code
  code = ""

test_cases.close()
