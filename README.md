# Sistema de Gerenciamento de Biblioteca

## Integrantes
- Alisson Fortran
- Miguel Geme Stella
- Victor Leonardo Piconi Cardinali

## Descrição
Sistema em Python para gerenciar
uma biblioteca, seus leitores, funcionários,
materiais e empréstimos.

## Regras de negócio

- Cada leitor deve possuir uma matrícula única.
- Cada bibliotecário deve possuir um registro único.
- Cada material deve possuir um código único.
- Apenas materiais disponíveis podem ser emprestados.
- Cada leitor pode possuir no máximo 5 empréstimos ativos.
- Livros possuem prazo de empréstimo de 14 dias.
- Revistas possuem prazo de empréstimo de 7 dias.
- Um empréstimo não pode ser devolvido mais de uma vez.
- Atrasos na devolução podem gerar multas.
- Todos os empréstimos devem estar associados a um leitor
  e a um material cadastrado.

## Mapeamento das entidades

O sistema é composto pelas seguintes entidades:

### 1. Pessoas

| Entidade | Atributos | Comportamentos |
|---|---|---|
| `Pessoa` (abstrata) | Nome, documento | `apresentar()` |
| `Leitor` | Matrícula, empréstimos | `apresentar()`, `identificador` |
| `Bibliotecario` | Registro | `apresentar()`, `registro` |

### 2. Materiais

| Entidade | Atributos | Comportamentos |
|---|---|---|
| `Material` (abstrata) | Código, título, disponibilidade | `calcular_prazo_dias()`, `tipo_material()`, `validar_codigo()` |
| `Livro` | Autor | `calcular_prazo_dias()`, `tipo_material()`, `from_string()` |
| `Revista` | Edição | `calcular_prazo_dias()`, `tipo_material()` |

### 3. Operações e gerenciamento

| Entidade | Atributos | Comportamentos |
|---|---|---|
| `Emprestimo` | Leitor, material, data do empréstimo, data de devolução | `devolver()`, `dias_atraso`, `data_devolucao_prevista` |
| `Biblioteca` | Nome, leitores, bibliotecários, materiais, empréstimos | `cadastrar_leitor()`, `cadastrar_bibliotecario()`, `cadastrar_material()`, `buscar_material()`, `buscar_leitor()`, `realizar_emprestimo()`, `realizar_devolucao()`, `listar_materiais()`, `listar_pessoas()`, `gerar_relatorio()` |

### Descrição das entidades

- **Pessoa:** classe abstrata que representa os dados comuns de uma pessoa cadastrada no sistema.
- **Leitor:** representa uma pessoa que pode realizar empréstimos de materiais da biblioteca.
- **Bibliotecario:** representa o funcionário responsável pelas atividades administrativas da biblioteca.
- **Material:** classe abstrata que representa os materiais disponíveis no acervo.
- **Livro:** representa um livro cadastrado na biblioteca, possuindo autor e prazo de empréstimo próprio.
- **Revista:** representa uma revista do acervo, possuindo edição e prazo de empréstimo próprio.
- **Emprestimo:** registra a retirada de um material por um leitor e controla as datas de empréstimo e devolução.
- **Biblioteca:** gerencia os cadastros, materiais, leitores, bibliotecários e operações de empréstimo e devolução.

## Requisitos de POO

| Requisito | Conceito | Implementação |
|---|---|---|
| R1 | Classes e objetos | modelos/ |
| R2 | Composição | biblioteca.py e emprestimo.py |
| R3 | Encapsulamento | Atributos protegidos nas classes |
| R4 | Classmethod e Staticmethod | livro.py e material.py |
| R5 | Properties | pessoa.py, material.py e emprestimo.py |
| R6 | Atributos de classe | leitor.py e material.py |
| R7 | Herança e super() | pessoa.py, leitor.py e bibliotecario.py |
| R8 | Polimorfismo | material.py, livro.py e revista.py |
| R9 | Classe abstrata | pessoa.py e material.py |
| R10 | Protocol | interfaces.py |

## Diagrama de classes
Consultar docs/diagrama-classes.md
 (Para visualizar de forma compreensível, de Ctrl + shift + V)

## Como executar

No terminal, dentro da pasta do projeto:

python src/main.py
