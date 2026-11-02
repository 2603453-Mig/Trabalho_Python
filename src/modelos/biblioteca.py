from modelos.leitor import Leitor
from modelos.bibliotecario import Bibliotecario
from modelos.material import Material
from modelos.emprestimo import Emprestimo

from interfaces import Identificavel

from excecoes import (
    CadastroDuplicadoError,
    NaoEncontradoError,
    RegraNegocioError
)


class Biblioteca:
    """Gerencia os cadastros e as operações da biblioteca."""

    def __init__(self, nome: str):
        self._nome = nome
        self._leitores: list[Leitor] = []
        self._bibliotecarios: list[Bibliotecario] = []
        self._materiais: list[Material] = []
        self._emprestimos: list[Emprestimo] = []

    def _verificar_identificador_unico(self, objeto: Identificavel, colecao: list) -> None:
        """Verifica se o identificador já está cadastrado."""

        for item in colecao:
            if item.identificador == objeto.identificador:
                raise CadastroDuplicadoError(
                    f"O identificador '{objeto.identificador}' já está cadastrado."
                )

    def cadastrar_leitor(self, leitor: Leitor) -> None:
        """Cadastra um leitor na biblioteca."""

        self._verificar_identificador_unico(leitor, self._leitores)
        self._leitores.append(leitor)

    def cadastrar_bibliotecario(self, bibliotecario: Bibliotecario) -> None:
        """Cadastra um bibliotecário na biblioteca."""

        self._verificar_identificador_unico(
            bibliotecario,
            self._bibliotecarios
        )
        self._bibliotecarios.append(bibliotecario)

    def cadastrar_material(self, material: Material) -> None:
        """Cadastra um material no acervo."""

        self._verificar_identificador_unico(material, self._materiais)
        self._materiais.append(material)

    def listar_materiais(self) -> list[Material]:
        return self._materiais.copy()

    def listar_pessoas(self) -> list[Leitor | Bibliotecario]:
        return self._leitores.copy() + self._bibliotecarios.copy()