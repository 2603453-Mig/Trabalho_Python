from datetime import date, timedelta
from modelos.leitor import Leitor
from modelos.material import Material


class Emprestimo:
    """Representa um empréstimo de material."""

    def __init__(self, leitor: Leitor, material: Material):
        self._leitor = leitor
        self._material = material
        self._data_emprestimo = date.today()
        self._data_devolucao = None

    @property
    def leitor(self) -> Leitor:
        return self._leitor

    @property
    def material(self) -> Material:
        return self._material

    def devolver(self) -> None:
            """Registra a devolução do material."""
            self._data_devolucao = date.today()

    @property
    def data_devolucao(self) -> date | None:
        """Retorna a data em que o material foi devolvido."""
        return self._data_devolucao

    @property
    def data_devolucao_prevista(self) -> date:
        prazo = self.material.calcular_prazo_dias()
        return self._data_emprestimo + timedelta(days=prazo)

    @property
    def dias_atraso(self) -> int:
        """Calcula quantos dias o empréstimo está atrasado."""
        data_referencia = self._data_devolucao or date.today()
        return max(0, (data_referencia - self.data_devolucao_prevista).days)