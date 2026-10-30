from abc import ABC, abstractmethod
from interfaces import Identificavel


class Material(ABC):
    """Classe base para os materiais da biblioteca."""

    total_criados = 0

    def __init__(self, codigo: str, titulo: str):
        self._codigo = codigo
        self.titulo = titulo
        self._disponivel = True

        Material.total_criados += 1

    @staticmethod
    def validar_codigo(codigo: str) -> bool:
        """Verifica se o código é válido."""
        return bool(codigo.strip())

    @property
    def identificador(self) -> str:
        return self._codigo

    @property
    def codigo(self) -> str:
        return self._codigo

    @property
    def titulo(self) -> str:
        return self._titulo

    @titulo.setter
    def titulo(self, valor: str) -> None:
        if not valor.strip():
            raise ValueError("O título não pode estar vazio.")

        self._titulo = valor

    @property
    def disponivel(self) -> bool:
        return self._disponivel

    @abstractmethod
    def calcular_prazo_dias(self) -> int:
        """Define o prazo de empréstimo do material."""
        pass

    @abstractmethod
    def tipo_material(self) -> str:
        """Retorna o tipo do material."""
        pass