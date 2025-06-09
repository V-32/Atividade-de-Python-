def cadastrar_produto():
    # Produto cadastrado fixo para exemplo
    return {"nome": "Arroz", "tipo": "Alimento", "estoque": 10}

def buscar_produto(produto, nome_busca):
    if produto['nome'].lower() == nome_busca.lower():
        print(f"Produto encontrado: {produto['tipo']} ({produto['nome']}) com estoque de {produto['estoque']}")
    else:
        print("Produto não encontrado.")

def atualizar_estoque(produto, quantidade):
    produto['estoque'] += quantidade
    print(f"Estoque atualizado: {produto['estoque']} unidades de {produto['nome']}")

# Cadastro do produto
produto = cadastrar_produto()

# Menu de opções
print("\nEscolha uma opção:")
print("1) Buscar produto")
print("2) Atualizar estoque")
opcao = input("Opção: ")

if opcao == "1":
    nome_busca = input("Digite o nome do produto a ser buscado: ")
    buscar_produto(produto, nome_busca)
elif opcao == "2":
    quantidade = int(input("Digite a quantidade a ser adicionada ao estoque: "))
    atualizar_estoque(produto, quantidade)
else:
    print("Opção inválida, tente novamente.")


