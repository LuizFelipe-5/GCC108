import sys

runScript = sys.argv[1:]
try:
    file = open(runScript[0], 'r')
except:
    print("Não foi possível abrir o arquivo")

text = file.read().splitlines()
