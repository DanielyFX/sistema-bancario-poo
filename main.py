from src.domain.repository.RepositoryBankManegement import RepositoryBankManegement

from src.utils.menu import Menu

from src.domain.entities.cliente import Cliente
from src.domain.entities.conta import Conta

lista_clientes = []
lista_contas = []
manager = RepositoryBankManegement()

while True:
    Menu.exibir_menu()

    selecao = input("Escolha uma das opções do menu: \n").lower()

    match (selecao):
        case "d":
            numero = int(input("Insiar o número da conta para depositar: \n"))
            conta = manager.get_conta(lista_contas, numero)
            if isinstance(conta, Conta):
                valor = float(input("Insira um valor para depositar: \n"))
                transacao = manager.deposito(conta, valor)
                print(transacao)
            else:
                print(conta)

        case "s":
            numero = int(input("Insiar o número da conta para sacar: \n"))
            conta = manager.get_conta(lista_contas, numero)
            if isinstance(conta, Conta):
                valor = float(input("Insira um valor para sacar: \n"))
                transacao = manager.saque(conta, valor)
                print(transacao)
            else:
                print(conta)

        case "e":
            numero = int(input("Insira o número da conta que deseja consultar o extrato: \n"))
            conta = manager.get_conta(lista_contas, numero)
            if isinstance(conta, Conta):
                manager.extrato(conta)
            else:
                print(conta)

        case "nc":
            manager.exibir_clientes(lista_clientes)
            cpf = input("Insira o cpf do cliente: \n").lower().strip()
            busca_cliente = manager.get_cliente(lista_clientes, cpf)
            if isinstance(busca_cliente, Cliente):
                nova_conta = manager.nova_conta(busca_cliente, len(lista_contas) + 1)
                lista_contas.append(nova_conta)
            else:
                print("Não existe clientes cadastrados com o cpf informado!")

        case "lc":
            manager.get_all_contas(lista_contas)

        case "nu":
            novo_cliente = manager.criar_cliente(lista_clientes)
            if isinstance(novo_cliente, Cliente):
                lista_clientes.append(novo_cliente)
            else:
                print(novo_cliente)

        case "q":
            print("Tenha um ótimo dia!\n")
            break


