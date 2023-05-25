import random

sorteio = random.randint(0, 11)
acertou = False
print(sorteio)

for i in range(1, 11):
    palpite = int(input('Informe o seu palpite:  '))

    if palpite == sorteio:
        acertou = True
        print(f'Parabéns, você acertou na {i} tentativa tu é o cara!!!!')
        break

    else:
        print('Perdeu, KSKSKSKS, vai dnv burrão')
        if palpite < sorteio:
            print('você chutou muito baixo')
        else:
            print('Você chutou muito perto!')

if acertou == False:
    print(f'O número sorteiado foi {sorteio}')

