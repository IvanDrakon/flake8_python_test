from typing import Union

from fila_base import FilaBase
from constantes import CODIGO_PRIORITARIO
from estatistica_detalhada import EstatisticaDetalhada
from estatistica_resumida import EstatisticaResumida

Classes = Union[EstatisticaDetalhada, EstatisticaResumida]


class FilaPrioritaria(FilaBase):

    def gera_senha_atual(self) -> None:
        self.senha_atual = f'{CODIGO_PRIORITARIO}{self.codigo}'

    def chama_cliente(self, caixa: int) -> str:
        cliente_atual = self.fila.pop(0)
        self.clientes_atendidos.append(cliente_atual)
        return(f'Cliente Atual: {cliente_atual}, dirija-se ao caixa: {caixa}')

    def estatistica(self, retorna_estatistica: Classes) -> dict:

        return retorna_estatistica.roda_estatistica(self.clientes_atendidos)
