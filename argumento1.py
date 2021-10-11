from os import stat
import sys

runScript = sys.argv[1:]
try:
    file = open(runScript[0], 'r')
except:
    print("Não foi possível abrir o arquivo")

text = file.read().splitlines()

transitions = []
transitions2 = []
transitions3 = []
input = text[-1]
initialState = 1
aux = 0
white = 3

for line in text[1:len(text)-2]:
    transitions.append(line)
    transitions2.append(line)
    transitions3.append(line)

for item in input:
    if item == '1':
        aux += 1
    else:
        # verificar no transitions (aux e estado atual)
        # c, initialState = funcao()
        aux = 0

# funcao retorna a letra e o proximo estado


def funcao():
    return a, b
