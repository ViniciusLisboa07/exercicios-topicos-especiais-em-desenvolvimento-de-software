# 3. Desenvolver o jogo term.ooo a partir de uma lista de palavras.  Devem aparecer as letras que
# já foram descobertas, as letras já tentadas no teclado e assim por diante. Atente-se à
# formatação.

import random

GREEN = "\033[0;32m"
YELLOW = "\x1b[33m"
RESET = "\033[0;0m"


arquivo = "lista_palavras.txt" 

def le_arquivo(arq):
    """ Lê arquivo especificado e retorna uma lista com todas as linhas """    
    with open(arq, encoding="UTF-8") as f:
        return [linha.strip() for linha in f]

def escolher_palavra():
    # palavras = ["Bacia", "Cadar", "Dente", "Estar", "Falar", "Grito", "Hotel", "Irado", "Jazia", "Karma", "Lazer", "Maçã", "Olhar", "Pular", "Rampa", "Sabor"]
    palavras = le_arquivo(arquivo)
    return random.choice(palavras)

def imprimir_palavra_atual(palavra_atual, letras_corretas_fora_posicao, palavra):
    print(f"Palavra atual: ", end="")

    for i in range(len(palavra_atual)):
        if palavra_atual[i] == palavra[i]:
            print(GREEN + f"{palavra_atual[i]} " + RESET, end="")
        elif palavra_atual[i] in letras_corretas_fora_posicao:
            print(YELLOW + f"{palavra_atual[i]} " + RESET, end="")
        else:
            print(f"{palavra_atual[i]} ", end="")

def jogar_termoo():
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
        print(f"Você perdeu! A palavra era: {palavra}")


jogar_termoo()