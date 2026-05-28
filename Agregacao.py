# realizando agregaçao
from Cliente import Cliente
from ContaClienteExtrato import Conta

cliente1 = Cliente(123, "Adriano", "Rua 1")
cliente2 = Cliente(456, "Emile", "Rua 2")
# Criando uma conta com dois clientes, fazendo a agregacao com uma lista
conta1 = Conta([cliente1, cliente2], 1, 0)


conta1.depositar(1000)
conta1.sacar(500)
conta1.extrato.extrato(conta1.numero)
