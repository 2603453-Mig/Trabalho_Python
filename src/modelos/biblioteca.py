from modelos.leitor import Leitor
from modelos.bibliotecario import Bibliotecario
from modelos.material import Material
from modelos.emprestimo import Emprestimo

from excecoes import (
    CadastroDuplicadoError,
    NaoEncontradoError,
    RegraNegocioError
)


class Biblioteca:
    """Gerencia os cadastros e operações da biblioteca."""

    def __init__(self, nome: str):
        self._nome = nome

        # Composição: a biblioteca mantém seus próprios objetos.
        self._leitores: list[Leitor] = []
        self._bibliotecarios: list[Bibliotecario] = []
        self._materiais: list[Material] = []
        self._emprestimos: list[Emprestimo] = []

    def cadastrar_leitor(self, leitor: Leitor) -> None:
        """Cadastra um novo leitor."""
        pass

    def cadastrar_bibliotecario(self, bibliotecario: Bibliotecario) -> None:
        """Cadastra um novo bibliotecário."""
        pass

    def cadastrar_material(self, material: Material) -> None:
        """Adiciona um material ao acervo."""
        pass

    def buscar_material(self, codigo: str) -> Material:
        """Busca um material pelo código."""
        raise NotImplementedError

    def buscar_leitor(self, matricula: str) -> Leitor:
        """Busca um leitor pela matrícula."""
        raise NotImplementedError

    def realizar_emprestimo(self, matricula: str, codigo: str) -> Emprestimo:
        """Realiza o empréstimo de um material."""
        raise NotImplementedError

    def realizar_devolucao(self, codigo: str) -> None:
        """Registra a devolução de um material."""
        raise NotImplementedError

    def listar_materiais(self) -> list[Material]:
        """Retorna todos os materiais cadastrados."""
        return self._materiais.copy()

    def listar_pessoas(self) -> list[Leitor | Bibliotecario]:
        """Retorna uma lista mista de pessoas."""
        return self._leitores.copy() + self._bibliotecarios.copy()

    def gerar_relatorio(self) -> str:
        """Gera um relatório do acervo e dos empréstimos."""
        raise NotImplementedError