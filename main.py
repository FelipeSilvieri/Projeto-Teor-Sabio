import sys
from PyQt5.QtWidgets import QApplication
from jogo import Jogo
from interface_grafica import InterfaceGrafica
from bebidas_cadastradas import BebidasCadastradas

class Main:   

    def __init__(self) -> None:
        self.bebidas_cadastradas = BebidasCadastradas
        self.app = QApplication(sys.argv)
        self.jogo = Jogo()
        self.interface = InterfaceGrafica(self.jogo, self.bebidas_cadastradas)
        self.interface.show()
        sys.exit(self.app.exec_())

if __name__ == '__main__':
    Main.__init__(self=Main)
    