#SISTEMA DE ESTOQUE
#Menu principal
import negocios_crud


def menu():
    while True:
        print("\n ---- MENU ESTOQUE ---- ")
        print("1 - Adicionar item: ")
        print("2 - Listar estoque: ")
        print("3 - Alterar item: ")
        print("4 - Excluir item: ")
        print("0 - Sair do Sistema")

        opcao = input ("Digite uma opção: ")
        if opcao == "1":
            negocios_crud.adicionar_item()
        elif (opcao == "2"):
            negocios_crud.listar_estoque()
        elif (opcao == "3"):
            print("Alterar item")
            negocios_crud.alterar_item()
        elif (opcao == "4"):
            print("Excluir item")
            negocios_crud.excluir_item()
        elif (opcao == "0"):
            break
        else:
            print ("Opção Inválida. ")

menu()