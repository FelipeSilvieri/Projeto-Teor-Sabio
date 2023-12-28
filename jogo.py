from jogador import Jogador

class Jogo:
    
    def __init__(self):
        self.jogador = None

    def iniciar_jogo(self, nome, genero, peso):
        self.jogador = Jogador(nome, genero, peso)

    def continuar_jogo(self, volume, teor, tempo_decorrido):
        if self.jogador:
            self.jogador.aumenta_teor_sangue(volume, teor)
            self.jogador.diminui_teor_sangue(tempo_decorrido)
            return self.jogador.get_estado()
        else:
            return 'O jogo ainda não foi iniciado.'
