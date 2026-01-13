from decorators import log_operacao

class GestorFrota:
    def __init__(self):
        self.veiculos = []

    @log_operacao
    def adicionar_veiculo(self, veiculo):
        self.veiculos.append(veiculo)

    @log_operacao
    def remover_por_indice(self, indice):
        if 0 <= indice < len(self.veiculos):
            self.veiculos.pop(indice)
            return True
        return False

    def filter_by_brand(self, marca):
        return [v for v in self.veiculos if v.marca.lower() == marca.lower()]

    def exportar(self, caminho="fleet_exportada.txt"):
        with open(caminho, "w", encoding="utf-8") as f:
            for v in self.veiculos:
                f.write(str(v) + "\n")