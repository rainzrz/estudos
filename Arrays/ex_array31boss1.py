"""
FINAL BOSS 1. Maior quadrado em colunas

Existem N colunas formadas por blocos 1x1 lado a lado.
As alturas das colunas formam uma sequência não decrescente.

A altura da coluna K é dada por A[K].

Crie uma função:
def solution(A)

que retorne o comprimento do lado do maior quadrado
formado por blocos que pode ser encontrado nessas colunas.

Um quadrado de lado X só pode existir se houver
X colunas consecutivas com altura maior ou igual a X.

Exemplos:
Entrada: [1, 2, 2, 4, 5]
Saída: 2

Entrada: [10, 10, 10, 10]
Saída: 4

Restrições:
N está no intervalo de 1 até 250000
Cada valor de A está entre 1 e 100000000
O array é não decrescente

Objetivo:
Testar raciocínio matemático, limites e eficiência.
"""
