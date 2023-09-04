# 4. Banco de dados de dicionarios. Criar um menu com três opções (1-Cadastrar Usuario, 2-imprimir usuarios, 0-sair).

# Foi criado um loop principal que exibe um menu com três opções: cadastrar usuário, imprimir usuários e sair. 
# Permite-se ao usuário definir quais campos são obrigatórios para o cadastro de usuários.
# Quando o usuário escolhe a opção de imprimir usuários, ele pode selecionar entre diferentes tipos de filtragem. As opções incluem imprimir todos os usuários, imprimir por nome, imprimir por campos e valores, e imprimir por combinações de nome, campos e valores.
# Foram utilizados funções lambda associadas a funções de ordem superior para realizar as filtragens. 
# 
# Caso 1: Não recebe argumentos e imprime todos os usuários. A função lambda apenas formata os usuários para impressão e o map executa a função lambda para cada usuário.
# 
# Caso 2: Recebe nomes para filtrar. A função lambda filtra os usuários que possuem o nome informado e a função map formata os usuários para impressão.
# 
# Caso 3: Recebe campos e valores para filtrar. A função lambda filtra os usuários que possuem os campos e valores informados e a função map formata os usuários para impressão.
# 
# Caso 4: É uma 'junção' de 2 e 3. Recebe nomes, campos e valores para filtrar. Primeiro cria-se a condição atraves da função lambda, apos isso são filtrados os usuarios por nomes e entao por campos e valores. Por fim, a função map formata os usuários para impressão.


def cadastrar_usuario(campos_obrigatorios):
  '''Cadastra um usuário no banco de dados. Preechendo os campos obrigatorios e os opcionais.'''
  
  print("Cadastrando usuario...")
  usuario = {}
  for campo in campos_obrigatorios:
      valor = input(f"Informe o valor para '{campo}': ")
      usuario[campo] = valor
  
  while True:
    campo = input("Desaja cadastrar mais campos? Se sim digite o campo se nao digite sair: ")
    if campo == "sair":
      break 
    valor = input(f"Informe o valor para '{campo}': ")
    usuario[campo] = valor

  return usuario

def imprimir_usuarios(*args, **kwargs):
  '''Imprime os usuários cadastrados no banco de dados, conforme as condições de recebimento de parametros.'''

  print("Imprimindo usuarios...")
  
  print(args, kwargs)
  print("=-=-=-=-")
  
  if len(banco_usuarios) == 0:
    print("Nenhum usuário cadastrado!")
  else:
    
    lista_de_usuarios = list(banco_usuarios.values())

    # Caso que não recebe argumentos
    if not args and not kwargs:
      print("Imprimindo todos os usuários...")
      imprimir_todos = lambda usuario: "\n".join([f"{campo}: {valor}" for campo, valor in usuario.items()])
      usuarios_formatados = map(imprimir_todos, lista_de_usuarios)
      print("\n".join(usuarios_formatados))

    # Caso 2: Recebe nomes para filtrar
    elif args and not kwargs:
      nomes_filtrados = filter(lambda usuario: usuario.get("nome") in args, lista_de_usuarios)
      imprimir_todos = lambda usuario: "\n".join([f"{campo}: {valor}" for campo, valor in usuario.items()])
      usuarios_formatados = map(imprimir_todos, nomes_filtrados)
      print("\n".join(usuarios_formatados))
      
    # Caso 3: Recebe campos e valores para filtrar
    elif kwargs and not args:
      condicao = lambda usuario: all(usuario.get(campo) == valor for campo, valor in kwargs.items())
      usuarios_filtrados = filter(condicao, lista_de_usuarios)
      imprimir_todos = lambda usuario: "\n".join([f"{campo}: {valor}" for campo, valor in usuario.items()])
      usuarios_formatados = map(imprimir_todos, usuarios_filtrados)
      print("\n".join(usuarios_formatados))
      
    # Caso 4: Recebe nomes, campos e valores para filtrar
    elif args and kwargs:
      condicao = lambda usuario: all(usuario.get(campo) == valor for campo, valor in kwargs.items())
      nomes_filtrados = list(filter(lambda usuario: usuario.get("nome") in args, lista_de_usuarios))
      usuarios_filtrados = filter(condicao, nomes_filtrados)
      imprimir_todos = lambda usuario: "\n".join([f"{campo}: {valor}" for campo, valor in usuario.items()])
      usuarios_formatados = map(imprimir_todos, usuarios_filtrados)
      print("\n".join(usuarios_formatados))

def gerenciar_opcao_da_impressao(opcao):
  '''Gerencia a opção escolhida pelo usuário para impressão dos usuários.'''
  
  if opcao == 1:
    imprimir_usuarios()
  elif opcao == 2:
    nomes = input("Digite o(s) nome(s) do(s) usuario(s) separados por virgula: ").split(",")
    imprimir_usuarios(*nomes)
  elif opcao == 3:
    
    campos_valores = {}
    while True:
      print("Digite 'sair' para sair.")
      campo = input("Digite o campo: ")

      if campo == "sair":
        break

      valor = input(f"Digite o valor de {campo}: ")
      campos_valores[campo] = valor
      
    imprimir_usuarios(**campos_valores)
  elif opcao == 4:
    nomes = input("Digite os nomes dos usuarios: ").split(",")

    campos_valores = {}
    while True:
      print("Digite 'sair' para sair.")
      campo = input("Digite o campo: ")

      if campo == "sair":
        break

      valor = input(f"Digite o valor de {campo}: ")
      campos_valores[campo] = valor

    imprimir_usuarios(*nomes, **campos_valores)
  else:
    print("Opção inválida!")


print("Quais campos serão obrigatorios para o cadastro de usuarios?")
campos_obrigatorios = tuple(input("Digite os campos separados por virgula: ").split(","))
print(campos_obrigatorios)
banco_usuarios = {}

while True:
  print("\nMenu:")
  print("1 - Cadastrar Usuario")
  print("2 - Imprimir Usuarios")
  print("0 - Sair")
  
  escolha = int(input("Digite a opção desejada: "))
  
  if escolha == 1:
    usuario = cadastrar_usuario(campos_obrigatorios)
    banco_usuarios[len(banco_usuarios) + 1] = usuario
    print("Usuário cadastrado com sucesso!")
  elif escolha == 2:
    print("Selecione uma opção:")
    
    print("1 - Imprimir todos os usuarios")
    print("2 - Imprimir usuarios por nome")
    print("3 - Imprimir usuarios por campos e valores")
    print("4 - Imprimir usuarios por campos e valores e nomes")
    
    opcao = int(input("Digite a opção desejada: "))
    gerenciar_opcao_da_impressao(opcao)
  elif escolha == 0:
    print("Saindo...")
    break
  else:
    print("Opção inválida!")