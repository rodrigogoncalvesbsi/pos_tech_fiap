

import re
print('\n\n')
titulo_livro = input('Digite o título dos livros:')
letra_inicial = input('Digite a letra inicial para pesquisa:')

resultado = re.findall(rf'\b{letra_inicial}[a-zà-ÿ]*', titulo_livro, re.IGNORECASE)

print(resultado)

