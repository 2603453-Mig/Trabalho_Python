from modelos.material import Material


class Livro(Material):
    """Representa um livro do acervo."""

    PRAZO_DIAS = 14

    def __init__(self, codigo: str, titulo: str, autor: str):
        super().__init__(codigo, titulo)

        if not autor.strip():
            raise ValueError("O autor não pode estar vazio.")

        self._autor = autor.strip()

    @property
    def autor(self) -> str:
        return self._autor

    def calcular_prazo_dias(self) -> int:
        return self.PRAZO_DIAS

    def tipo_material(self) -> str:
        return "Livro"

    @classmethod
    def from_string(cls, dados: str):
        codigo, titulo, autor = dados.split(";")
        return cls(codigo, titulo, autor)