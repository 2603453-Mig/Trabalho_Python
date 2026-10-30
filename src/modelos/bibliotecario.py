from modelos.pessoa import Pessoa


class Bibliotecario(Pessoa):
    """Representa um funcionário da biblioteca."""

    def __init__(self, nome: str, documento: str, registro: str):
        super().__init__(nome, documento)

        self._registro = registro

    @property
    def registro(self) -> str:
        return self._registro

    def apresentar(self) -> str:
        return f"Bibliotecário: {self.nome} - Registro: {self.registro}"