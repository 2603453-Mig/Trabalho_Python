class BibliotecaError(Exception):
    """Exceção base para todos os erros do sistema de biblioteca."""
    pass


# ---------- ERROS DE CADASTRO ----------

class CadastroDuplicadoError(BibliotecaError):
    """Erro quando um cadastro já existe no sistema."""
    pass


class NaoEncontradoError(BibliotecaError):
    """Erro quando um objeto solicitado não é encontrado."""
    pass


# ---------- ERROS DE EMPRÉSTIMO ----------

class MaterialIndisponivelError(BibliotecaError):
    """Erro quando tentam emprestar um material indisponível."""
    pass


class LimiteEmprestimosError(BibliotecaError):
    """Erro quando o leitor ultrapassa o limite de empréstimos ativos."""
    pass


class EmprestimoNaoEncontradoError(NaoEncontradoError):
    """Erro quando o empréstimo solicitado não é encontrado."""
    pass


class DevolucaoDuplicadaError(BibliotecaError):
    """Erro quando tentam devolver um material já devolvido."""
    pass