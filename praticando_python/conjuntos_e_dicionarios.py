# 04 - Ana está organizando uma festa de aniversário e precisa de uma lista de convidados que não tenha repetições , 
# pois algumas pessoas foram convidadas mais de uma vez por engano. Ela gostaria que o programa solicitasse o nome dos convidados e, 
# ao final, exibisse a lista organizada sem repetições.

#Escreva um programa que receba os nomes dos convidados até que o usuário digite 'sair', e ao final mostre a lista de convidados sem repetições.
print('\n\n')
lista_convidados = set()

while True:
    nome_convidado = input('Digite o nome do convidado:')
    if nome_convidado.lower() == 'sair':
        break
    if nome_convidado not in lista_convidados:
        lista_convidados.add(nome_convidado)

print('Convidados confirmados:',lista_convidados)

# 05 - Clara é editora de uma revista e deseja comparar dois artigos para identificar quais palavras aparecem em ambos. 
# Sua tarefa é criar um programa que receba dois textos e exiba o conjunto de palavras comuns entre eles.
print('\n\n')

conjunto_texto01 = set('O sol brilha forte no céu azul'.split())
conjunto_texto02 = set('O céu azul anuncia um dia de sol intenso'.split())

texto_comum = conjunto_texto01.intersection(conjunto_texto02)

print('Palavras em comum: ', texto_comum)

# 06 - Laura e Ana resolveram fazer compras juntas, mas criaram duas listas diferentes. Elas querem um programa que mostre:
    # Quais itens apareceram nas duas listas
    # Quais foram exclusivos de Laura
    # Quais foram exclusivos da Ana
# Escreva um programa que solicite as listas e mostre os resultados dessas comparações.
print('\n\n')

lista_laura = {'leite', 'pão', 'café', 'açúcar'}
lista_ana = {'pão', 'café', 'biscoito', 'chocolate'} 

compras_comuns = lista_ana.intersection(lista_laura)
exclusivos_laura = lista_laura.difference(lista_ana)
exclusivos_ana = lista_ana.difference(lista_laura)

print('Itens em ambas as listas: ', compras_comuns)
print('Itens exclusivos de Laura: ', exclusivos_laura)
print('Itens exclusivos de Ana: ', exclusivos_ana)
print(f"Itens em ambas as listas: {', '.join(compras_comuns)}")  

# 07 - Marina trabalha no setor de segurança de uma empresa e precisa verificar se um determinado conjunto de permissões 
# faz parte das permissões principais de um sistema. Sua tarefa é desenvolver um programa que receba duas listas de permissões 
# e verifique se a segunda lista está contida na primeira.
print('\n\n')

permissoes_principais01 = {'leitura', 'escrita','execução', 'compartilhamento'}
permissoes_solicitadas01 = {'leitura', 'escrita'}

permissoes_principais02 = {'leitura', 'escrita','execução', 'compartilhamento'}
permissoes_solicitadas02 = {'leitura', 'exclusão'}

print('CASO 01')
if permissoes_solicitadas01.issubset(permissoes_principais01):
    print('As permissões solicitadas fazem parte das permissões principais. ')
else:
    print('As permissões solicitadas não fazem parte das permissões principais. ')


print('CASO 02')
if permissoes_solicitadas02.issubset(permissoes_principais02):
    print('As permissões solicitadas fazem parte das permissões principais. ')
else:
    print('As permissões solicitadas não fazem parte das permissões principais. ')


# 08 - Joana é gerente de projetos e precisa consolidar as listas de tarefas de duas equipes distintas. 
# Após unir as listas, ela quer remover uma tarefa específica informada pelo usuário. 
# Sua tarefa é criar um programa que realize essa operação.
print('\n\n')

#equipe_a = set(input('Digite as tarefas da equipe: ').split(','))


equipe_a = {"planejar reunião", "revisar documento", "testar sistema"} 

equipe_b = {"testar sistema", "implementar funcionalidade", "corrigir bug"} 

equipes_a_b = equipe_a.union(equipe_b)

tarefa = input('informe a tarefa que deseja excluir: ')

if tarefa in equipes_a_b:
    equipes_a_b.remove(tarefa)
    print(f'A tarefa {tarefa} foi excluída com sucesso!!')
else:
    print('A tarefa informada não existe.')

print(f'Tarefas finais: {', '.join(equipes_a_b)}')

# 09 - Ana é responsável pelo controle de estoque de uma loja de artigos para papelaria. 
# Ela precisa de um programa que permita cadastrar produtos em forma de dados estruturados. 
# O sistema deve solicitar o nome e a quantidade de três produtos e, ao final, exibir as informações cadastradas em um dicionário, 
# onde cada produto será uma chave e a quantidade correspondente será o valor.
print('\n\n')

produtos = dict()

for i in range(0,1):
    nome_produto = input('Digite o nome do produto: ')
    qtd_produto = int(input('Digite a quantidade: ') )
    produtos[nome_produto] = qtd_produto


print('Dicionário de produtos: ', produtos)


# Ana percebeu que, após o cadastro inicial dos produtos, precisa atualizar a quantidade de um item específico no estoque. 
# Sua tarefa é criar um programa que solicite o nome do produto e a nova quantidade, atualizando essa informação no dicionário de estoque.
print('\n\n')

 
estoque = { 

    "Caderno universitário": 50, 

    "Caneta azul": 120, 

    "Borracha branca": 30 

} 

nome_produto = input('Digite o nome do produto a ser atualizado: ')
qtd_produto = int(input('Digite a nova quantidade: ') )

if nome_produto in estoque:
    estoque[nome_produto] = qtd_produto
else:
    print('O produto digitado não existe.')

print('Estoque: ', estoque)


# 11 - Lucas é voluntário na organização de uma maratona e recebeu a lista de participantes com suas respectivas idades. 
# Agora, ele precisa de um programa que apresente três informações:
    # Os nomes de todos os participantes.
    # As idades de todos os participantes.
    # Uma relação completa com o nome e a idade de cada um.
# Sua tarefa é criar esse programa com base nas informações fornecidas.
print('\n\n')


participantes = { 

    "Mariana": 25, 

    "Carlos": 32, 

    "Beatriz": 28, 

    "Rafael": 35 

} 

print(f"Nomes dos participantes: {', '.join(participantes.keys())}") 
print(f"Idades dos participantes: {', '.join(str(idade) for idade in participantes.values())}") 

print("Participantes e suas idades:")
for nome, idade in participantes.items():
    print(f'- {nome}: {idade} anos')



# 12 - Laura está organizando um workshop sobre tecnologia e precisa de um programa que permita remover participantes que desistiram do evento. 
# O sistema armazena os participantes em um dicionário, onde cada chave é o nome e o valor é um conjunto com os dados do participante. 
# O programa deve solicitar o nome de um participante e remover esse nome da lista de participantes registrados, caso exista.
print('\n\n')


participantes = { 

    "Workshop 1": {"Alice", "Bruno", "Carla", "Diego"}, 

    "Workshop 2": {"Fernanda", "Gustavo", "Helena"} 

} 

nome = input('Nome do participante a ser removido: ')

for workshop, nomes in participantes.items(): 

    nomes.discard(nome) 

print("Lista atualizada de participantes:") 

for workshop, nomes in participantes.items(): 

    print(f"{workshop}: {nomes}") 


# 13 - Nathalia é gerente de uma loja virtual e precisa de um sistema que receba os registros de vendas organizados por categoria de produto. 
# Cada categoria contém uma lista de dicionários representando as vendas individuais, com informações sobre o produto, a quantidade vendida e o 
# valor unitário. Sua tarefa é criar um programa que exiba o total de vendas por categoria.
print('\n\n')


vendas = { 

    "Eletrônicos": [ 

        {"produto": "Smartphone", "quantidade": 5, "valor_unitario": 2000}, 

        {"produto": "Tablet", "quantidade": 3, "valor_unitario": 1500} 

    ], 

    "Eletrodomésticos": [ 

        {"produto": "Geladeira", "quantidade": 2, "valor_unitario": 3000}, 

        {"produto": "Micro-ondas", "quantidade": 4, "valor_unitario": 800} 

    ], 

    "Livros": [ 

        {"produto": "Livro A", "quantidade": 10, "valor_unitario": 50}, 

        {"produto": "Livro B", "quantidade": 5, "valor_unitario": 100} 

    ] 

} 

for categoria, produtos in vendas.items():

    total = 0
    for produto in produtos:
        total += produto['quantidade'] * produto['valor_unitario']

    print(f' - {categoria}: R$ {total:.2f}')




