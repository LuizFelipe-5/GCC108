# GCC108 - Trabalho Prático
## Simulador - Máquina de Turing Universal
### Autor: Luiz Felipe Montuani e Silva - 201920253

1) Formatação arquivo "argumento1":
    - O arquivo "argumento1" deve conter em sua primeira linha uma sequência de três números zero (000), sequência que simboliza o início do bloco de transições.
    <br>
    <br>
    - Nas linhas subsequentes do arquivo estará as transições, as quais devem ser formadas pelo estado atual, a letra atual, o próximo estado, a próxima letra e a direção. Todos separados por um número zero e também é necessário acrescentar dois ao final de cada transição que não seja a última da máquina.
    <br>
    Exemplo:
    <br>
    1011101101110100 <br>
    11010111010100 <br>
    11011011110110100 <br>
    11101101110110100 <br>
    1110111011111011101100 <br>
    11110101111010100 <br>
    111101110111110111011 
    <br><br>
    - A linha após o bloco de transições deve conter três números zero (000), sequência que representa o fim do bloco de transições.
    <br><br>
    - Por fim, a linha seguinte deve conter a entrada, a qual deve inciar com o símbolo branco, aqui descrito como uma sequência de três números um (111), em seguida as letras seguintes da palavra, todas separadas por um número zero e uma sequência de três números zero(000) depois da última letra. <br>
    Exemplo:
    <br>
    11101011011011000
    <br>
    <br>
2) Execução: rodar o comando abaixo na raiz do projeto
    - python programa.py argumento1 


