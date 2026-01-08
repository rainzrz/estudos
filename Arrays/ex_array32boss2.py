"""
FINAL BOSS 2. Hospital mais próximo

Uma cidade possui N distritos numerados de 0 até N-1.
Os distritos são conectados por M ruas bidirecionais.

As ruas são descritas por dois arrays A e B,
onde uma rua conecta A[K] com B[K].

Existem hospitais localizados em alguns distritos,
descritos pelo array H.

Uma ambulância sempre sai do hospital mais próximo
e percorre o caminho mais curto.
Cada rua leva exatamente 1 minuto para ser percorrida.

Crie uma função:
def solution(N, A, B, H)

que retorne o maior tempo necessário
para uma ambulância chegar a qualquer distrito.

Se existir algum distrito que não pode ser alcançado
por nenhuma ambulância, retorne -1.

Exemplos:
N=3, A=[1], B=[2], H=[0,1,2]
Saída: 0

N=6, A=[0,1,1,3], B=[1,2,3,4], H=[2,4]
Saída: -1

N=6, A=[0,1,1,3,0,4], B=[1,2,3,4,5,5], H=[2,4]
Saída: 2

Objetivo:
Avaliar domínio de grafos, BFS e casos limite.
"""
