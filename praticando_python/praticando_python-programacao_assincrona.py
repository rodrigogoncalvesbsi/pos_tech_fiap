import asyncio

async def corrotina():
    print('Início.')
    await asyncio.sleep(3)
    print('Fim.')

asyncio.run(corrotina())

# 05 - Alice é uma desenvolvedora que precisa testar uma API de terceiros que tem um tempo de resposta variável. 
# Para simular esse comportamento, ela quer um programa que exiba uma mensagem, aguarde um tempo determinado e 
# depois exiba outra mensagem informando que o tempo acabou.
# Esse programa deve ser assíncrono, permitindo que Alice compreenda melhor como funciona a espera sem bloquear 
# a execução do código.
# Com base nesse cenário, crie um programa que aguarde 3 segundos antes de exibir a mensagem final.

print('\n\n')

async def temporizador():
    print('Iniciando temporizador... ')
    await asyncio.sleep(3)
    print('Tempo finalizado após 3 segundos! ')

asyncio.run(temporizador())

# 06 - Carlos é um engenheiro de software que precisa processar duas tarefas simultaneamente: uma que simula um download 
# e outra que simula uma análise de dados. Ele quer que ambas as tarefas sejam iniciadas ao mesmo tempo, 
# e que o programa exiba mensagens informando o início e o fim de cada uma.
# Com base nesse cenário, crie um programa que inicie ambas as tarefas ao mesmo tempo, e exiba as mensagens quando cada 
# uma for concluída. Dica: Utilize asyncio.gather() para rodar ambas em paralelo.

print('\n\n')


async def baixar_dados(): 
    print("Iniciando download...") 
    await asyncio.sleep(2) 
    print("Download concluído!") 

async def analisar_dados(): 
    print("Iniciando análise de dados...") 
    await asyncio.sleep(3) 
    print("Análise de dados concluída!") 

async def main(): 
    await asyncio.gather(baixar_dados(), analisar_dados()) 

asyncio.run(main())

# 07 - Carlos precisa calcular o fatorial de cinco números diferentes simultaneamente. Como cálculos pesados podem demorar, 
# ele quer garantir que todos sejam processados ao mesmo tempo, e os resultados exibidos assim que estiverem prontos.
# Crie um programa que calcule o fatorial de cinco números diferentes de forma assíncrona, 
# onde os cálculos devem ser realizados paralelamente e exiba os resultados conforme forem concluídos, 
# em ordem de menor número para maior número.

print('\n\n')

async def calcular_fatorial(numero):
    resultado = 1
    for i in range(2, numero + 1):
        resultado *= i
    await asyncio.sleep(numero)
    print(f'Fatorial de {numero} = {resultado}')


async def main():
    numeros = [5, 3, 7, 4, 6]
    await asyncio.gather(
        calcular_fatorial(numeros[0]),
        calcular_fatorial(numeros[1]),
        calcular_fatorial(numeros[2]),
        calcular_fatorial(numeros[3]),
        calcular_fatorial(numeros[4])
    )

asyncio.run(main())

# 08 - Lucas trabalha em um sistema de notificações que precisa enviar mensagens para usuários. No entanto, 
# algumas notificações só devem ser enviadas se o usuário tiver ativado essa opção no sistema. Além disso, 
# se o usuário for VIP, ele deve receber uma notificação prioritária antes das demais.
# Com base nesse cenário, crie um programa que simule o envio de notificações para três usuários. Cada usuário tem um status diferente:
    # Ana: VIP (deve receber uma notificação prioritária antes das normais).
    # João: Usuário comum, mas ativou as notificações.
    # Carla: Usuária comum, mas desativou as notificações (não deve receber nada).
# O programa deve exibir quais notificações foram enviadas e quais usuários não receberam nada.

# Saída esperada:
    # Enviando notificações...
    # Notificação VIP para Ana enviada!
    # Notificação normal para João enviada!
    # Carla desativou as notificações. Nada foi enviado.
    # Todas as notificações foram processadas!

# 09 - Marcos é dono de uma loja online e precisa de um sistema que processe pedidos de forma assíncrona. 
# O sistema deve seguir a seguinte lógica:

    # Primeiro, verificar se o pagamento foi aprovado;
    # Se o pagamento for aprovado, verificar se há estoque disponível;
    # Somente se houver estoque disponível, confirmar o pedido e enviá-lo para entrega;
    # Se o pagamento falhar ou não houver estoque, o pedido deve ser cancelado.

# A lista de pedidos já está definida no sistema, com o status do pagamento e do estoque previamente cadastrados. 
# Confira o código:
    # pedidos = [
    #     {"id": 101, "pagamento_aprovado": True, "estoque_disponivel": True},
    #     {"id": 102, "pagamento_aprovado": True, "estoque_disponivel": False},
    #     {"id": 103, "pagamento_aprovado": False, "estoque_disponivel": True},
    #     {"id": 104, "pagamento_aprovado": True, "estoque_disponivel": True},
    #     {"id": 105, "pagamento_aprovado": False, "estoque_disponivel": False},
    # ]

#O programa deve simular essa lógica para três pedidos, exibindo mensagens conforme o processamento ocorre.
#Saída esperada:
    # Processando pedido #101...
    # Pagamento aprovado para pedido #101.
    # Estoque disponível para pedido #101.
    # Pedido #101 confirmado! Enviado para entrega.
    
    # Processando pedido #102...
    # Pagamento aprovado para pedido #102.
    # Estoque indisponível para pedido #102. Pedido cancelado.
    
    # Processando pedido #103...
    # Pagamento recusado para pedido #103. Pedido cancelado.
    
    # Todos os pedidos foram processados!

