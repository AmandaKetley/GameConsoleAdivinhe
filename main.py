from random import randint

cont = 5

while cont > 0 :

    computador = randint(0,10)
    tentativas = cont

    print('\033[1;33m-=-\033[m'*20)
    print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
    print('\033[1;31mvoce tem {} tentativas\033[m'.format(tentativas))
    print('\033[1;33m-=-\033[m'*20)

    jogador = int(input('Em que número eu pensei?'))

    if jogador == computador:
        print('Parabens! Você conseguiu')
    else:
        print('Não foi dessa vez, eu pense em {} e não no {}'.format(computador,jogador))

    cont = cont -1
