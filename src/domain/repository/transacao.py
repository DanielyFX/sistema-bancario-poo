from abc import ABC, abstractmethod
from src.domain.entities.conta import Conta
from src.domain.repository.deposito import Deposito
from src.domain.repository.saque import Saque

#class Trasacao(ABC, Saque, Deposito):

#    @abstractmethod
#    def registrar(conta: Conta):
#        pass


#if __name__ == "__main__":
#    transacao = Trasacao()
#    print(transacao.Saque.__class__.__name__)