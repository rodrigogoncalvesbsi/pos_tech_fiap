# 1 - Imprima a frase: Python na Escola de Programação da Alura.
print('Python na Escola de Programação da Alura.\n\n')






#2 - Imprima a frase: Meu nome é {nome} e tenho {idade} anos em que nome e idade precisam ser valores armazenados em variáveis.
nome = 'Rodrigo Gonçalves'
idade = 40

print(f' Meu nome é {nome} e tenho {idade} anos\n\n')

#3 - Imprima a palavra: ‘ALURA’ de modo que cada letra fique em uma linha, como mostrado a seguir:

print('A\nL\nU\nR\nA \n\n\n')

print('A','L','U','R','A',sep='\n') #resposta do professor


# 4 - Imprima a frase: O valor arredondado de pi é: {pi_arredondado} em que o valor de pi precisa ser armazenado em uma variável e 
#     arredondado para apenas duas casas decimais. Para facilitar, utilize:

pi = 3.14159
pi_arredondado = print(round(pi,2))
print(f'O valor arredondado de pi é: {pi:.2f}')