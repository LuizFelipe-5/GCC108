__author__ = "Luiz Felipe Montuani e Silva - 201920253"
class Maquina: 
    '''
    Classe que representa a Máquina de Turing Universal, aqui chamada de 𝑈𝐻 (Universal with Heuristics).
    '''
    def __init__ (self, entrada, transicoes):
        '''
        Construtor da classe Máquina.
        '''
        self.entrada = entrada
        self.transicoes = transicoes
        self.estado = '1'
        self.letra = ''
    
    def transicao(self, estado, letra):
        '''
        Função que procura se existe transição dado um estado atual e a posição atual da cabeça de leitura e
        retorna a nova letra, o proximo estado e a direção.
        :return: novo estado, nova letra e a direção
        '''
        estaCorreto = False
        novoEstado = ''
        novaLetra = ''
        direcao = ''

        for linha in self.transicoes:
            if (not estaCorreto):
                if(linha[0] == estado and linha[1] == letra):
                    estaCorreto = True
                    novoEstado = linha[2]
                    novaLetra = linha[3]
                    direcao = linha[4]
            
        return novoEstado, novaLetra, direcao
    
    def computar_entrada(self):
        '''
        Função que dada a entrada informada, verifica se a mesma é válida e, caso seja, percorre e escreve na fita
        a palavra formada.
        '''
        auxWhile = 0
        aux = 0
        estado = ''
        count = 0
        while(auxWhile < len(self.entrada)):
            if self.entrada[auxWhile] != '':
                aux = self.entrada[auxWhile]
                self.estado, self.letra, direcao = self.transicao(self.estado, aux)
                
                # Heurística para a condição de parada
                if(estado == self.estado):
                    count += 1
                    if(count == 30):
                        self.entrada = ''
                        break
                else:
                    count = 0                   
                self.entrada[auxWhile] = self.letra
                estado = self.estado

                if direcao == '1':
                    auxWhile += 1
                else:
                    auxWhile -= 1
            else:
                auxWhile += 1
    
    def resultado(self):
        '''
        Função que escreve na tela o resultado da simulação da 𝑈𝐻 (Universal with Heuristics).
        '''
        if (self.entrada == ''):
            print('Simulação encerrada - Heurística para loop infinito')
        else:    
            for item in self.entrada:
                if item != '':
                    print(item, end='0')
            print(end='00')
            print()

    def executar(self):
        '''
        Função que executa a simulação da 𝑈𝐻 (Universal with Heuristics).
        '''
        self.computar_entrada()
        self.resultado()
    


