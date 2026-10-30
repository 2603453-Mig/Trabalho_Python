from modelos.biblioteca import Biblioteca


class Menu:
    """Controla a interação entre o usuário e o sistema."""

    def __init__(self, biblioteca: Biblioteca):
        self._biblioteca = biblioteca

    def exibir(self) -> None:
        """Exibe o menu principal e controla o programa."""

        while True:
            print("\n========== SISTEMA DE BIBLIOTECA ==========")
            print("1 - Cadastrar leitor")
            print("2 - Cadastrar bibliotecário")
            print("3 - Cadastrar material")
            print("4 - Realizar empréstimo")
            print("5 - Realizar devolução")
            print("6 - Listar pessoas e materiais")
            print("7 - Buscar material")
            print("8 - Gerar relatório")
            print("0 - Sair")

            opcao = input("\nEscolha uma opção: ")

            try:
                if opcao == "0":
                    print("Encerrando o sistema...")
                    break

                elif opcao == "1":
                    self.cadastrar_leitor()

                elif opcao == "2":
                    self.cadastrar_bibliotecario()

                elif opcao == "3":
                    self.cadastrar_material()

                elif opcao == "4":
                    self.realizar_emprestimo()

                elif opcao == "5":
                    self.realizar_devolucao()

                elif opcao == "6":
                    self.listar_dados()

                elif opcao == "7":
                    self.buscar_material()

                elif opcao == "8":
                    self.gerar_relatorio()

                else:
                    print("Opção inválida.")

            except (ValueError, Exception) as erro:
                print(f"Erro: {erro}")

    def cadastrar_leitor(self) -> None:
        """Solicita os dados de um leitor."""
        print("Cadastro de leitor - A implementar.")

    def cadastrar_bibliotecario(self) -> None:
        """Solicita os dados de um bibliotecário."""
        print("Cadastro de bibliotecário - A implementar.")

    def cadastrar_material(self) -> None:
        """Solicita os dados de um material."""
        print("Cadastro de material - A implementar.")

    def realizar_emprestimo(self) -> None:
        """Solicita os dados de um empréstimo."""
        print("Empréstimo - A implementar.")

    def realizar_devolucao(self) -> None:
        """Solicita os dados de uma devolução."""
        print("Devolução - A implementar.")

    def listar_dados(self) -> None:
        """Exibe os dados cadastrados."""

        print("\n--- PESSOAS ---")

        for pessoa in self._biblioteca.listar_pessoas():
            print(pessoa.apresentar())

        print("\n--- MATERIAIS ---")

        for material in self._biblioteca.listar_materiais():
            print(f"{material.tipo_material()}: {material.titulo}")

    def buscar_material(self) -> None:
        """Busca um material pelo código."""
        print("Busca de material - A implementar.")

    def gerar_relatorio(self) -> None:
        """Exibe o relatório da biblioteca."""
        print(self._biblioteca.gerar_relatorio())