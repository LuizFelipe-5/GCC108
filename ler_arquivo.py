'''
Arquivo que possui a função responsável por tentar abrir e formatar o "argumento1".
'''
__author__ = "Luiz Felipe Montuani e Silva - 201920253"

import sys

def ler_arquivo():
    '''
    Função que tentar realizar a leitura e separação do arquivo "argumento1" em linhas,
    as quais representam as transições.
    :return: retorna o texto e as transições
    '''
    runScript = sys.argv[1:]

    try:
        arquivo = open(runScript[0], 'r')

        texto = arquivo.read().splitlines()

        entrada = texto[-1].split('0')
        
        transicoes = []

        for line in texto[1:len(texto)-2]:
            transicoes.append(line.split('0'))

        return entrada, transicoes
    
    except:
        print("Não foi possível abrir o arquivo")

    


    


    
