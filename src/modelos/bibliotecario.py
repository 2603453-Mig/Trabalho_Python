from modelos.pessoa import Pessoa

class Bibliotecario(Pessoa):
    """Representa um funcionário da biblioteca."""

    def __init__(self, nome: str, documento: str, registro: str):
        super().__init__(nome, documento)

        if not registro.strip():
            raise ValueError("O registro não pode estar vazio.")

        self._registro = registro.strip()

    @property
    def registro(self) -> str:
        return self._registro

    @property
    def identificador(self) -> str:
        return self._registro

    def apresentar(self) -> str:
        return f"Bibliotecário: {self.nome} - Registro: {self.registro}"