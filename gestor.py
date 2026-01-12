from decorators import log_operacao

class GestorFrota:
    def __init__(self):
        self.veiculos = []

    @log_operacao
    def adicionar_veiculo(self, veiculo):
        self.veiculos.append(veiculo)
