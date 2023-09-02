# 2. Crie um jogo da velha NxN em que o usuário deve definir as dimensões do tabuleiro (sempre quadrado).

# O metodo principal (jogar_jogo_da_velha) é responsavel por chamar os demais metodos e controlar o fluxo do jogo. 
# Nele há um loop com condição de parada, que só é quebrado quando o jogo termina, seja por vitoria ou empate. O empata acontece quando o numero de jogadas é igual ao numero de casas do tabuleiro.
#
# O metodo criar_tabuleiro é responsavel por criar o tabuleiro, com base na dimensao informada pelo usuario.
# 
# O metodo imprimir_tabuleiro é responsavel por imprimir o tabuleiro na tela, com as respectivas jogadas.
# 
# O metodo verifica vitoria, recebe o tabuleiro (com o valores preenchidos) e o jogador atual, e verifica se o jogador atual venceu, 
# validando linha, coluna e diagonais com base na dimensao do tabuleiro.


def criar_tabuleiro(dimensao):
  '''Cria um tabuleiro NxN com dimensão informada pelo usuário.'''
  
  tabuleiro = [[" " for _ in range(dimensao)] for _ in range(dimensao)]
  return tabuleiro

def imprimir_tabuleiro(tabuleiro):
  '''Imprime o tabuleiro na tela.'''
    
  dimensao = len(tabuleiro)
  for i in range(dimensao):
      print(" | ".join(tabuleiro[i]))
      if i < dimensao - 1:
          print("-" * (4 * dimensao - 1))

def fazer_jogada(tabuleiro, linha, coluna, jogador):
  '''Faz uma jogada no tabuleiro, se a posição estiver vazia.'''

  if tabuleiro[linha][coluna] == ' ':
      tabuleiro[linha][coluna] = jogador
      return True
  else:
      return False

def verificar_vitoria(tabuleiro, jogador):
  '''Verifica se o jogador (X ou O) venceu o jogo.'''

  dimensao = len(tabuleiro)
  
  # Verificar linhas e colunas
  for i in range(dimensao):
      if all(tabuleiro[i][j] == jogador for j in range(dimensao)) or all(tabuleiro[j][i] == jogador for j in range(dimensao)):
          return True
  
  # Verificar diagonais
  if all(tabuleiro[i][i] == jogador for i in range(dimensao)) or all(tabuleiro[i][dimensao - 1 - i] == jogador for i in range(dimensao)):
      return True
  
  return False

def jogar_jogo_da_velha(dimensao):
  '''Função principal do jogo da velha.''' 
    
    
  tabuleiro = criar_tabuleiro(dimensao)
  jogador_atual = 'X'
  jogadas_restantes = dimensao * dimensao
  
  while jogadas_restantes > 0:
    imprimir_tabuleiro(tabuleiro)
    print(f"Vez do jogador {jogador_atual}")
    
    linha = int(input("Digite a linha da sua jogada (0 a {}): ".format(dimensao - 1)))
    coluna = int(input("Digite a coluna da sua jogada (0 a {}): ".format(dimensao - 1)))

    if 0 <= linha < dimensao and 0 <= coluna < dimensao:
        if fazer_jogada(tabuleiro, linha, coluna, jogador_atual):
            if verificar_vitoria(tabuleiro, jogador_atual):
                imprimir_tabuleiro(tabuleiro)
                print(f"Jogador {jogador_atual} venceu!")
                break
            else:
                jogadas_restantes -= 1
                jogador_atual = 'X' if jogador_atual == 'O' else 'O'
        else:
            print("Essa posição já está ocupada. Tente novamente.")
    else:
        print("Jogada fora do limite do tabuleiro. Tente novamente.")

  if jogadas_restantes == 0:
    imprimir_tabuleiro(tabuleiro)
    print("Empate!")

  
dimensao = int(input("Digite a dimensão do tabuleiro: "))
jogar_jogo_da_velha(dimensao)