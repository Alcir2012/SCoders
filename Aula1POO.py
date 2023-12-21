class ContaEmBanco:
    def __init__(self):
        self.saldo = 150
    def MostrarSaldo(self):
        return self.saldo
    def DepositarSaldo(self):
        deposit = float(input('Digite quanto você deseja depositar '))
        self.saldo += deposit
        return self.saldo
    def ContasAPagar(self):
        contas = int(input('Insira as contas a pagar '))
        self.saldo -= contas
        if self.saldo < 0:
            return f'Você está com um saldo negativo de: {self.saldo}'
        return self.saldo
    
c1 = ContaEmBanco()
print("Saldo inicial:", c1.MostrarSaldo())  # Mostra o saldo inicial (150 inicialmente)
novo_saldo = c1.DepositarSaldo()  # Pede para depositar um valor e retorna o novo saldo
print("Novo saldo após depósito:", novo_saldo)
saldo_apos_contas = c1.ContasAPagar()  # Deduz o valor das contas a pagar e retorna o saldo final
print(saldo_apos_contas)
