"""
faca um programa que peca ao usuario para digitar um numero inteiro
informe se este numero e par ou impar. caso o usuario nao digite um numero
inteiro, informe que nao e um numero inteiro

"""

numero = input('Digite um numero inteiro: ')
if numero.isdigit():
    if (int(numero))%2 == 0:
        print('O numero que voce digitou e par.')
    else:
        print('O numero que voce digitou e impar.')

else:
    print('Voce nao digitou um numero inteiro.')