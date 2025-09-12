# Como já vimos, programação é prática! Criamos mais uma lista de atividades (não obrigatórias) 
# para você exercitar e reforçar ainda mais seu aprendizado e o conteúdo da vez são listas, 
# blocos de repetição e try except. Bora praticar?

# Exercícios

# 1 - Crie uma lista para cada informação a seguir:

# Lista de números de 1 a 10;
# Lista com quatro nomes;
# Lista com o ano que você nasceu e o ano atual.

numeros = []
tamanho = 10


for i in range(tamanho):
    numeros.append(i+1)

for numero in numeros:
    print(numero)


nomes = []
tamanho = 4

#for i in range(tamanho):
#    nomes.append(input(f"Informe o nome {i}:"))


# 3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.
soma = 0
for numero in numeros:
    if (numero % 2) != 0:
        soma = soma + numero

print(soma) 

#4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.
# Inverte a ordem da lista

# numeros.reverse()
# for numero in numeros:
#     print(numero)

# Começa em 9 (tamanho - 1), vai até -1, e subtrai 1 a cada passo
for i in range(len(numeros) - 1, -1, -1):
    print(numeros[i])

#5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a 
# tabuada desse número, indo de 1 a 10.

numero_tabuada = int(input('\n\nInforme um número:'))
tamanho = 10

for i in range(tamanho):
    print(f'{i+1} x {numero_tabuada} = {(i+1) * numero_tabuada}')


# 6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. 
# Utilize um bloco try-except para lidar com possíveis exceções.

soma = 0
#numeros.append('dois')

for numero in numeros:
    try:
        soma = numero + soma
    except:
        print("Ocorreu um erro insperado!")

print(f'Resultado da soma: {soma}')


#7 - Construa um código que calcule a média dos valores em uma lista. 
# Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.


media = 0 

for numero in numeros:
    media = media + numero
try:
    media = media / (len(numeros) + 1)
except:
    print("Ocorreu um erro insperado!")

print(f'Resultado da média: {media}')


