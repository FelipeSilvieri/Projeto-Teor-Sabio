from PyQt5.QtWidgets import QDialog, QMainWindow, QPushButton, QLabel, QLineEdit, QWidget, QVBoxLayout, QStackedWidget, QComboBox, QHBoxLayout, QSizePolicy, QMessageBox
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt
import webbrowser


class InterfaceGrafica(QMainWindow):
      
    def __init__(self, jogo, bebidas_cadastradas):
        super().__init__()
        self.jogo = jogo
        self.volume = 0
        self.teor = 0
        self.texto_funcionamento = 'O jogo TeorSábio serve para realizar uma estimativa com base na modelagem da \nequação de Widmark para inferir os efeitos psicológicos, físicos e sociais \nadvindos da concentração de alcool no sangue do usuário. Esse cálculo é \nrealizado a partir de alguns dados (peso, genero, quantidade de alcool ingerido e tempo decorrido). \nO jogo serve apenas para fazer uma estimativa e realizar uma simulação estimada dos \nefeitos com base em estudos, mas não substitui de jeito nenhum a \nutilização de medidores precisos como o utilizado no teste de bafômetro! \nSe for beber não dirija.'
        self.bebidas = bebidas_cadastradas
        self.get_bebidas = self.bebidas.get_bebidas()
        self.combo_volume = True
        self.combo_teor = True
        self.cadastro_dialog = CadastroBebidaDialog()
        self.nome_c = self.cadastro_dialog.nome_c_input
        self.volume_c = self.cadastro_dialog.volume_c_input
        self.teor_c = self.cadastro_dialog.teor_c_input
        self.init_ui()

    def init_ui(self):
        
        self.setWindowTitle('Teor Sábio')
        self.setGeometry(100, 100, 600, 400)  # Aumenta o tamanho da janela

        # Página 1: Inserção de dados do jogador
        self.pagina1 = QWidget()
        self.layout_pagina1 = QVBoxLayout()
        
        # ---------------------------------------
        # ----------------- CSS -----------------
        # ---------------------------------------
        
        # Configuração da fonte
        font = QFont()
        font.setFamily('Arial')
        font.setPointSize(11)
        font.setBold(True)

        button = "QPushButton { background-color: lightgray; } QPushButton:hover { background-color: lightblue; }"
        start_button = "QPushButton { background-color: darkgreen; color: white; font-weight: bold; } QPushButton:hover { background-color: green; }"
        label = "QLabel { background-color: #1f1f1f; color: white;}"
        border_none = "QWidget { border: none; }"
        ingerir_bebida = "QPushButton { background-color: #fc7a57; color: white; font-weight: bold;} QPushButton:hover { background-color: #cb4b28; }"
        button_inserir_cadastrar = "QPushButton { background-color: lightgray; } QPushButton:hover { background-color: #fc7a57; }"
        button_cadastrar = "QPushButton { background-color: lightgray; } QPushButton:hover { background-color: lightgreen; }"
        
        # ---------------------------------------
        # ---------------------------------------
        # ---------------------------------------
        
        # Criar um novo widget para conter os botões "Como Funciona" e "Vídeo Explicativo"
        botoes_widget = QWidget(self)
        botoes_widget.setStyleSheet(border_none)
        botoes_layout = QHBoxLayout()

        # Botão "Como Funciona"
        botao_como_funciona = QPushButton('Como Funciona', self)
        botao_como_funciona.setStyleSheet(button)
        botao_como_funciona.clicked.connect(self.mostrar_como_funciona)
        botoes_layout.addWidget(botao_como_funciona)

        # -------------------------- Botão "Vídeo Explicativo" --------------------------
        botao_video_explicativo = QPushButton('Vídeo Equação Widmark', self)
        botao_video_explicativo.setStyleSheet(button)
        botao_video_explicativo.clicked.connect(self.mostrar_video_explicativo)
        botoes_layout.addWidget(botao_video_explicativo)
        botoes_widget.setLayout(botoes_layout)
        self.layout_pagina1.addWidget(botoes_widget)
        spacer = QLabel(self)
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.layout_pagina1.addWidget(spacer)
        # --------------------------------------------------------------------------------
                    
        imagem_label = QLabel(self)
        pixmap = QPixmap('logo_teor_sabio.png')
        pixmap = pixmap.scaled(350, 250, aspectRatioMode=1)
        imagem_label.setPixmap(pixmap)
        imagem_label.setAlignment(Qt.AlignCenter)
        self.layout_pagina1.addWidget(imagem_label)

        # --------------------------------------------------------------
        # ------------------------ Input Widget ------------------------ 
        # --------------------------------------------------------------
        
        self.label_nome = QLabel('Nome do Jogador:', self)
        self.label_nome.setStyleSheet(label)
        self.label_nome.setFont(font)
        self.layout_pagina1.addWidget(self.label_nome)

        self.pagina1.setLayout(self.layout_pagina1)

        self.nome_input = QLineEdit(self)
        self.layout_pagina1.addWidget(self.nome_input)

        self.label_genero = QLabel('Gênero:', self)
        self.label_genero.setStyleSheet(label)
        self.label_genero.setFont(font)
        self.layout_pagina1.addWidget(self.label_genero)

        self.genero_combo = QComboBox(self)
        self.genero_combo.addItem('Masculino')
        self.genero_combo.addItem('Feminino')
        self.layout_pagina1.addWidget(self.genero_combo)

        self.label_peso = QLabel('Peso (kg):', self)
        self.label_peso.setStyleSheet(label)
        self.label_peso.setFont(font)
        self.layout_pagina1.addWidget(self.label_peso)

        self.peso_input = QLineEdit(self)
        self.layout_pagina1.addWidget(self.peso_input)

        self.iniciar_btn = QPushButton('Iniciar Jogo', self)
        self.iniciar_btn.setStyleSheet(start_button)
        self.iniciar_btn.clicked.connect(self.mostrar_pagina2)
        self.layout_pagina1.addWidget(self.iniciar_btn)

        self.pagina1.setStyleSheet("border: 1px solid gray; padding: 10px;")
        self.pagina1.setLayout(self.layout_pagina1)

        # ------------------------------------------------------------
        # ------------------------------------------------------------
        # ------------------------------------------------------------

        # Página 2: Jogo propriamente dito
        self.pagina2 = QWidget()
        self.layout_pagina2 = QVBoxLayout()

        self.label_info_jogador = QLabel('', self)  # Mostrará nome do jogador
        self.label_info_jogador.setAlignment(Qt.AlignHCenter)
        self.label_info_jogador.setFont(font)
        self.layout_pagina2.addWidget(self.label_info_jogador)

        self.label_vezes_bebida = QLabel('', self)
        self.label_vezes_bebida.setAlignment(Qt.AlignCenter)
        self.label_vezes_bebida.setStyleSheet("color: #094509; border: none; font-weight: bold;")
        self.layout_pagina2.addWidget(self.label_vezes_bebida)
        
        self.label_teor_alcoolico = QLabel('', self)  # Mostrará teor alcoólico atual
        self.label_teor_alcoolico.setStyleSheet("background-color: #1f1f1f; border: none; font-weight: bold; color: white; font-size: 16px")
        self.label_teor_alcoolico.setAlignment(Qt.AlignCenter)
        self.layout_pagina2.addWidget(self.label_teor_alcoolico)
        
        # -------------------------------------------------------
        # ----------------- Cadastrar Bebida --------------------
        # -------------------------------------------------------
        # -------------------------------------------------------
        
        self.escolha_label = QLabel('Escolha abaixo uma opção de bebida já cadastrada.',self)
        self.escolha_label.setAlignment(Qt.AlignCenter)
        self.escolha_label.setStyleSheet('border: none;')
        self.layout_pagina2.addWidget(self.escolha_label)
        
        self.bebida_combo = QComboBox(self)
        for bebida in self.get_bebidas:
            self.bebida_combo.addItem(bebida["nome"])
        self.layout_pagina2.addWidget(self.bebida_combo)
        
        
        self.cadastrar_bebida_btn = QPushButton('Cadastrar Nova Bebida', self)
        self.cadastrar_bebida_btn.setStyleSheet(button_cadastrar)
        self.cadastrar_bebida_btn.clicked.connect(self.criar_widget_cadastro_bebida)
        self.layout_pagina2.addWidget(self.cadastrar_bebida_btn)
        
        self.inserir_bebida_btn = QPushButton('Inserir Info Bebida Por Escrito (ativa os campos abaixo \/)', self)
        self.inserir_bebida_btn.setStyleSheet(button_inserir_cadastrar)
        self.inserir_bebida_btn.clicked.connect(self.habilitar_inputs_bebida)
        self.layout_pagina2.addWidget(self.inserir_bebida_btn)
        # -------------------------------------------------------
        
        self.volume_input = QLineEdit(self)
        self.volume_input.setPlaceholderText('Volume de bebida (mL)')
        self.volume_input.setAlignment(Qt.AlignHCenter)
        self.layout_pagina2.addWidget(self.volume_input)
        

        self.teor_input = QLineEdit(self)
        self.teor_input.setPlaceholderText('Teor alcoólico (%)')
        self.teor_input.setAlignment(Qt.AlignHCenter)
        self.layout_pagina2.addWidget(self.teor_input)


        self.tempo_input = QLineEdit(self)
        self.tempo_input.setStyleSheet("background-color: #ffede8")
        self.tempo_input.setPlaceholderText('Tempo passado (horas) -- OBRIGATÓRIO! 0 para primeira...')

        self.tempo_input.setAlignment(Qt.AlignHCenter)
        self.layout_pagina2.addWidget(self.tempo_input)
            

        self.continuar_btn = QPushButton('Ingerir Bebida', self)
        self.continuar_btn.setStyleSheet(ingerir_bebida)
        self.continuar_btn.setFont(font)
        self.continuar_btn.clicked.connect(self.continuar_jogo)
        self.continuar_btn.setFixedHeight(int(self.continuar_btn.sizeHint().height() * 5))

        self.layout_pagina2.addWidget(self.continuar_btn)

        self.estado_label = QLabel('', self)
        self.estado_label.setStyleSheet("color: white; border: none; background-color:#1f1f1f; ")
        self.layout_pagina2.addWidget(self.estado_label)
        
        self.pagina2.setStyleSheet("border: 1px solid gray; padding: 10px;")
        self.pagina2.setLayout(self.layout_pagina2)

        
        # ------------------------------------------------
        # ----------------- Como Funciona ----------------
        # ------------------------------------------------

        self.como_funciona = QWidget()
        self.layout_como_funciona = QVBoxLayout()

        self.label_como_funciona = QLabel(self.texto_funcionamento, self)  # Mostrará o funcionamento do jogo
        self.label_como_funciona.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.label_como_funciona.setFont(font)

        self.layout_como_funciona.addWidget(self.label_como_funciona)
        # Botão "Voltar"
        botao_voltar = QPushButton('Voltar', self)
        botao_voltar.clicked.connect(self.mostrar_pagina1)
        self.layout_como_funciona.addWidget(botao_voltar)

        self.como_funciona.setLayout(self.layout_como_funciona)

        # ------------------------------------------------------
           
        # Adicionar páginas a um widget empilhado
        self.stacked_widget = QStackedWidget()
        self.stacked_widget.addWidget(self.pagina1)
        self.stacked_widget.addWidget(self.pagina2)
        self.stacked_widget.addWidget(self.como_funciona)
        self.setCentralWidget(self.stacked_widget)
        
        # Inicialização campos input disabled
        self.volume_input.setEnabled(False)
        self.teor_input.setEnabled(False)
        if self.tempo_input != None:
            self.tempo_input.setEnabled(True)

    def criar_widget_cadastro_bebida(self):
        result = self.cadastro_dialog.exec_()

        if result == QDialog.Accepted:
            # Processar o cadastro da bebida
            self.nome_c = self.cadastro_dialog.nome_c_input.text()
            self.volume_c = float(self.cadastro_dialog.volume_c_input.text())
            self.teor_c = float(self.cadastro_dialog.teor_c_input.text())
        
            mensagem = self.bebidas.cadastrar_bebida(self.nome_c, self.volume_c, self.teor_c)
            
            self.atualizar_combo_bebida()
            
            QMessageBox.information(self, 'Cadastro de Bebida', mensagem)
    
    def atualizar_combo_bebida(self):
        self.bebida_combo.clear()
        for bebida in self.get_bebidas:
            self.bebida_combo.addItem(bebida['nome'])
    
    def get_bebida_info(self):
        for bebida in self.get_bebidas:
            if bebida['nome'] == str(self.bebida_combo.currentText()):
                return bebida
    
    def mostrar_como_funciona(self):
        self.stacked_widget.setCurrentIndex(2)
    
    def mostrar_video_explicativo(self):
        youtube_url = "https://www.youtube.com/watch?v=kFExaZAb33o"
        webbrowser.open(youtube_url)
    
    def habilitar_inputs_bebida(self):
        self.volume_input.setEnabled(True)
        self.teor_input.setEnabled(True)
        if self.tempo_input != None:
            self.tempo_input.setEnabled(True)
        self.bebida_combo.setEnabled(False)
        self.combo_volume = False
        self.combo_teor = False
        
    
    def mostrar_pagina2(self):
        try:
            nome = self.nome_input.text()
            genero = self.genero_combo.currentText()
            peso = float(self.peso_input.text())
            self.jogo.iniciar_jogo(nome, genero, peso)
            self.stacked_widget.setCurrentIndex(1)  # Mostrar a página 2
            self.atualizar_info_jogador()
        except:
            pass
            
    def mostrar_pagina1(self):
        self.stacked_widget.setCurrentIndex(0)  # Mostrar a página 1

    def continuar_jogo(self):
        try:
            bebida_info = self.get_bebida_info()
            if self.combo_volume:   
                volume = float(bebida_info['volume'])
            else:    
                volume = float(self.volume_input.text())
                
            if self.combo_teor:
                teor = float(bebida_info['teor']/100)
            else:    
                teor = float(self.teor_input.text()) / 100   
            
            tempo_decorrido = float(self.tempo_input.text())
                
            estado = self.jogo.continuar_jogo(volume, teor, tempo_decorrido)
            self.atualizar_info_jogador()
            self.estado_label.setText(f'Estado: {estado}')
            self.tempo_passado = 0.01
        except ValueError:
            self.alert = QWidget()
            if self.tempo_input.text() == '' or self.tempo_input.text() == None:
                QMessageBox.information(self, 'Erro de inserção', 'Não deixe o campo "tempo decorrido" em branco!')
            else:
                QMessageBox.information(self, 'Erro!', 'Preencha os campos corretamente!')
        
    def atualizar_info_jogador(self):
        try:
            jogador = self.jogo.jogador
            if jogador.teor_sangue < 0:
                jogador.teor_sangue = 0
            if jogador:
                info = f'Jogador: {jogador.nome}\nGênero: {jogador.genero}'
                self.label_info_jogador.setText(info)
                self.label_info_jogador.setStyleSheet("border: none; background-color: #1f1f1f; color: white;")
                self.label_info_jogador.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                self.label_vezes_bebida.setText(f'Você ja bebeu {jogador.vezes} vezes!')
                self.label_teor_alcoolico.setText(f'BAC Atual (concentração de alcool no sangue): {jogador.teor_sangue:.2f}')
            jogador.vezes += 1
        except:
            pass

class CadastroBebidaDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Cadastro de Bebida')
        self.setGeometry(200, 200, 400, 200)

        input_style = "border: 1px solid gray; padding: 10px;"
        button_style = "border: none; padding: 10px; background-color: #fc7a57"
        layout = QVBoxLayout()

        self.nome_c_input = QLineEdit(self)
        self.nome_c_input.setPlaceholderText('Nome da bebida')
        self.nome_c_input.setStyleSheet(input_style)
        layout.addWidget(self.nome_c_input)

        self.volume_c_input = QLineEdit(self)
        self.volume_c_input.setPlaceholderText('Volume (mL)')
        self.volume_c_input.setStyleSheet(input_style)
        layout.addWidget(self.volume_c_input)

        self.teor_c_input = QLineEdit(self)
        self.teor_c_input.setPlaceholderText('Teor alcoólico (%)')
        self.teor_c_input.setStyleSheet(input_style)
        layout.addWidget(self.teor_c_input)

        cadastrar_btn = QPushButton('Cadastrar Bebida', self)
        cadastrar_btn.setStyleSheet(button_style)
        cadastrar_btn.clicked.connect(self.accept)
        layout.addWidget(cadastrar_btn)

        self.setLayout(layout)

