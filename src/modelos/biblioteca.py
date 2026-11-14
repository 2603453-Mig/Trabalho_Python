from modelos.leitor import Leitor
from modelos.bibliotecario import Bibliotecario
from modelos.material import Material
from modelos.emprestimo import Emprestimo
from modelos.livro import Livro
from modelos.revista import Revista

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
    
        # Faz o relatório
    def gerar_relatorio(self) -> str:
        """Gera um relatório geral da biblioteca."""

        relatorio = []

        relatorio.append("\n========== RELATÓRIO DA BIBLIOTECA ==========")

        relatorio.append(f"\nNome da biblioteca: {self._nome}")

        relatorio.append("\n--- CADASTROS ---")
        relatorio.append(f"Total de leitores: {len(self._leitores)}")
        relatorio.append(
            f"Total de bibliotecários: {len(self._bibliotecarios)}"
        )

        # Separação dos materiais
        livros = [
            material for material in self._materiais
            if isinstance(material, Livro)
        ]

        revistas = [
            material for material in self._materiais
            if isinstance(material, Revista)
        ]

        relatorio.append("\n--- MATERIAIS CADASTRADOS ---")
        relatorio.append(f"Total de materiais: {len(self._materiais)}")

        relatorio.append("\n--- LIVROS ---")
        relatorio.append(f"Quantidade de livros: {len(livros)}")


        relatorio.append("\n--- REVISTAS ---")
        relatorio.append(f"Quantidade de revistas: {len(revistas)}")

        # Disponibilidade
        disponiveis = sum(
            1 for material in self._materiais
            if material.disponivel
        )

        emprestados = len(self._materiais) - disponiveis

        relatorio.append("\n--- DISPONIBILIDADE ---")
        relatorio.append(f"Materiais disponíveis: {disponiveis}")
        relatorio.append(f"Materiais emprestados: {emprestados}")

        # Empréstimos
        ativos = sum(
            1 for emprestimo in self._emprestimos
            if emprestimo.data_devolucao is None
        )

        devolvidos = len(self._emprestimos) - ativos

        relatorio.append("\n--- EMPRÉSTIMOS ---")
        relatorio.append(f"Empréstimos ativos: {ativos}")
        relatorio.append(f"Empréstimos devolvidos: {devolvidos}")
        relatorio.append(f"Total de empréstimos: {len(self._emprestimos)}")

        relatorio.append("\n============================================")

        return "\n".join(relatorio)
    