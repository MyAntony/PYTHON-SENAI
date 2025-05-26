def adicionar_item():
    codigo = input("Codigo do produto: ")
    descricao = input("Descrição: ")
    fabricante = input("Fabricante: ")
    preco = input("Preço do produto: ")

    with open ("estoque.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{codigo}, {descricao}, {fabricante}, {preco}\n")
    print("Item adicionado com sucesso!")

def listar_estoque():
    with open ("estoque.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            item = linha.strip().split (",")
            print (f" Código: {item[0]}, Descrição: {item[1]}, Fabricante: {item[2]}, Preço: {item[3]} ")

def alterar_item():
    codigo = input("Codigo do produto: ")
    with open ("estoque.txt", "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()
    with open ("estoque.txt", "w") as arquivo:
        for linha in linhas:
            item = linha.strip().split (",")
            if item[0] == codigo:
                print("Digite os novos dados: ")
                novo_codigo = input("Código: ")
                nova_descricao = input("Descrição: ")
                novo_fabricante = input("Fabricante: ")
                novo_preco = input("Preço: ")
                arquivo.write (f"{novo_codigo}, {nova_descricao}, {novo_fabricante}, {novo_preco}\n")
            else:
                arquivo.write(linha)
    print("Item alterado com sucesso!")

def excluir_item():
    codigo = input("Codigo do produto: ")
    with open ("estoque.txt", "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()

    with open ("estoque.txt", "w") as arquivo:
        for linha in linhas:
            item = linha.strip().split (",")
            if item[0] != codigo:
                arquivo.write(linha)
    print("Item removido com sucesso!")