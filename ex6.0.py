#Desenvolva um programa que receba um número inteiro como entrada do usuário e
#verifique se o número informado é um número primo. Um número primo é um número que
#somente pode ser divisível por 1 e por si mesmo

num = int(input('Informe o numero inteiro:'))

primo = True
for i in range(2, num):
    if num % i == 0:
        primo = False
        break
if primo:
    print('É primo!')
else:
    print('Não é primo!')