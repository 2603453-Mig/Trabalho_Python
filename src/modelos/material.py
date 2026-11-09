from abc import ABC, abstractmethod
from excecoes import MaterialIndisponivelError


class Material(ABC):
    """Classe base para os materiais da biblioteca."""

    total_criados = 0

    def __init__(self, codigo: str, titulo: str):
        if not self.validar_codigo(codigo):
            raise ValueError("O código não pode estar vazio.")

        self._codigo = codigo.strip()
        self.titulo = titulo
        self._disponivel = True

        Material.total_criados += 1

    @staticmethod
    def validar_codigo(codigo: str) -> bool:
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

        self._titulo = valor.strip()

    @property
    def disponivel(self) -> bool:
        return self._disponivel

    def marcar_emprestado(self) -> None:
        """Marca o material como emprestado."""

        if not self._disponivel:
            from excecoes import MaterialIndisponivelError
            raise MaterialIndisponivelError(
                "Este material já está emprestado."
            )

        self._disponivel = False


    def marcar_disponivel(self) -> None:
        """Marca o material como disponível novamente."""
        self._disponivel = True

    @abstractmethod
    def calcular_prazo_dias(self) -> int:
        pass

    @abstractmethod
    def tipo_material(self) -> str:
        pass