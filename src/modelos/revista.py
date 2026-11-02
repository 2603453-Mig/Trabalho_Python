from modelos.material import Material


class Revista(Material):
    """Representa uma revista do acervo."""

    PRAZO_DIAS = 7

    def __init__(self, codigo: str, titulo: str, edicao: int):
        super().__init__(codigo, titulo)

        if not isinstance(edicao, int) or isinstance(edicao, bool) or edicao <= 0:
            raise ValueError("A edição deve ser um número inteiro positivo.")

        self._edicao = edicao

    @property
    def edicao(self) -> int:
        return self._edicao

    def calcular_prazo_dias(self) -> int:
        return self.PRAZO_DIAS

    def tipo_material(self) -> str:
        return "Revista"