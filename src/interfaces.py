from typing import Protocol


class Identificavel(Protocol):
    """Define o contrato de objetos que possuem identificador."""

    @property
    def identificador(self) -> str:
        """Retorna o identificador do objeto."""