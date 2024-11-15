"""
Faca um programa que pergunte a hora ao usuario e, baseando-se no horario descrito, exiba a saudacao apropriada;
use bom dia 0-11, boa tarde 12-17 e boa noite 18-23

"""

hora = input('Que horas sao? Por favor utilize apenas numeros: ')

if (int(hora)>0) and (int(hora)<=11):
    print('Bom dia!')

elif (int(hora)>=12) and (int(hora)<=17):
    print('Boa tarde!')

else: 
    print('Boa noite!')
