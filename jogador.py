class Jogador:
    
    def __init__(self, nome, genero, peso):
        self.nome = nome
        self.genero = genero
        self.peso = peso
        self.taxa_eliminacao = 0.017
        self.teor_sangue = 0
        self.vezes = 0

    def aumenta_teor_sangue(self, volume, teor, densidade = 0.789, fator_conversao = 0.12):
        if self.genero == 'masculino':
            fator_genero = 0.58
        elif self.genero == 'feminino':
            fator_genero = 0.49
        else:
            fator_genero = 0.53  # Valor padrão se o gênero não for especificado corretamente
        alcool_consumido = (volume * teor * 0.9) / densidade
        
        # Equação de Widmark
        widmark = (alcool_consumido * fator_conversao / (self.peso * fator_genero))
        self.teor_sangue += widmark
    
    def diminui_teor_sangue(self, tempo_decorrido):
        self.teor_sangue -= self.taxa_eliminacao * tempo_decorrido

    def get_estado(self):     
        if self.teor_sangue < 0.03:
            return 'Sóbrio -- Comportamento: A pessoa aparenta estar normal.'
        elif 0.03 <= self.teor_sangue < 0.06:
            return 'Levemente Alcoolizado -- Leve euforia, relaxamento.'
        elif 0.06 <= self.teor_sangue < 0.1:
            return 'Proibído de dirigir pela lei brasileira -- Comportamento: Sentimentos embotados, redução da sensibilidade à dor, euforia, desinibição.'
        elif 0.1 <= self.teor_sangue < 0.25:
            return 'Consideravelmente Alcoolizado. Cuidado! -- Comportamento: Excesso, exuberância, possibilidade de náusea e vômito, reflexos mais lentos.'
        elif 0.25 <= self.teor_sangue < 0.35:
            return 'Muito Alcoolizado. Cuidado! -- Comportamento: Grandes possibilidades de vômito, excesso, exuberância, possibilidade de náusea e vômito, reflexos mais lentos.'
        elif 0.35 <= self.teor_sangue < 0.4:
            return 'Completamente Alcoolizado. Considere parar imediatamente! -- Comportamento: Estupor, depressão do sistema nervoso central, dificuldade em entender, alternância entre estados de consciência.'
        else:
            return 'Perigo a vida! -- Comportamento: Grave depressão do sistema nervoso central, coma, possibilidade de morte, problemas de respiração, ritmo cardíaco e nistagmo posicional.'
