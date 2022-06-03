import abc


class FilaBase(metaclass=abc.ABCMeta):
    codigo = 0
    fila = []
    clientes_atendidos = []
    senha_atual: str = ""
    
    def reseta_fila(self) -> None:
        if self.codigo >= 200:
            self.codigo = 0
        else:
            self.codigo += 1

    @abc.abstractclassmethod
    def gera_senha_atual(self):
        ...

    @abc.abstractclassmethod
    def atualiza_fila(self):
        ...

    @abc.abstractclassmethod
    def chama_cliente(self, caixa: int):
        ...
    