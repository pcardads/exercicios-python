# gerador de cpf

import random

nove_digitos = ''
for i in range(9):
    nove_digitos += str(random.randint(0, 9))

contador_regressivo_1 = 10

resultado_digito_1 = 0

for digito in nove_digitos:
    resultado_digito_1 += int(digito)*contador_regressivo_1
    contador_regressivo_1 -= 1 # pois a conta deve ser feita de forma regressiva
digito1 = (resultado_digito_1 * 10) % 11 # multiplicando por 10 e depois pegando o resto da divisão por 11

digito1 = digito1 if digito1 <= 9 else 0

dez_digitos = nove_digitos + str(digito1)
contador_regressivo_2 = 11

resultado_digito_2 = 0

for digito in dez_digitos:
    resultado_digito_2 += int(digito)*contador_regressivo_2
    contador_regressivo_2 -= 1
digito2 = (resultado_digito_2 *10) % 11

digito2 = digito2 if digito2 <= 9 else 0

cpf_validado = f'{nove_digitos}{digito1}{digito2}'
print(cpf_validado)