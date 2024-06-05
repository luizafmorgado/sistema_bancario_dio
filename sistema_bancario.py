############### VARIAVEIS##################
# Declaração das variáveis globais
opcao = int(input("Olá seja bem-vindo a página do seu banco. Digite 1 para continuar: "))  # Solicita ao usuário para confirmar continuação

menu = """
|1| Depositar
|2| Sacar
|3| Extrato
|4| Sair
"""  # Menu de opções disponíveis para o usuário

saldo = 0  # Saldo inicial do usuário
limite = 500  # Limite de saque diário
extrato = ""  # Histórico de transações
numero_saques = 0  # Contador de saques realizados
LIMITE_SAQUES = 3  # Máximo de saques permitidos por dia

############### LOOP PRINCIPAL ################
# Loop infinito para manter o programa rodando até que o usuário escolha sair
while True: 
    print(menu)  # Exibe o menu de opções
    escolha = input()  # Lê a escolha do usuário

    # Verifica se o usuário digitou 1 para confirmar a continuação
    if opcao!= 1:
        print("Erro Operação inválida, tente novamente.")  # Mensagem de erro se a confirmação não for dada
        continue  # Pula para a próxima iteração do loop

    ############### DEPÓSITO ################
    # Processamento da opção de depósito
    if escolha == "1":
        valor = float(input("Digite o valor para ser depósitado: "))  # Solicita o valor a ser depositado
        if valor > 0:  # Verifica se o valor é positivo
            saldo += valor  # Atualiza o saldo com o valor depositado
            extrato += f"Depósito: R$ {valor:.2f}\n"  # Atualiza o histórico de transações
        else: 
            print("Erro. Valor informado é inválido!")  # Mensagem de erro se o valor não for válido
    
    ############### SAQUE ################
    # Processamento da opção de saque
    elif escolha == "2":
        valor = float(input("Digite o valor do saque: "))  # Solicita o valor a ser sacado
        sem_saldo = valor > saldo  # Verifica se o saldo é suficiente
        excedeu_limite = valor > limite  # Verifica se o saque excede o limite diário
        excedeu_saque = numero_saques >= LIMITE_SAQUES  # Verifica se o limite de saques diários foi atingido

        # Mensagens de erro específicas para diferentes condições de falha
        if sem_saldo:
            print("Operação falhou por saldo insuficiente!")
        elif excedeu_limite:
            print("Operação falhou pois valor de saque excedeu limite! Informe um valor menor de R$500,00 ")
        elif excedeu_saque:
            print("Operação falhou pois número máximo de saques diários foram ultrapassados!")
        elif valor > 0:  # Se todas as condições anteriores forem falsas
            saldo -= valor  # Subtrai o valor do saque do saldo
            extrato += f"Saque: R$ {valor:.2f}\n"  # Atualiza o histórico de transações
            numero_saques += 1  # Incrementa o contador de saques
        else: 
            print("Erro Valor informado é inválido.")
    
    ############### EXTRATO ################
    # Processamento da opção de visualizar o extrato
    elif escolha == "3":
        print("Não foram realizados movimentações." if not extrato else extrato)  # Exibe o histórico de transações
        print(f"\nSaldo: R$ {saldo:.2f}")  # Exibe o saldo atualizado
    
    ############### SAIR ################
    # Processamento da opção de sair
    elif escolha == "4":
        print("Saindo do programa")  # Mensagem indicando que o usuário está saindo
        break  # Encerra o loop e, consequentemente, o programa
    else: 
        print("Erro Opção inválida, tente novamente.")  # Mensagem de erro para opções desconhecidas
