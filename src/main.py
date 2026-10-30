from modelos.biblioteca import Biblioteca
from modelos.leitor import Leitor
from modelos.bibliotecario import Bibliotecario
from modelos.livro import Livro
from modelos.revista import Revista

from menu import Menu


def criar_dados_exemplo(biblioteca: Biblioteca) -> None:
    """Carrega dados iniciais para demonstração."""

    leitor = Leitor(
        "Maria Silva",
        "12345678900",
        "L001"
    )

    bibliotecario = Bibliotecario(
        "Carlos Souza",
        "98765432100",
        "B001"
    )

    livro = Livro(
        "LIV001",
        "Dom Casmurro",
        "Machado de Assis"
    )

    revista = Revista(
        "REV001",
        "National Geographic",
        120
    )

    biblioteca.cadastrar_leitor(leitor)
    biblioteca.cadastrar_bibliotecario(bibliotecario)
    biblioteca.cadastrar_material(livro)
    biblioteca.cadastrar_material(revista)


def main() -> None:
    """Inicializa o sistema."""

    biblioteca = Biblioteca("Biblioteca Central")

    criar_dados_exemplo(biblioteca)

    menu = Menu(biblioteca)
    menu.exibir()


if __name__ == "__main__":
    main()