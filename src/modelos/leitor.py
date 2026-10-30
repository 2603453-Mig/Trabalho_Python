from modelos.pessoa import Pessoa
from interfaces import Identificavel


class Leitor(Pessoa):
    """Representa um leitor da biblioteca."""

    LIMITE_EMPRESTIMOS = 5

    def __init__(self, nome: str, documento: str, matricula: str):
        super().__init__(nome, documento)

        self._matricula = matricula
        self._emprestimos = []

    @property
    def identificador(self) -> str:
        return self._matricula

    @property
    def matricula(self) -> str:
        return self._matricula

    def apresentar(self) -> str:
        return f"Leitor: {self.nome} - Matrícula: {self.matricula}"