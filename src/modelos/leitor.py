from modelos.pessoa import Pessoa
from excecoes import LimiteEmprestimosError

class Leitor(Pessoa):
    """Representa um leitor da biblioteca."""

    LIMITE_EMPRESTIMOS = 5

    def __init__(self, nome: str, documento: str, matricula: str):
        super().__init__(nome, documento)

        if not matricula.strip():
            raise ValueError("A matrícula não pode estar vazia.")

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

    @property
    def emprestimos(self) -> list:
        """Retorna uma cópia da lista de empréstimos."""
        return self._emprestimos.copy()

    def adicionar_emprestimo(self, emprestimo) -> None:
        """Adiciona um empréstimo ao leitor."""

        emprestimos_ativos = [
            item for item in self._emprestimos
            if item.data_devolucao is None
        ]

        if len(emprestimos_ativos) >= self.LIMITE_EMPRESTIMOS:

            raise LimiteEmprestimosError(
                "O leitor atingiu o limite de empréstimos ativos."
            )

        self._emprestimos.append(emprestimo)