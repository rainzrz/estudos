"""
Imprima a palavra: ‘ALURA’ de modo que cada letra fique em uma linha, como mostrado a seguir:
A
L
U
R
A
"""

palavra = input("Digite a palavra desejada: ")
palavra_vertical = list(palavra)

for letra in palavra_vertical:
    print(f"{letra}")
