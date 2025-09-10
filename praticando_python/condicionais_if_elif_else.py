maca = input("Informe a quantidade de maçãs: \n")
banana = input("Informe a quantidade de bananas:")

if maca == banana:
    print("deu empate")
elif maca > banana:
    print("As maçãs tiveram mais vendas.")
else:
    print("As bananas tiveram mais vendas.")


a = int(input("\n\n\ninfrome os dias para a atividade A: \n"))
b = int(input("infrome os dias para a atividade B: \n"))
c = int(input("infrome os dias para a atividade C: \n"))

if a < 0 or b < 0 or c < 0:
    print("Os dias não podem ser negativos.")
else:
    print(f"O tempo total do projeto é: {a + b + c}")



temperatura_atual = int(input("\n\n\nInforme a temperatura atual: "))

if temperatura_atual > 25:
    print("Alerta! temperatura acima do limite permitido.")



peso = float(input("\n\n\nInforme o peso: "))
altura = float(input("Informe a altura: "))

imc = peso / (altura ** 2)
print(f"seu IMC é: {imc:.2f}")
if imc < 18.5:
    print("Você está abaixo do peso.")
elif 18.5 <= imc < 25:
    print("Peso normal.")
else:
    print("Você está acima do peso.")



total_despesas = float(input("\n\n\nInforme o total de despesas do mês: "))

if total_despesas > 3000:
    print("Atenção! Você ultrapassou o limite do orçamento.")
else:
    print("Seus gastos estão dentro do orçamento para o mês.")



hora_atual = float(input("\n\n\nInforme a hora atual:"))

if 8.0 <= hora_atual < 18.0:
    print("Acesso permitido")
else:
    print("Acesso negado")




nota01 = float(input("\n\n\nDigite a primeira nota: "))
nota02 = float(input("Digite a segunda nota: "))
nota03 = float(input("Digite a tereira nota: "))

media_final = (nota01 + nota02 + nota03)/3
print(f"Média: {media_final:.2f}")

if media_final >= 7:
    print("Você está Aprovado.")
elif 5 <= media_final < 7:
    print("Você está de Recuperação.")
else:
    print("Você está Reprovado.")



distancia = int(input("Digite a distância percorrida (em km):"))


if distancia <= 100:
    print("Valor do pedágio: R$ 10,00")
elif 100 < distancia <= 200:
    print("Valor do pedágio: R$ 20,00")
else:
    print("Valor do pedágio: R$ 30,00")



numero = int(input("\n\n\nDigite um número inteiro: "))

if (numero % 2) == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")




renda_mensal = float(input("Digite o valor da sua renda mensal:"))
parcela = float(input("Digite o valor da parcela desejada: "))

if renda_mensal < 2000.0:
    print("Empréstimo negado: renda menor que o previsto.")
elif parcela > (renda_mensal * 0.3):
    print("Empréstimo negado: parcela acima de 30% da renda.")
else:
    print("Empréstimo Aprovado.")