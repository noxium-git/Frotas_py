from PySide6 import QtWidgets
from gui import Janela

def main():
    app = QtWidgets.QApplication([])
    w = Janela()
    w.show()
    app.exec()

if __name__ == "__main__":
    main()
