import sys

runScript = sys.argv[1:]
try:
    file = open(runScript[0], 'r')
except:
    print("Não foi possível abrir o arquivo")

text = file.read().splitlines()

transitions = []
input = text[-1]

for line in text[1:len(text)-2]:
    transitions.append(line)
