import sys

runScript = sys.argv[1:]
try:
    file = open(runScript[0], 'r')
except:
    print("Não foi possível abrir o arquivo")

R = '1'
L = '11'
a = '1'
b = '11'
B = '111'
