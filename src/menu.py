from modelos.biblioteca import Biblioteca
from modelos.leitor import Leitor
from modelos.bibliotecario import Bibliotecario
from modelos.livro import Livro
from modelos.revista import Revista

from excecoes import (
    CadastroDuplicadoError,
    NaoEncontradoError,
    MaterialIndisponivelError,
    LimiteEmprestimosError
)
        
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

            except Exception as erro:
                print(f"Erro inesperado: {erro}")
    
    #--------- COMEÇO DAS FUNÇÕES DE SOLICITAÇÕES -----------
                
    def solicitar_nome(self):
        """Verificar se o nome está adequado"""
        while True:
            nome = input("Nome: ").strip()

            try:
                if not nome.replace(" ", "").isalpha():
                    raise ValueError("Digite apenas letras.")

                return nome

            except ValueError as erro:
                print(f"Nome inválido: {erro}")

    def solicitar_documento(self):
        """Verificar se o documento está adequado"""
        while True:
            documento = input("CPF (11 números): ").strip()

            if not documento.isdigit():
                print("Documento inválido! Digite apenas números.")
                continue

            if len(documento) != 11:
                print("Documento inválido! Deve possuir 11 números.")
                continue

            return documento
    
    def solicitar_codigo(self):
        while True:
            codigo = input("Código do material: ").strip()

            if codigo:
                return codigo

            print("Código inválido! O campo não pode ficar vazio.")


    def solicitar_titulo(self):
        while True:
            titulo = input("Título: ").strip()

            if titulo:
                return titulo

            print("Título inválido! O campo não pode ficar vazio.")


    def solicitar_edicao(self):
        while True:
            edicao = input("Número da edição: ").strip()

            if not edicao.isdigit():
                print("Edição inválida! Digite apenas números.")
                continue

            edicao = int(edicao)

            if edicao <= 0:
                print("A edição deve ser maior que zero.")
                continue

            return edicao
    
    #----------- FIM DAS FUNÇÕES DE SOLICITAÇÕES -------------
    
    #--------- COMEÇO DAS FUNÇÕES DE CADASTRO -----------

    def cadastrar_leitor(self):
        print("\n--- Cadastro de Leitor ---")

        nome = self.solicitar_nome()
        documento = self.solicitar_documento()
        matricula = input("Matrícula: ")

        try:
            leitor = Leitor(nome, documento, matricula)
            self._biblioteca.cadastrar_leitor(leitor)

            print("\nLeitor cadastrado com sucesso!")

        except (ValueError, CadastroDuplicadoError) as erro:
            print(f"\nErro ao cadastrar leitor: {erro}")

    def cadastrar_bibliotecario(self) -> None:
        print("\n--- Cadastro de Bibliotecario ---")

        nome = self.solicitar_nome()
        documento = self.solicitar_documento()
        registro = input("Registro: ")

        try:
            bibliotecario = Bibliotecario(nome, documento, registro)
            self._biblioteca.cadastrar_bibliotecario(bibliotecario)

            print("\nBibliotecario cadastrado com sucesso!")

        except (ValueError, CadastroDuplicadoError) as erro:
            print(f"\nErro ao cadastrar bibliotecario: {erro}")

    def cadastrar_material(self):
        print("\n--- Cadastro de Material ---")
        print("1 - Livro")
        print("2 - Revista")

        tipo = input("Escolha o tipo de material: ").strip()

        try:
            if tipo == "1":
                codigo = self.solicitar_codigo()
                titulo = self.solicitar_titulo()
                autor = input("Autor: ").strip()

                material = Livro(codigo, titulo, autor)

            elif tipo == "2":
                codigo = self.solicitar_codigo()
                titulo = self.solicitar_titulo()
                edicao = self.solicitar_edicao()

                material = Revista(codigo, titulo, edicao)

            else:
                print("Opção inválida!")
                return

            self._biblioteca.cadastrar_material(material)

            print("\nMaterial cadastrado com sucesso!")

        except (ValueError, CadastroDuplicadoError) as erro:
            print(f"\nErro ao cadastrar material: {erro}")
    
    #----------- FIM DAS FUNÇÕES DE CADASTRO -------------

    def realizar_emprestimo(self) -> None:
        """Solicita os dados e realiza um empréstimo."""

        print("\n--- Realizar Empréstimo ---")

        matricula = input("Matrícula do leitor: ").strip()
        codigo = self.solicitar_codigo()

        try:
            emprestimo = self._biblioteca.realizar_emprestimo(
                matricula, codigo
            )

            print("\nEmpréstimo realizado com sucesso!")
            print(f"Leitor: {emprestimo.leitor.nome}")
            print(f"Material: {emprestimo.material.titulo}")
            print(
                f"Devolução prevista: "
                f"{emprestimo.data_devolucao_prevista.strftime('%d/%m/%Y')}"
            )

        except (NaoEncontradoError,
                MaterialIndisponivelError,
                LimiteEmprestimosError) as erro:

            print(f"\nNão foi possível realizar o empréstimo: {erro}")

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