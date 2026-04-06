from random import randint
from time import sleep

#boas_vindas 
print('Seja bem-vindo ao \033[30;45mJogo de Adivinhações!\033[m \ndesenvolvido por: \033[35mLara Francieli Furlaneti Gonzaga\033[m. ')
nome = input('Qual é o seu nome? ')
print('Que nome bonito, {}! Vamos começar nosso jogo...' .format(nome.title()))

#loop_do_jogo
jogar = 's'
while jogar == 's':
    sleep(2)
    print('*=' *10, '\033[34m🤔 PENSANDO EM UM NÚMERO 🤔\033[m', '=*' *10)
    numero_correto = randint(1,10)
    sleep(2)
    print('Prontinho! Está na hora de você tentar acertar em que número eu pensei.')

    #tentativa_do_usuario
    tentativa = int(input('Digite um número entre 1 e 10: '))

    #verificação_tentativa_usuario
    if tentativa == numero_correto:
        print('UAU! Está \033[32;40mCORRETO\033[m!!! O número que eu pensei foi {} 😎.' .format(numero_correto))
    else:
        print('Que pena, você \033[31mNÃO ACERTOU \033[m. O número que eu pensei foi {} 😢.' .format(numero_correto))
    sleep(1)

    #jogar_novamente
    jogar = input('Você quer jogar de novo? Digite \033[32mS \033[mpara SIM e \033[31mN \033[mpara NAO: ' )
    jogar = jogar.lower().strip()
if jogar == 'n':
     print('Ok, até outro dia, {}! Foi muito divertido jogar com você 😊' .format(nome.title()))
   