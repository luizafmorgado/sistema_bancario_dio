from abc import ABC, abstractclassmethod, abstractproperty  # Importação das classes ABC, abstractclassmethod e abstractproperty do módulo abc
from datetime import datetime  # Importação da classe datetime do módulo datetime

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco  # Atributo que armazena o endereço do cliente
        self.contas = []  # Lista que armazena as contas associadas ao cliente

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)  # Método para realizar uma transação em uma conta

    def adicionar_conta(self, conta):
        self.contas.append(conta)  # Método para adicionar uma conta à lista de contas do cliente

class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome  # Atributo que armazena o nome da pessoa física
        self.data_nascimento = data_nascimento  # Atributo que armazena a data de nascimento da pessoa física
        self.cpf = cpf  # Atributo que armazena o CPF da pessoa física

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0  # Saldo inicial da conta (privado)
        self._numero = numero  # Número da conta (privado)
        self._agencia = "0001"  # Agência da conta (privado)
        self._cliente = cliente  # Cliente associado à conta (privado)
        self._historico = Historico()  # Instância do histórico de transações associado à conta

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)  # Método de classe para criar uma nova conta

    @property
    def saldo(self):
        return self._saldo  # Propriedade que retorna o saldo da conta

    @property
    def numero(self):
        return self._numero  # Propriedade que retorna o número da conta

    @property
    def agencia(self):
        return self._agencia  # Propriedade que retorna a agência da conta

    @property
    def cliente(self):
        return self._cliente  # Propriedade que retorna o cliente associado à conta

    @property
    def historico(self):
        return self._historico  # Propriedade que retorna o histórico de transações da conta

    def sacar(self, valor):
        saldo = self.saldo  # Obtém o saldo atual da conta
        excedeu_saldo = valor > saldo  # Verifica se o valor do saque excede o saldo disponível

        if excedeu_saldo:
            print("\n Erro na operação. Saldo insuficiente.")  # Mensagem de falha se não houver saldo suficiente
        elif valor > 0:
            self._saldo -= valor  # Deduz o valor do saque do saldo da conta
            print("\n Saque realizado com sucesso!")  # Mensagem de sucesso ao realizar o saque
            return True
        else:
            print("\n Erro na operação falhou! Por favir digite um valor válido. ")  # Mensagem de falha se o valor do saque for inválido
        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor  # Adiciona o valor do depósito ao saldo da conta
            print("\n Depósito realizado com sucesso!")  # Mensagem de sucesso ao realizar o depósito
        else:
            print("\n Erro na operação falhou! Por favir digite um valor válido.")  # Mensagem de falha se o valor do depósito for inválido
            return False
        return True

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite  # Limite de crédito da conta corrente
        self.limite_saques = limite_saques  # Número máximo de saques permitidos

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
        )  # Calcula o número de saques já realizados

        excedeu_limite = valor > self.limite  # Verifica se o valor do saque excede o limite de crédito
        excedeu_saques = numero_saques >= self.limite_saques  # Verifica se o número de saques excede o limite permitido

        if excedeu_limite:
            print("\n Erro na operação! O valor do saque excede o limite permitido. ")  # Mensagem de falha se o saque exceder o limite
        elif excedeu_saques:
            print("\n Erro na operação! Número máximo de saques diários foi excedido. ")  # Mensagem de falha se o número de saques exceder o limite
        else:
            return super().sacar(valor)  # Chama o método sacar da classe base
        return False

    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """  # Representação textual da conta corrente

class Historico:
    def __init__(self):
        self._transacoes = []  # Lista que armazena as transações da conta

    @property
    def transacoes(self):
        return self._transacoes  # Propriedade que retorna as transações da conta

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,  # Tipo da transação (Saque ou Depósito)
                "valor": transacao.valor,  # Valor da transação
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%s"),  # Data e hora da transação
            }
        )  # Adiciona uma nova transação ao histórico

class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass  # Propriedade abstrata para o valor da transação

    @abstractclassmethod
    def registrar(self, conta):
        pass  # Método abstrato para registrar a transação na conta

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor  # Valor do saque

    @property
    def valor(self):
        return self._valor  # Retorna o valor do saque

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)  # Realiza o saque na conta
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)  # Adiciona o saque ao histórico da conta

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor  # Valor do depósito

    @property
    def valor(self):
        return self._valor  # Retorna o valor do depósito

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)  # Realiza o depósito na conta
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)  # Adiciona o depósito ao histórico da conta
