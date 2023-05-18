import random

palavras = ['quadriceps', 'gluteo', 'posterior', 'ombro', 'costas', 'peito', 'triceps', 'biceps' ]
palavra_random = random.choice(palavras)
palavra_oculta = ['_'] * len(palavra_random)
tentativas = 10

print("\n-Jogo da forca maromba-\n")
print("Você possuira 8 tentativas para acertar sua palavra!\n")

for tentativa in range(tentativas):
    
    palavra_jogo = print(f'Sua palavra é: {palavra_oculta}')
    letra_index = input("\nDigite uma letra: ")    
    print(f'Você realizou {tentativa+1} tentativa de {tentativas} tentativas!')

    if letra_index in palavra_random:
        print("\nEssa letra existe na palavra!")
        
        for letra in range(len(palavra_random)):
            if letra_index == palavra_random[letra]:
                palavra_oculta[letra] = letra_index

    else:
        print("\nEssa letra não existe na palavra!\n")

    if '_' not in palavra_oculta:
        break


if '_' not in palavra_random and palavra_random == 'quadriceps' or palavra_random == 'gluteo' or palavra_random == 'posterior':
    print("Parabéns, você é um maromba de verdade e isso é um sinal para você ir treinar inferiores!")
elif '_' not in palavra_random and palavra_random == 'ombro' or palavra_random == 'biceps' or palavra_random == 'costas' or palavra_random == 'peito' or palavra_random == 'triceps':
    print("Parabéns, você é um maromba de verdade e isso é um sinal para você ir treinar superiores!")
else: 
    print("Você perdeu...frango!")



