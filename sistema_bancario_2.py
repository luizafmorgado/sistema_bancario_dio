# Função para exibir o menu principal ao usuário
def menu():
    # Retorna a entrada do usuário após exibir o menu
    return input("""\n
    ------------ MENU ------------
    |1|\tDepositar
    |2|\tSacar
    |3|\tExtrato
    |4|\tNova conta
    |5|\tListar contas
    |6|\tNovo usuário
    |0|\tSair
        """)
    
    return input(menu)


# Função para realizar um depósito
def depositar(saldo, valor, extrato, /):
    # Verifica se o valor é positivo
    if valor > 0:
        # Atualiza o saldo e o extrato
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n Valor informado foi depositado ")
    else:
        # Informa ao usuário sobre erro de valor
        print("\n Erro. Valor informado é inválido!")

    # Retorna o novo saldo e o extrato atualizado
    return saldo, extrato

# Função para realizar um saque
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    # Verifica condições de saque
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    # Trata erros específicos
    if excedeu_saldo:
        print("\n Operação falhou por saldo insuficiente.")

    elif excedeu_limite:
        print("\n Operação falhou pois valor de saque excedeu limite! Informe um valor menor de R$500,00")

    elif excedeu_saques:
        print("\n Operação falhou pois número máximo de saques diários foram ultrapassados!")

    # Realiza o saque se todas as condições forem atendidas
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n Saque realizado com sucesso! ")

    else:
        # Informa ao usuário sobre erro de valor
        print(" Erro. Valor informado é inválido! ")

    # Retorna o novo saldo e o extrato atualizado
    return saldo, extrato

# Função para exibir o extrato do usuário
def exibir_extrato(saldo, /, *, extrato):
    # Exibe o extrato e o saldo atualizado
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")

# Função para criar um novo usuário
def criar_usuario(usuarios):
    # Solicita dados do usuário
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    # Verifica se o CPF já existe
    if usuario:
        print ("\n Já existe usuário com esse CPF ")
        return

    # Solicita informações adicionais e cria o usuário
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print(" Usuário criado com sucesso ")

# Função para filtrar um usuário pelo CPF
def filtrar_usuario(cpf, usuarios):
    # Retorna o usuário com o CPF especificado ou None se não encontrar
    return next((usuario for usuario in usuarios if usuario["cpf"] == cpf), None)

# Função para criar uma nova conta
def criar_conta(agencia, numero_conta, usuarios):
    # Solicita o CPF do usuário
    cpf = input("Informe o CPF: ")
    usuario = filtrar_usuario(cpf, usuarios)

    # Verifica se o usuário existe
    if usuario:
        # Retorna os detalhes da conta criada
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print("\n Usuário não encontrado ")

# Função para listar todas as contas
def listar_contas(contas):
    # Exibe detalhes de cada conta
    for conta in contas:
        print("=" * 100)
        print(f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}""", end="\n\n")

# Função principal que executa o programa
def main():
    # Configurações iniciais
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    # Loop principal do programa
    while True:
        opcao = menu()

        # Processamento das opções do menu
        if opcao == "1":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "2":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)

        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "4":
            criar_usuario(usuarios)

        elif opcao == "5":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == "6":
            listar_contas(contas)

        elif opcao == "0":
            break

        else:
            print("Operação inválida, por favor tente novamente! ")

# Chamada da função principal para iniciar o programa
if __name__ == "__main__":
    main()