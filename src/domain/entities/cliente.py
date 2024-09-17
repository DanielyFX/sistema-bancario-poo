from src.domain.repository.transacao import Transacao
from src.domain.entities.conta import Conta


class Cliente:
    def __init__(self, endereco: str, contas: list):
        self._endereco: endereco
        self._contas: contas

    @property
    def endereco(self) -> str:
        return self._endereco
    
    @endereco.setter
    def endereco(self, valor: str):
        self._endereco = valor

    @property
    def contas(self) -> list:
        return self._contas
    
    @contas.setter
    def contas(self, valor: list):
        self._contas = valor

    def realizar_transacao(conta: Conta, transacao: Transacao):
        match (transacao.Saque.__class__.__name__):
            case "Saque":
                pass