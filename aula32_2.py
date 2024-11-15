"""
Faca um programa que peca o primeiro nome do usuario. ZSe o nome tiver 4 letras ou menos escreva "Seu nome e curto";
se tiver entre 5 e 6 letras, escreva "Seu nome e normal";
se tiver mais de 6, escreva "Seu nome e muito grande"

"""

nome = input('Digite o seu primeiro nome: ')
tamanho_nome = len(nome)

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print('Seu nome e muito curto.')

    elif tamanho_nome >=5 and tamanho_nome <=6:
        print('Seu nome e normal.')

    else:
        print('Seu nome e muito grande')
else:
    print('Digite mais de uma letra.')
