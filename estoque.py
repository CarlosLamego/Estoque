import os.path

produtos = []
valores = []

def titulo(mensa, traco=" - "):
    print()
    print(mensa)
    print(traco*40)

def incluir()
    titulo("Cadastrar Produto: ")
    produto = input("Nome do produto: ")
    produtos.append(produto)
    valor = float(input("Valor do Produto: "))
    valores.append(valor)
    print("Ok, produto cadastrado.")



# 1º. Adicionei o que eu quero do meu estoque:
while True:
    titulo("Cadastrar Produto: ", "=")
    print("1. Incluir Pordutos")
    print("2. Listar Pordutos")
    print("3. Pesquisar")
    print("4. Excluir")
    print("5. Alterar Preço")
    print("6. Resumo")
    print("7. Finalizar")
    opcao = int(input("Opção: "))
    if opcao == 1:
        incluir()
    elif opcao == 2:
        listar()
    elif opcao == 3:
        pesquisar()
    elif opcao == 4:
        excluir()
    elif opcao == 5:
        alterar()
    elif opcao == 6:
        resumo()
    else:
        break
