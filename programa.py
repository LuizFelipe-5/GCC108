"""
Arquivo que centraliza todas as operações necessárias para a realização da simulação da 𝑈𝐻 (Universal with Heuristics).
"""
__author__ = "Luiz Felipe Montuani e Silva - 201920253"

from ler_arquivo import ler_arquivo
from maquina import Maquina

try:
    entrada, transicoes = ler_arquivo()
    maquina = Maquina(entrada, transicoes)
    maquina.executar()
except:
    # Tratamento feito na ler_arquivo.py
    pass
    