from abc import ABC, abstractmethod


class Pessoa(ABC):
    """Classe abstrata que representa uma pessoa."""

    def __init__(self, nome: str, documento: str):
        self.nome = nome
        self._documento = documento

    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, valor: str) -> None:
        if not valor.strip():
            raise ValueError("O nome não pode estar vazio.")

        self._nome = valor

    @property
    def documento(self) -> str:
        return self._documento

    @abstractmethod
    def apresentar(self) -> str:
        """Retorna uma apresentação da pessoa."""
        pass