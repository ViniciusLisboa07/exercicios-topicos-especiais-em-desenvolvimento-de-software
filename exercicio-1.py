# 1 Crie uma versão do jogo da velha 4x4. As regras são as mesmas da versão 3x3

# Foi divido o problema em metodos para facilitar a leitura e entendimento do codigo.  O metodo principal (jogar_jogo_da_velha) 
# é responsavel por chamar os demais metodos e controlar o fluxo do jogo. Nele há um loop infinito que só é quebrado quando o jogo
# termina, seja por vitoria ou empate. 
# 
# O metodo imprimir_tabuleiro é responsavel por imprimir o tabuleiro na tela, com as respectivas jogadas.
# 
# O metodo verifica vitoria, recebe o tabuleiro (com o valores preenchidos) e o jogador atual, e verifica se o jogador atual venceu, 
# validando linha, coluna e diagonais.


def imprimir_tabuleiro(tabuleiro):
    '''Imprime o tabuleiro na tela.'''
  
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("--+---+---+--")

def verificar_vitoria(tabuleiro, jogador):
    '''Verifica se o jogador (X ou O) venceu o jogo.'''
  
    # Verifica linhas e colunas
    for i in range(4):
        if all(tabuleiro[i][j] == jogador for j in range(4)) or all(tabuleiro[j][i] == jogador for j in range(4)):
            return True

    # Verifica diagonais
    if all(tabuleiro[i][i] == jogador for i in range(4)) or all(tabuleiro[i][3 - i] == jogador for i in range(4)):
        return True

    return False

def validando_entrada(linha, coluna, tabuleiro):
    '''Verifica se a linha e coluna informadas são válidas.'''
  
    if 0 <= linha <= 3 and 0 <= coluna <= 3 and tabuleiro[linha][coluna] == " ":
        return True
    else:
        return False
    
def jogar_jogo_da_velha():
    '''Função principal do jogo da velha.'''
  
    # Criando o tabuleiro e define o jogador inicial
    tabuleiro = [[" " for _ in range(4)] for _ in range(4)]
    print(tabuleiro)
    # tabuleiro é uma lista de listas, onde cada lista interna representa uma linha do tabuleiro
    
    jogador_atual = "X"
    jogadas = 0

    while True:
        imprimir_tabuleiro(tabuleiro)
        print(f"Jogador {jogador_atual}, é sua vez.")

        linha = int(input("Digite o número da linha (0 a 3): "))
        coluna = int(input("Digite o número da coluna (0 a 3): "))

        if validando_entrada(linha, coluna, tabuleiro):
            tabuleiro[linha][coluna] = jogador_atual
            jogadas += 1

            if verificar_vitoria(tabuleiro, jogador_atual):
                imprimir_tabuleiro(tabuleiro)
                print(f"Jogador {jogador_atual} venceu!")
                break
            elif jogadas == 4 * 4:
                imprimir_tabuleiro(tabuleiro)
                print("O jogo empatou!")
                break

            jogador_atual = "O" if jogador_atual == "X" else "X"
        else:
            print("Movimento inválido. Tente novamente.")


jogar_jogo_da_velha()
