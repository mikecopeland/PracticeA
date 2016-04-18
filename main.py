from sys import argv
assert isinstance(argv, object)

script, filename = argv

txt = open(filename)

lines = txt.readline()

def lastWord(word):
    answer = ""
    letters = list(word)
    for letter in letters:
        if letter >= answer[:1]:
           answer = letter + answer
        else:
           answer = answer + letter
    return answer;

for i in range(1, int(lines)+1):
    print("Case " + str(i) + ": " + lastWord(txt.readline()))



