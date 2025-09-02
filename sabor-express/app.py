import os

restaurantes = ['Pizza','Sushi']

def exibir_nome_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░""")

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair \n')
    

def finalizar_app():
    exibir_subtitulo("Finalizando o app.")

def voltar_menu_principal():
    input("\n Digite uma tecla para voltar ao menu principal: ")
    main()

def opcao_invalida():
    print("Opção inválida!\n")
    voltar_menu_principal()

def exibir_subtitulo(texto):
    os.system("cls")
    print(texto)
    print()

    

def cadastrar_restaurante():
    exibir_subtitulo("Cadastro de novos restaurantes.")
    nome_restaurante = input("Digite o nome do restaurante que deseja cadastrar:")
    restaurantes.append(nome_restaurante)
    print(f"\n O restaurante {nome_restaurante} foi cadastrado com sucesso!\n\n")
    voltar_menu_principal()

def listar_restaurantes():
    exibir_subtitulo("Listando os restaurantes:")
    
    for restaurante in restaurantes:
        print(f". {restaurante}")

    voltar_menu_principal()
    

def escolher_opcao():   
    try:
        opcao_escolhida = int(input('Escolha uma opção: \n'))

        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            print("Ativar restaurante.")
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()


def main():
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()