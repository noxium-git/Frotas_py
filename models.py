class Veiculo:
    def __init__(self, marca, preco):
        self.marca = marca
        self.preco = preco

    def calcular_imposto(self):
        return self.preco * 0.10

    def __str__(self):
        return f"Veiculo | {self.marca} | {self.preco:.2f}€ | imposto {self.calcular_imposto():.2f}€"


class CarroEletrico(Veiculo):
    def __init__(self, marca, preco, bateria_kwh):
        super().__init__(marca, preco)
        self.bateria_kwh = bateria_kwh

    def calcular_imposto(self):
        return self.preco * 0.05

    def __str__(self):
        return f"Elétrico | {self.marca} | {self.preco:.2f}€ | {self.bateria_kwh}kWh"
