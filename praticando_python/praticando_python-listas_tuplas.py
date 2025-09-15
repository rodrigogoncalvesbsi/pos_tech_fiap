lista_compras = ['açúcar', 'café', 'arroz']

produto = input('Digite o item que você quer verificar: ')
produto_adicionado = False

for lista in lista_compras:
    if produto == lista:
        print('Produto já adicionado a sua lista de compras!') 
        produto_adicionado = True
        break
    else:
        produto_adicionado = False

if produto_adicionado == False:
    print(f'O item {produto} precisa ser comprado.')


#Com base nisso, desenvolva um programa que receba como entrada uma lista contendo as notas de todos os participantes 
# e exiba, ao final, essa lista ordenada em ordem crescente.

#Exemplo de Entrada:
print('\n\n')
notas = [85, 70, 90, 60, 75]

notas.sort()

print("Notas ordenadas:", notas)

#Uma ONG está organizando uma campanha de arrecadação de alimentos e precisa registrar os nomes dos voluntários 
# que vão ajudar na ação. À medida que os voluntários se inscrevem, seus nomes devem ser adicionados à lista e 
# quando for digitado a palavra sair o programa deve encerrar.
print('\n\n')
voluntarios = []

while True:
    nome = input('Digite o nome do voluntário (ou SAIR para encerrar): ')

    if nome != 'sair':
        voluntarios.append(nome)
    else:
        break

print('Voluntários registrados:', voluntarios)   

#Armano trabalha com a gestão de dois estoques de mercadorias que são representados como tuplas. 
# Agora, ele precisa criar um relatório unificado com os produtos dos dois estoques juntos.
#Para ajudá-lo, como você criaria um programa que ler as informações dos estoques e gera um 
# relatório com todos os produtos juntos?
print('\n\n')
produtos_estoque_01 = ('Arroz', 'Feijão', 'Macarrão')
produtos_estoque_02 = ('Óleo', 'Sal', 'Açúcar')

estoque_total = produtos_estoque_01 + produtos_estoque_02

print('Estoque combinado: ', estoque_total)

#Camila adora receber amigos para jantares temáticos. Para o próximo encontro, ela quer garantir que a 
# ordem de chegada seja respeitada, mas ainda precisa fazer ajustes na lista de convidados. 
# Camila quer adicionar novos nomes e organizá-los em posições específicas.

#Como você criaria um programa que mostre a lista inicial, permita a inserção de um novo nome em uma 
# posição escolhida e exiba a lista atualizada?
print('\n\n')

lista_atual_convidados = ['Ana', 'Pedro', 'Carlos']
nome = input('Digite o nome do novo convidado: ')
posicao = int(input('Digite a posição na qual deseja inserir o convidado: '))

lista_atual_convidados.insert(posicao, nome)

print('Lista atualizada de convidados: ', lista_atual_convidados)

# 09 - A Futuro Eventos, uma empresa especializada em organização de conferências, cometeu um erro ao registrar 
# a sequência dos eventos de uma conferência importante. Os eventos foram registrados na ordem inversa à 
# que deveriam acontecer. Agora, a equipe precisa corrigir a ordem dos eventos para garantir que a conferência 
# aconteça conforme o planejamento original.

#Considerando a lista inicial de eventos, crie um programa que permita ao organizador ordená-los, 
# de forma que a lista final siga a sequência correta.
print('\n\n')

eventos_registrados = ['Encerramento', 'Palestra 3', 'Palestra 2', 'Abertura']
eventos_registrados.reverse()
print('Ordem corrigida: ', eventos_registrados)

# 10 - O clube de atletismo Alura Runners organizou uma corrida e divulgou a lista com a classificação final 
# dos participantes. Mas, um erro foi identificado: um dos nomes está incorreto. 
# O organizador precisa de um programa que permita localizar o nome errado e substituí-lo pelo correto.

#Como você escreveria um programa que solicite o nome errado, o nome correto e atualize a lista exibindo 
# a nova classificação ao final?
print('\n\n')

nome_incorreto = input('Digite o nome incorreto: ')
nome_correto = input('Digite o nome correto: ')

lista_classificacao = ['Ana', 'João', 'Pedro', 'Rodrigo']
posicao = int(0)

for nome in lista_classificacao:
    if nome == nome_incorreto:
        lista_classificacao.remove(nome_incorreto)
        break
        posicao += 1
    else:
        posicao += 1

lista_classificacao.insert(posicao,nome_correto)
print(f'O nome {nome_incorreto} foi substituido por {nome_correto}.')
print('Lista atualizada: ', lista_classificacao)


# 11 - Paulo está criando uma lista de pedidos para a lanchonete. Ele já tem todos os pedidos, 
# mas percebeu que o último foi inserido por engano e precisa removê-lo.

#Diante deste problema, ajude Paulo criando um programa que automatize essa operação, 
# permitindo listar os pedidos e remover o último item automaticamente.
print('\n\n')

pedidos = ['Sanduíche', 'Suco', 'Sobremesa']

pedidos.pop()

print('Pedidos finais: ', pedidos)

# 12 - A professora Helena quer facilitar sua rotina na hora de calcular a média das notas finais da turma. 
# Ela sempre anota as notas dos alunos ao longo do semestre e, no final, precisa de um relatório para saber 
# se a turma está indo bem.

#Para isso, ajude a professora a criar um programa que receba as notas finais de todos os alunos e calcule a média da turma.
print('\n\n')

notas_finais = input("Digite as notas dos alunos separadas por vírgula: ").split(", ")
soma = float(0)
cont = int(0)

for notas in notas_finais:
    soma += float(notas)
    cont += 1
print(f'Média final da turma: {soma / cont}')

#Solução do professor:
# notas = input("Digite as notas dos alunos separadas por vírgula: ").split(", ")
# notas = [float(nota) for nota in notas]
# media = sum(notas) / len(notas)
# print(f"Média final da turma: {media:.2f}")


# 13 - Uma escola está organizando os dados dos alunos para criar um relatório resumido. 
# Cada aluno tem seus dados registrados em uma única entrada, incluindo nome, idade e nota final no semestre. 
# Esses dados devem ser exibidos separadamente para cada aluno no formato abaixo:
# Ajude a escola a desenvolver um programa que registre as informações dos alunos, organize os dados e exiba um relatório detalhado 
# com as informações separadamente.
print('\n\n')
dados = input("Digite os dados do aluno no formato Nome, Idade, Nota separados por vírgula: ").split(", ")

for i in range(0, len(dados), 3):
    nome, idade, nota = dados[i], int(dados[i + 1]), float(dados[i + 2])
    print(f"Aluno: {nome}")
    print(f"Idade: {idade}")
    print(f"Nota: {nota}\n")
