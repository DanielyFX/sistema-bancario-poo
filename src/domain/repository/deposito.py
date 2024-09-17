class Deposito:
    def __init__(self, valor: float = 0):
        self._valor = valor

    @property
    def valor(self) -> float:
        return self._valor
    
    @valor.setter
    def valor(self, n: float):
        self._valor = n

    