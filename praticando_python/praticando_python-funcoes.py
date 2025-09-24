def ola_mundo(nome):
    return f'Olá, {nome}!'


#nome = input('informe seu nome:')
#print(ola_mundo(nome))


# 04 - Julia é professora e precisa de um programa para ajudar seus alunos a calcularem suas idades 
# com base no ano de nascimento. Sua tarefa é criar uma função que receba o ano de nascimento e o ano 
# atual e retorne à idade correspondente.

def idade(ano, ano_atual):
    return ano_atual - ano


ano_nascimento = int(input('Digite o ano de nascimento: '))
ano_atual = int(input('Digite o ano atual: '))

print('A idade é: ', idade(ano_nascimento, ano_atual))

# 05 - Sara está participando de um concurso de escrita, e uma das regras exige que cada palavra de seu texto tenha 
# um limite máximo de caracteres.
# Ajude Sara criando uma função que receba uma palavra e exiba a quantidade de caracteres.

def contar_caracteres(palavra):
    return len(palavra)

palavra = input('Digite uma palavra: ')

print(f'Essa palavra tem {contar_caracteres(palavra)} caracteres.')

# 06 - Beatriz está desenvolvendo um sistema de atendimento para um site de serviços. 
# Ela deseja criar um programa que exiba uma saudação personalizada dependendo da hora do 
# dia que o usuário acessa a plataforma. O sistema deverá ter a seguinte regra:
    # Se for antes das 12h, exibir "Bom dia";
    # Entre 12h e 18h, exibir "Boa tarde";
    # Após 18h, exibir "Boa noite".
print('\n\n')
def saudacao(hora):
    if 0 <= hora < 12:
        resposta = 'Bom dia'
    elif 12 <= hora < 18:
        resposta = 'Boa tarde'
    else:
        resposta = 'Boa noite'
    
    return resposta

hora_atual = int(input('Digite a hora atual (0-23): '))

print(saudacao(hora_atual))

# 07 - Pedro está criando um sistema de cadastro de produtos para sua loja e percebeu que todos 
# os números de telefone dos clientes estão armazenados como strings. No entanto, para facilitar 
# buscas e validações, ele precisa que esses números sejam tratados como inteiros.

#Dado o seguinte código com uma lista de números de telefone armazenados incorretamente como str, 
# faça duas funções, uma que converte os tipos para inteiro e outra que verifica se a conversão foi 
# feita corretamente e todos os números de telefone são inteiros:


telefones = ["11987654321", "21912345678", "31987654321", "11911223344"] 

def converte_inteiros():
    i = int(0)
    for tel in telefones:
        telefones[i] = int(tel)
        i += 1

def valida_conversao():
    for tel in telefones:
        if isinstance(tel, int) == False:
            return 'Os números não foram convertidos corretamente.'
    return 'Todos os números foram convertidos corretamente!'

converte_inteiros()
print(telefones)
print(valida_conversao())


# 08 - Carlos trabalha em um comércio e precisa saber o valor total de vendas realizadas no dia. 
# As vendas são informadas em uma única linha separadas por espaços.
# Sua tarefa é criar um programa que receba essa linha, converta os valores para números e exiba o total.
print('\n\n')

def converter_valores(lista):  
   return [int(valor) for valor in lista] 

valores = input('Digite os valores das vendas: ').split(' ')

valores_convertidos = converter_valores(valores)
print(f'O total de vendas foi: {sum(valores_convertidos)}')


# 09 - Lucas está desenvolvendo um sistema para gerar relatórios financeiros e precisa filtrar apenas os 
# valores pares de uma lista de números informada pelo usuário.
# Crie um programa que receba uma lista de números e exiba apenas os pares usando a função filter().
print('\n\n')

lista = input('Digite os números separados por espaço: ').split()

lista_convertida = converter_valores(lista)
pares = list(filter(lambda x: x % 2 == 0, lista_convertida))
print("Números pares:", pares)