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
