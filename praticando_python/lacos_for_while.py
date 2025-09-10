clientes = ["João", "Maria", "Carlos", "Ana", "Beatriz"]

for cliente in clientes:
    print(cliente)
    print()


#O que é um loop infinito?
#André está testando um novo recurso no backend do Buscante que processa dados em um loop. 
# Durante os testes, ele percebeu que o sistema parou de responder, e suspeita que o problema está em um loop infinito.

#contador = 0

#while contador < 10:
#    print("Processando dados...")

#O problema desse loop while é que o contador não está sendo incrementado.



for numero in range(5):
    print("Bem-vindo ao Buscante!\n")

print("\n\n\n")

valores = [10, 20, 30, 40, 50]
soma = 0

for valor in valores:
    soma += valor

print(f"A soma total das receitas é: {soma}\n\n\n")


#Organizando seu portfólio
#Crie um programa que ajude Ana a percorrer a lista de projetos e exiba os nomes dos projetos válidos. 
# Se encontrar um item None, o programa deve exibir a mensagem: "Projeto ausente".


projetos = ["website", "jogo", "análise de dados", None, "aplicativo móvel"]

for projeto in projetos:
    if projeto == None:
        print("Projeto ausente.")
        continue
    print(f"{projeto}")



# 09 Entendendo o uso do break
#Ajude José a criar um programa que percorra a lista e exiba a mensagem "Livro encontrado: <nome do livro>" assim que o livro "O Hobbit" for encontrado. 
# Após encontrar o livro, o programa deve parar imediatamente a busca, sem verificar os livros restantes.
print("\n\n\n")

livros = ["1984", "Dom Casmurro", "O Pequeno Príncipe", "O Hobbit", "Orgulho e Preconceito"]

for livro in livros:
    if livro == "O Hobbit":
        print(f"Livro encontrado: {livro}.")
        break


# 10 Controle de estoque
#Crie um programa que simule as vendas de um livro com o estoque inicial de 5 exemplares. 
# O programa deve exibir a mensagem "Venda realizada! Estoque restante: <quantidade>" a cada venda e, ao final, exibir a mensagem "Estoque esgotado".
print("\n\n\n")
exemplares = 5

while exemplares > 0:
    print(f"Venda realizada! Estoque restante: {exemplares}")
    exemplares -= 1

print("Estoque esgotado.")


# 11 Contagem Regressiva
# Aline está implementando uma funcionalidade que exibe mensagens personalizadas para os clientes durante uma promoção especial da sua nova loja de livros. 
# O sistema deve exibir uma mensagem de contagem regressiva personalizada para cada número de 10 até 1, e ao final exibir a mensagem: "Aproveite a promoção agora!".
    # Para números pares, exiba: "Faltam apenas <número> segundos - Não perca essa oportunidade!".
    # Para números ímpares, exiba: "A contagem continua: <número> segundos restantes.".
    # Ao final da contagem, exiba a mensagem: "Aproveite a promoção agora!".
print("\n\n\n")

for i in range(10, 0, -1):
    if i % 2 == 0:
        print(f"Faltam apenas {i} segundos - Não perca essa oportunidade!")
    else:
        print(f"A contagem continua: {i} segundos restantes.")
print("Aproveite a promoção agora!")



# 12 Utilidade do continue em laços
# Ana está implementando um sistema de filtragem de livros no Buscante. A funcionalidade deve percorrer uma lista de livros e exibir o nome de cada livro 
# disponível em estoque. No entanto, se o livro estiver esgotado, ele deve ser ignorado durante a iteração.
print("\n\n\n")

livros = [
    {"nome": "1984", "estoque": 5},
    {"nome": "Dom Casmurro", "estoque": 0},
    {"nome": "O Pequeno Príncipe", "estoque": 3},
    {"nome": "O Hobbit", "estoque": 0},
    {"nome": "Orgulho e Preconceito", "estoque": 2}
]

for livro in livros:
    if livro["estoque"] > 0:
        print(f"Livro disponível: {livro["nome"]}")


# 13 Validação de entrada para login
# João está desenvolvendo um sistema de cadastro para um site de leitura. Ele precisa garantir que os usuários insiram um nome de usuário e uma senha válidos. 
# As regras são as seguintes:
    # O nome de usuário deve ter pelo menos 5 caracteres.
    # A senha deve ter pelo menos 8 caracteres.
    # João quer que o sistema continue solicitando as informações até que ambas as condições sejam atendidas. 
    # Quando o usuário insere dados válidos, o programa deve exibir a mensagem: "Cadastro realizado com sucesso!".
print("\n\n\n")

nome = "null"
senha = "null"

while len(nome) < 5 or len(senha) < 8:
    nome = input("Digite seu nome de usuário: ")
    senha = input("Digite sua senha: ")
print("\n\nCadastro realizado com sucesso!")

#Lógica do professor:
while True:
    nome_usuario = input("Digite seu nome de usuário: ")
    senha = input("Digite sua senha: ")

    if len(nome_usuario) < 5:
        print("O nome de usuário deve ter pelo menos 5 caracteres.")
        continue

    if len(senha) < 8:
        print("A senha deve ter pelo menos 8 caracteres.")
        continue

    print("Cadastro realizado com sucesso!")
    break





