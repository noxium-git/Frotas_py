from PySide6 import QtWidgets
from models import Veiculo, CarroEletrico
from gestor import GestorFrota


class Janela(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestão de Frotas")

        self.frota = GestorFrota()

        self.tipo = QtWidgets.QComboBox()
        self.tipo.addItems(["Veiculo", "CarroEletrico"])

        self.marca = QtWidgets.QLineEdit()
        self.preco = QtWidgets.QLineEdit()
        self.bateria = QtWidgets.QLineEdit()

        self.lista = QtWidgets.QListWidget()

        self.filtro = QtWidgets.QLineEdit()

        btn_add = QtWidgets.QPushButton("Adicionar")
        btn_rm = QtWidgets.QPushButton("Remover Selecionado")
        btn_exp = QtWidgets.QPushButton("Exportar")
        btn_filtrar = QtWidgets.QPushButton("Filtrar")
        btn_limpar = QtWidgets.QPushButton("Limpar filtro")

        btn_add.clicked.connect(self.adicionar)
        btn_rm.clicked.connect(self.remover)
        btn_exp.clicked.connect(self.exportar)
        btn_filtrar.clicked.connect(self.aplicar_filtro)
        btn_limpar.clicked.connect(self.atualizar_lista)

        form = QtWidgets.QFormLayout()
        form.addRow("Tipo:", self.tipo)
        form.addRow("Marca:", self.marca)
        form.addRow("Preço (€):", self.preco)
        form.addRow("Bateria (kWh):", self.bateria)

        botoes = QtWidgets.QHBoxLayout()
        botoes.addWidget(btn_add)
        botoes.addWidget(btn_rm)
        botoes.addWidget(btn_exp)

        filtro_l = QtWidgets.QHBoxLayout()
        filtro_l.addWidget(QtWidgets.QLabel("Marca:"))
        filtro_l.addWidget(self.filtro)
        filtro_l.addWidget(btn_filtrar)
        filtro_l.addWidget(btn_limpar)

        layout = QtWidgets.QVBoxLayout()
        layout.addLayout(form)
        layout.addLayout(botoes)
        layout.addLayout(filtro_l)
        layout.addWidget(self.lista)

        self.setLayout(layout)

    def adicionar(self):
        tipo = self.tipo.currentText().strip()
        marca = self.marca.text().strip()

        if not marca:
            QtWidgets.QMessageBox.warning(self, "Erro", "A marca não pode estar vazia.")
            return

        try:
            preco = float(self.preco.text().strip())
            if preco < 0:
                raise ValueError
        except ValueError:
            QtWidgets.QMessageBox.warning(self, "Erro", "Preço inválido. Exemplo: 12000 ou 12000.50")
            return

        if tipo == "Veiculo":
            veiculo = Veiculo(marca, preco)
        else:
            try:
                bateria = float(self.bateria.text().strip())
                if bateria <= 0:
                    raise ValueError
            except ValueError:
                QtWidgets.QMessageBox.warning(self, "Erro", "Bateria inválida. Exemplo: 40 ou 75")
                return

            veiculo = CarroEletrico(marca, preco, bateria)

        self.frota.adicionar_veiculo(veiculo)

        self.marca.clear()
        self.preco.clear()
        self.bateria.clear()

        self.atualizar_lista()

    def remover(self):
        indice = self.lista.currentRow()

        if indice == -1:
            QtWidgets.QMessageBox.information(self, "Info", "Seleciona um veículo para remover.")
            return

        if self.filtro.text().strip():
            QtWidgets.QMessageBox.warning(
                self,
                "Aviso",
                "Limpa o filtro antes de remover para evitar remover o veículo errado."
            )
            return

        ok = self.frota.remover_por_indice(indice)
        if not ok:
            QtWidgets.QMessageBox.warning(self, "Erro", "Não foi possível remover.")

        self.atualizar_lista()

    def exportar(self):
        if not self.frota.veiculos:
            QtWidgets.QMessageBox.information(self, "Info", "Não há veículos para exportar.")
            return

        self.frota.exportar("fleet_exportada.txt")
        QtWidgets.QMessageBox.information(
            self,
            "OK",
            "Inventário exportado para 'fleet_exportada.txt'"
        )

    def aplicar_filtro(self):
        marca = self.filtro.text().strip()

        if not marca:
            QtWidgets.QMessageBox.information(self, "Info", "Escreve uma marca para filtrar.")
            return

        filtrados = self.frota.filter_by_brand(marca)

        self.lista.clear()
        for v in filtrados:
            self.lista.addItem(str(v))

        if not filtrados:
            QtWidgets.QMessageBox.information(self, "Resultado", "Nenhum veículo encontrado.")

    def atualizar_lista(self):
        self.filtro.clear()
        self.lista.clear()

        for v in self.frota.veiculos:
            self.lista.addItem(str(v))
