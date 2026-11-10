from modelos.leitor import Leitor
from modelos.bibliotecario import Bibliotecario
from modelos.material import Material
from modelos.emprestimo import Emprestimo

from interfaces import Identificavel

from excecoes import (
    CadastroDuplicadoError,
    NaoEncontradoError,
    RegraNegocioError,
    MaterialIndisponivelError,
    DevolucaoDuplicadaError
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

# Funções relacionados aos leitores
    def cadastrar_leitor(self, leitor: Leitor) -> None:
        """Cadastra um leitor na biblioteca."""

        self._verificar_identificador_unico(leitor, self._leitores)
        self._leitores.append(leitor)

    def buscar_leitor(self, matricula: str) -> Leitor:
        """Busca um leitor pela matrícula."""

        for leitor in self._leitores:
            if leitor.matricula == matricula:
                return leitor

        raise NaoEncontradoError(
            f"Leitor com matrícula '{matricula}' não encontrado."
        )

# Funções relacionados aos bibliotecarios
    def cadastrar_bibliotecario(self, bibliotecario: Bibliotecario) -> None:
        """Cadastra um bibliotecário na biblioteca."""

        self._verificar_identificador_unico(
            bibliotecario,
            self._bibliotecarios
        )
        self._bibliotecarios.append(bibliotecario)

#Funções relacionados aos materiais
    def cadastrar_material(self, material: Material) -> None:
        """Cadastra um material no acervo."""

        self._verificar_identificador_unico(material, self._materiais)
        self._materiais.append(material)

    def buscar_material(self, codigo: str) -> Material:
        """Busca um material pelo código."""

        for material in self._materiais:
            if material.codigo == codigo:
                return material

        raise NaoEncontradoError(
            f"Material com código '{codigo}' não encontrado."
        )

    def listar_materiais(self) -> list[Material]:
        return self._materiais.copy()
        

    def listar_pessoas(self) -> list[Leitor | Bibliotecario]:
        return self._leitores.copy() + self._bibliotecarios.copy()

# Função de emprestimo e devolução
    def realizar_emprestimo(self, matricula: str, codigo: str) -> Emprestimo:
        """Realiza o empréstimo de um material para um leitor."""

        leitor = self.buscar_leitor(matricula)
        material = self.buscar_material(codigo)

        if not material.disponivel:
            raise MaterialIndisponivelError(
                "Este material já está emprestado."
            )

        emprestimo = Emprestimo(leitor, material)

        # Verifica o limite e registra no leitor.
        leitor.adicionar_emprestimo(emprestimo)

        # Atualiza a disponibilidade do material.
        material.marcar_emprestado()

        # Registra o empréstimo na biblioteca.
        self._emprestimos.append(emprestimo)

        return emprestimo

    def realizar_devolucao(self, codigo: str) -> Emprestimo:
        """Registra a devolução de um material."""

        material = self.buscar_material(codigo)

        for emprestimo in self._emprestimos:
            if emprestimo.material.codigo == codigo:

                if emprestimo.data_devolucao is not None:
                    raise DevolucaoDuplicadaError(
                        "Este material já foi devolvido."
                    )

                emprestimo.devolver()
                material.marcar_disponivel()

                return emprestimo

        raise NaoEncontradoError(
            f"Não existe empréstimo registrado para o material '{codigo}'."
        )