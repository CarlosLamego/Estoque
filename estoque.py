import os.path

#2º. Criei dois vetores vazios para receberem produtos e seus respectivos preços
produtos = []
valores = []


#3º. Início das funções que serão chamadas.
def titulo(mensa, traco=" - "):
    print()
    print(mensa)
    print(traco*40)

def incluir():
    titulo("Cadastrar Produto: ")
    produto = input("Nome do produto: ")
    produtos.append(produto)
    valor = float(input("Valor do Produto: "))
    valores.append(valor)
    print("Ok, produto cadastrado.")

def listar():
    titulo("Listagem dos Produtos: ")
    for g, h in zip(produtos, valores):
        print(f"{g: 20s} {h:5.2f}")

def pesquisar():
    pass

def excluir():
    titulo ("Exlcuir: ")
    print ("Digite o número do item a ser excluído: ")
    for i, produto in enumerate (produtos, star=1):
        print(f"{i}. {produto}")
    exc = input()
    produtos.pop(exc)
    valores.pop(exc)

def alterar():
    titulo("Alterar Preço: ")
    print("Digite o número do item a ter o preço alterado: ")
    for i, produto in enumerate(produtos , start=1):
        print(f"{i}. {produto}")
    alterar = input()
    valor = float(input("Valor do Produto: "))
    valores[alterar]= valor

def resumo():
    pass

def salvar():
    with open("estoque.txt", "w") as arq:
        for produto, valor in zip(produtos, valores):
            arq.write(f"{produtos}; {valores}\n")

def carregar():
    with open("estoque.txt", "r") as arq:
        linhas = arq.read().splitlines()
    
    for linha in linhas:
        partes = linha.split(";")
        produtos.append(partes[0])
        valores.append(float(partes[1]))

if os.path.exists("estoque.txt"):
    carregar()


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

salvar()