#Joguinho de adivinhação
secret = 'perfume'
digits = []
chance = 3

while True:
    if chance <= 0:  # Contador de chances
        print ('Você usou todas as suas chances, então você perdeu... :(')
        break

    letter = input('Digite uma letra: ')
    if letter.__len__() > 1:
        print('Ahhh, isso não vale, digite uma letra! ¬¬')
        continue

    digits.append(letter)

    if letter in secret:  # Checando as letras da palavra secreta
        print(f'UHUUUU, a letra {letter} existe na palavra! :D')
    else:
        print(f'Affff, a letra {letter} não existe na palavra secreta. :(')
        digits.pop()

    temp_secret = ''  # Apresentando os acertos das letras da palavra
    for secret_letter in secret:
        if secret_letter in digits:
            temp_secret += secret_letter
        else:
            temp_secret += '*'
    print(temp_secret)
    if temp_secret == secret:  # finalização
        print(f'PARABÉNS! Você acerto que a palavra secreta é {secret}! ;D')
        break
    else:
        print (f'A palavra secreta está assim: {temp_secret}')

    if letter not in secret:
        chance -= 1
    print (f'Você ainda tem {chance} chances!')
