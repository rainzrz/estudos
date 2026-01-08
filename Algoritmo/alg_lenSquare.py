"""
• Existem N colunas feitas de blocos 1x1, posicionadas lado a lado. As alturas das colunas consecutivas formam uma sequência não decrescente. 
• A altura da coluna de índice K (com K no intervalo [0...N−1]) é A[K].
• Qual é o maior quadrado formado por blocos que pode ser encontrado nessa sequência?

Escreva uma função que, dado um array A contendo N inteiros, retorne o comprimento do lado do maior quadrado que pode ser encontrado em A.

Exemplo:
• Dado A = [1, 2, 2, 4, 5], sua função deve retornar 2.
• Dado A = [10, 10, 10, 10], sua função deve retornar 4.

Escreva um algoritmo eficiente considerando as seguintes premissas:
• N é um inteiro no intervalo [1...250.000]
• Cada elemento do array A é um inteiro no intervalo [1...100.000.000]
• Os elementos do array A formam uma sequência não decrescente
"""

def solution(A):  # def significa definir uma função | solution é o nome da função | (A) é o que a função recebe para trabalhar
    n = len(A)  # len significa length (comprimento) | Conta quantos itens existem dentro da lista A
    max_square = 0  # Cria a variável max_square | Começa em 0 | Guarda o maior quadrado encontrado até agora

    for i in range(n):  # range(n) cria números de 0 até n - 1 | i muda de valor a cada repetição
        possible = min(A[i], n - i)  # A[i] pega o valor da lista na posição i | n - i mostra quantas posições ainda existem | min pega o menor valor
        if possible > max_square:  # Se o quadrado atual for maior que o maior já encontrado
            max_square = possible  # Atualiza o maior quadrado encontrado

    return max_square  # Devolve o maior quadrado no final
