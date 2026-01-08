"""
• Na cidade existem N distritos (numerados de 0 a N−1) conectados por M ruas. 
• As conexões são descritas por dois arrays, A e B, ambos de tamanho M. Um par (A[K], B[K]) indica uma rua entre os distritos A[K] e B[K] (para K de 0 a M−1).
• Também existem L hospitais, cujas localizações são descritas pelo array H. O hospital de índice J está localizado no distrito H[J] (para J de 0 a L−1).
• Se uma ambulância for necessária em um distrito, ela é enviada a partir do hospital que consiga chegar em menor tempo. 
• A ambulância sempre percorre o caminho mais curto possível, e atravessar uma rua leva exatamente 1 minuto.
• Potencialmente, pode haver um paciente precisando de ajuda em qualquer distrito da cidade. 
• Qual é o maior tempo necessário para alcançar qualquer paciente possível com uma ambulância?

Escreva uma função que, dado um inteiro N, os arrays A e B descrevendo as ruas da cidade e o array H indicando as localizações dos hospitais, retorne um inteiro que representa o maior tempo de deslocamento (em minutos) entre um distrito e o hospital mais próximo.

• Se algum distrito não puder ser alcançado por uma ambulância, a função deve retornar -1.

Escreva um algoritmo eficiente considerando as seguintes premissas:
• N é um inteiro no intervalo de 1 a 100.000
• M é um inteiro no intervalo de 1 a N
• L é um inteiro no intervalo de 1 a N
• Os elementos de H são todos distintos
• Cada elemento dos arrays A, B e H é um inteiro no intervalo de 0 a N−1
• Toda rua conecta dois distritos diferentes
• Não existem múltiplas ruas entre o mesmo par de distritos

Exemplo 1:
• Dado N = 3, A = [1], B = [2] e H = [0, 1, 2], sua função deve retornar 0.

Exemplo 2:
• Dado N = 6, A = [0, 1, 1, 3], B = [1, 2, 3, 4] e H = [2, 4], sua função deve retornar -1.

Exemplo 3:
• Dado N = 6, A = [0, 1, 1, 3, 0, 4], B = [1, 2, 3, 4, 5, 5] e H = [2, 4], sua função deve retornar 2.
"""

def solution(N, A, B, H):
    city_map = [[] for _ in range(N)]
    for i in range(len(A)):
        city_map[A[i]].append(B[i])
        city_map[B[i]].append(A[i])
    time_to_hospital = [-1] * N

    districts_to_visit = []
    index = 0

    for hospital in H:
        time_to_hospital[hospital] = 0
        districts_to_visit.append(hospital)

    while index < len(districts_to_visit):
        current_district = districts_to_visit[index]
        index += 1

        for connected_district in city_map[current_district]:
            if time_to_hospital[connected_district] == -1:
                time_to_hospital[connected_district] = (
                    time_to_hospital[current_district] + 1
                )
                districts_to_visit.append(connected_district)

    longest_time = 0
    for time in time_to_hospital:
        if time == -1:
            return -1
        if time > longest_time:
            longest_time = time

    return longest_time