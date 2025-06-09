def criar_produto(nome, codigo, quantidade, preco):
    produto = {"nome": nome, "codigo": codigo, "quantidade": quantidade, "preco": preco}
    return produto

def adicionar_produto(produtos, nome, codigo, quantidade, preco):
    produto = criar_produto(nome, codigo, quantidade, preco)
    produtos.append(produto)
    print(f"Produto {nome} adicionado com sucesso!")
    return produtos

def buscar_produto(produtos, nome):
    encontrados = [produto for produto in produtos if nome.lower() in produto["nome"].lower()]
    if encontrados:
        for produto in encontrados:
            print(f"Produto encontrado: {produto['nome']} | Código: {produto['codigo']} | Estoque: {produto['quantidade']} unidades | Preço: R${produto['preco']},00")
    else:
        print("Produto não encontrado.")

def listar_produtos(produtos):
    if produtos:
        print("Lista de produtos em estoque:")
        for produto in produtos:
            print(f"Nome: {produto['nome']} | Código: {produto['codigo']} | Estoque: {produto['quantidade']} unidades | Preço: R${produto['preco']},00")
    else:
        print("Nenhum produto cadastrado no estoque.")

def atualizar_estoque(produtos, codigo, nova_quantidade):
    for produto in produtos:
        if produto['codigo'] == codigo:
            produto['quantidade'] = nova_quantidade
            print(f"Estoque do produto {produto['nome']} atualizado para {nova_quantidade} unidades.")
            return produtos
    print("Produto não encontrado.")
    return produtos


produtos = []


while True:
    print("\nEscolha uma opção:")
    print("1) Adicionar produto")
    print("2) Buscar produto")
    print("3) Listar produtos")
    print("4) Atualizar estoque")
    print("5) Sair")
    
    opcao = input("Digite sua escolha: ")
    
    if opcao == "1":
        nome = input("Digite o nome do produto: ")
        codigo = input("Digite o código do produto: ")
        quantidade = int(input("Digite a quantidade em estoque: "))
        preco = float(input("Digite o preço do produto: "))
        produtos = adicionar_produto(produtos, nome, codigo, quantidade, preco)
    
    elif opcao == "2":
        nome = input("Digite o nome do produto para buscar: ")
        buscar_produto(produtos, nome)
    
    elif opcao == "3":
        listar_produtos(produtos)
    
    elif opcao == "4":
        codigo = input("Digite o código do produto para atualizar o estoque: ")
        nova_quantidade = int(input("Digite a nova quantidade em estoque: "))
        produtos = atualizar_estoque(produtos, codigo, nova_quantidade)
    
    elif opcao == "5":
        print("Saindo do sistema...")
        break
    
    else:
        print("Opção inválida, tente novamente.")
