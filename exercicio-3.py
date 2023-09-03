# 3. Desenvolver o jogo term.ooo a partir de uma lista de palavras.  Devem aparecer as letras que
# já foram descobertas, as letras já tentadas no teclado e assim por diante. Atente-se à
# formatação.


# Foi divido o problema em metodos para facilitar a leitura e entendimento do codigo.  O metodo principal (jogar_termoo) 
# é responsavel por chamar os demais metodos e controlar o fluxo do jogo. Nele há um loop com condição de parada, que só é quebrado quando o jogo termina, 
# seja por vitoria ou derrota.
# 
# Primeiramente é escolhida uma palavra aleatória da lista de palavras. Após isto sao criados as listas de letras corretas e letras corretas fora da posição e é recebido o input da tentativa
# do usuário. Além disso criei uma variavel de controle chamada palavra_atual, que é uma lista com o mesmo tamanho da palavra escolhida, e que vai sendo preenchida com as letras corretas (tanto na posição correta quanto na posição errada).
# 
# Após a validação da entrada, é feita a verificação se a tentativa é igual a palavra escolhida. Se for, o jogo termina com sucesso. Caso contrário, é feita a verificação de cada letra da tentativa, se ela está na palavra escolhida e se está na posição correta ou não.
# 
# Depois disso um loop corrige as letras corretas fora da posição, pois se a letra estiver na palavra e na posição correta, ela não deve ser considerada como correta fora da posição.
# 
# Ao final deste processo, é feita a impressão da palavra atual, com as letras corretas (verde) e incorretas, e as letras corretas que estão fora da posição correta (amarelas).

import random

GREEN = "\033[0;32m"
YELLOW = "\x1b[33m"
RESET = "\033[0;0m"


arquivo = "lista_palavras.txt" 

def le_arquivo(arq):
    ''' Lê arquivo especificado e retorna uma lista com todas as linhas '''   
     
    with open(arq, encoding="UTF-8") as f:
        return [linha.strip() for linha in f]

def escolher_palavra():
    ''' Escolhe uma palavra aleatória da lista de palavras'''

    palavras = le_arquivo(arquivo)
    return random.choice(palavras)

def imprimir_palavra_atual(palavra_atual, letras_corretas_fora_posicao, palavra):
    ''' Imprime a palavra atual, com as letras corretas (verde) e incorretas, e as letras corretas que estão fora da posição correta (amarelas)'''
    
    print(f"Palavra atual: ", end="")

    for i in range(len(palavra_atual)):
        if palavra_atual[i] == palavra[i]:
            print(GREEN + f"{palavra_atual[i]} " + RESET, end="")
        elif palavra_atual[i] in letras_corretas_fora_posicao:
            print(YELLOW + f"{palavra_atual[i]} " + RESET, end="")
        else:
            print(f"{palavra_atual[i]} ", end="")

def jogar_termoo():
    '''Função principal do jogo term.ooo.'''
    
    palavra = list(escolher_palavra().lower())
    letras_corretas = list()
    letras_corretas_fora_posicao = list()
    max_tentativas = 6

    print("Bem-vindo ao Term.ooo!")

    palavra_atual = list(''.join(['_' for letra in palavra]))

    while max_tentativas > 0:
        imprimir_palavra_atual(palavra_atual, letras_corretas_fora_posicao, palavra)

        tentativa = list(input("\nDigite uma palavra com cinco letras: ").lower())

        # validar entrada
        if len(tentativa) == 5:

            if tentativa == palavra:
                # se a tentativa for igual a palavra, sucesso
                print(f"Parabéns! Você adivinhou a palavra: ", end="")
                for letra in palavra:
                    print(GREEN + f"{letra} " + RESET, end="")
                print("\n")

                break

            for i in range(len(tentativa)):
                
                # se a tentativa[i] estiver na palavra e não na posição i, deve guardar na palavra atual na posição i com indicativo de posição errada
                # se a tentativa[i] estiver na palavra e na posição i, deve guardar na palavra atual na posição i
                
                if tentativa[i] == palavra[i]:
                    palavra_atual[i] = tentativa[i]
                    letras_corretas.append(tentativa[i])
                    continue
                    
                if tentativa[i] in palavra and tentativa[i] != palavra[i]:
                    palavra_atual[i] = tentativa[i]
                    
                    letras_restantes = list(letra for letra in palavra if letra not in letras_corretas)
                    letras_corretas_fora_posicao.append(tentativa[i]) if tentativa[i] in letras_restantes else None
                    continue

            for letra in letras_corretas_fora_posicao:
                if letra in letras_corretas:
                    letras_corretas_fora_posicao.remove(letra)
            
            max_tentativas -= 1
        else:
            print("Entrada inválida. Por favor, digite uma palavra com cinco letras.")

    if max_tentativas == 0:
        print(f"Você perdeu, zé! A palavra era: {palavra}")


jogar_termoo()