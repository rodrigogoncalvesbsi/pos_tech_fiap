import os

restaurantes = [{'nome':'Praça', 'categoria':'Japonesa', 'ativo': False},
                {'nome':'Pizza Suprema', 'categoria':'Pizza', 'ativo': True},
                {'nome':'Cantina', 'categoria':'Italiana', 'ativo': False}]


def exibir_nome_programa():
    '''Essa função exibe o titulo do programa.'''
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░""")

def exibir_opcoes():
    '''Essa função exibe as opções disponíveis no menu do programa.'''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alterar estado do restaurante')
    print('4. Sair \n')
    

def finalizar_app():
    '''Essa função finaliza o app'''
    exibir_subtitulo("Finalizando o app.")

def voltar_menu_principal():
    input("\n Digite uma tecla para voltar ao menu principal: ")
    main()

def opcao_invalida():
    print("Opção inválida!\n")
    voltar_menu_principal()

def exibir_subtitulo(texto):
    os.system("cls")
    linha = '*' * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print() 

def cadastrar_restaurante():
    '''Essa função é responsável por cadastrar um novo restaurante.
    
    Input:
       - nome do restaurante
       - categoria do restaurante

    Output:
       - adiciona um novo restaurante a lista de restaurantes
    '''

    exibir_subtitulo("Cadastro de novos restaurantes.")
    nome_restaurante = input("Digite o nome do restaurante que deseja cadastrar:")
    categoria = input(f"Digite a categoria do restaurante {nome_restaurante}:")

    dados_restaurante = {'nome': nome_restaurante, 'categoria':categoria, 'ativo': False}

    restaurantes.append(dados_restaurante)
    print(f"\n O restaurante {nome_restaurante} foi cadastrado com sucesso!\n\n")
    voltar_menu_principal()

def listar_restaurantes():
    '''Essa funçõa é responsálvel por listar todos os restaurantes cadastrados.'''
    exibir_subtitulo("Listando os restaurantes:")
    print(f'{'Nome restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Estatus')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = restaurante['ativo']
        
        print(f"- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}")

    voltar_menu_principal()

def alternar_estado_restaurante():
    '''Essa função é responsável por mudar o status do restaurante, ativo ou inativo'''

    exibir_subtitulo("Alterando estado do restaurante")
    nome_restaurante = input("Digite o nome do restaurante que deseja alterar o estado: ")
    restaurante_encontrado = False
    
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)

    if not restaurante_encontrado:
        print('O restaurante não foi encontrado!')

    voltar_menu_principal()


def escolher_opcao():
    '''Essa função é responsável por escolher uma opção do menu e direcionar para a função correspondente a escolha.'''   
    try:
        opcao_escolhida = int(input('Escolha uma opção: \n'))

        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
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