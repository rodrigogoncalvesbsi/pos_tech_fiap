# 1 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.

pessoa = {'nome':'rodrigo','idade':40,'cidade':'Aguas claras'}
          


# 2 - Utilizando o dicionário criado no item 1:
# Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
# Adicione um campo de profissão para essa pessoa;
# Remova um item do dicionário.

pessoa['idade'] = 41
pessoa['profissao'] = 'Engenheiro'
print(pessoa)

del pessoa['cidade']

print(pessoa)

#4 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.
pessoas = [{'nome':'rodrigo','idade':40,'cidade':'Aguas claras'},
          {'nome':'araujo','idade':41,'cidade':'brasília'}]

for pes in pessoas:
    if pes['nome'] == 'rodrigo':
        print('chave encontrada!')

#5 - Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.
