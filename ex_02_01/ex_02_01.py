#Exercício 2: Escreva um programa que use inputs para solicitar ao
#usuário seu nome e, em seguida, faça um cumprimento

nome = input('Digite seu nome: ')
print('Ola, {}' .format(nome))
print(f'Ola, {nome}!')
print('Ola,', nome, '!')
print('Ola, %s!' %nome)
