class BibliotecaError(Exception):
    """Exceção base do sistema de biblioteca."""
    pass


class CadastroDuplicadoError(BibliotecaError):
    """Erro quando um cadastro já existe."""
    pass


class NaoEncontradoError(BibliotecaError):
    """Erro quando um objeto não é encontrado."""
    pass


class RegraNegocioError(BibliotecaError):
    """Erro quando uma operação viola uma regra de negócio."""
    pass