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
input = text[-1].split('0')
auxWhile = 0
state = '1'
aux = ''
letra = ''
direction = ''


for line in text[1:len(text)-2]:
    transitions.append(line.split('0'))
    transitions2.append(line)
    transitions3.append(line)


# funcao retorna a nova letra, o proximo estado e a direcao


def transiction(state, letra):
    isCorrect = False
    newState = ''
    newWord = ''
    direction = ''

    for line in transitions:
        if (not isCorrect):
            if(line[0] == state and line[1] == letra):
                isCorrect = True
                newState = line[2]
                newWord = line[3]
                direction = line[4]
    return newState, newWord, direction


while(auxWhile < len(input)):
    if input[auxWhile] != '':
        aux = input[auxWhile]
        state, letra, direction = transiction(state, aux)
        input[auxWhile] = letra

        if direction == '1':
            auxWhile += 1
        else:
            auxWhile -= 1
    else:
        auxWhile += 1

for item in input:
    if item != '':
        print(item, end='0')
print(end='00')
print()
